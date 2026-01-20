import re
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

NFT_LINK_RE = re.compile(r"^https://t\.me/nft/[A-Za-z0-9_]+-\d+$")


def kb_main(nft_url: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    if nft_url and NFT_LINK_RE.match(nft_url):
        kb.add(InlineKeyboardButton(text="Посмотреть НФТ", url=nft_url))
    else:
        kb.button(text="Посмотреть НФТ (нет ссылки)", callback_data="no_link")

    kb.button(text="Перекрутить", callback_data="reroll")
    kb.adjust(1)
    return kb.as_markup()
