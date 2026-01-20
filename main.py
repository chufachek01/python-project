import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

from config import load_config
from data_gifts import GIFTS, Gift
from keyboards import kb_main
from render import render_start
from state import (
    set_root_message,
    get_root_message,
    set_current_gift,
    get_current_gift,
    set_has_screenshot,
    get_has_screenshot,
)

logging.basicConfig(level=logging.INFO)


def pick_gift(exclude_id: int | None = None) -> Gift:
    pool = [g for g in GIFTS if g.id != exclude_id]
    return random.choice(pool) if pool else random.choice(GIFTS)


def get_gift_by_id(gift_id: int | None) -> Gift:
    for g in GIFTS:
        if g.id == gift_id:
            return g
    return pick_gift()


async def upsert_root_message(
    bot: Bot,
    user_id: int,
    chat_id: int,
    caption: str,
    gift: Gift,
    image_path,
):
    root_id = get_root_message(user_id)

    if root_id:
        try:
            await bot.edit_message_caption(
                chat_id=chat_id,
                message_id=root_id,
                caption=caption,
                reply_markup=kb_main(gift.nft_url),
            )
            return
        except Exception:
            pass

    photo = FSInputFile(image_path)
    msg = await bot.send_photo(
        chat_id=chat_id,
        photo=photo,
        caption=caption,
        reply_markup=kb_main(gift.nft_url),
    )
    set_root_message(user_id, msg.message_id)


async def main():
    cfg = load_config()

    bot = Bot(
        token=cfg.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    @dp.message(CommandStart())
    async def on_start(message: Message):
        user_id = message.from_user.id
        chat_id = message.chat.id

        gift = pick_gift()
        set_current_gift(user_id, gift.id)

        caption = render_start(
            cfg.start_title,
            cfg.start_subtitle,
            get_has_screenshot(user_id),
        )

        await upsert_root_message(
            bot,
            user_id,
            chat_id,
            caption,
            gift,
            cfg.image_path,
        )

    @dp.callback_query(F.data == "reroll")
    async def on_reroll(callback: CallbackQuery):
        await callback.answer()

        user_id = callback.from_user.id
        prev = get_current_gift(user_id)

        gift = pick_gift(exclude_id=prev)
        set_current_gift(user_id, gift.id)

        caption = render_start(
            cfg.start_title,
            cfg.start_subtitle,
            get_has_screenshot(user_id),
        )

        await callback.message.edit_caption(
            caption=caption,
            reply_markup=kb_main(gift.nft_url),
        )

    @dp.callback_query(F.data == "no_link")
    async def on_no_link(callback: CallbackQuery):
        await callback.answer(
            "Ссылка на НФТ не задана или неверная",
            show_alert=True,
        )

    @dp.message(F.photo)
    async def on_photo(message: Message):
        user_id = message.from_user.id
        chat_id = message.chat.id

        set_has_screenshot(user_id, True)

        gift = get_gift_by_id(get_current_gift(user_id))
        caption = render_start(
            cfg.start_title,
            cfg.start_subtitle,
            True,
        )

        await upsert_root_message(
            bot,
            user_id,
            chat_id,
            caption,
            gift,
            cfg.image_path,
        )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
