from dataclasses import dataclass
from pathlib import Path

BOT_TOKEN = "8242611057:AAGNLww2RFXAcXFa4ty_igJAVLlLD1hByHw"

BASE_DIR = Path(__file__).resolve().parent
START_IMAGE_PATH = BASE_DIR / "banner.png"


@dataclass(frozen=True)
class Config:
    bot_token: str

    start_title: str = (
        "Вам выпал нфт, который вы можете посмотреть по кнопке\n"
        "Посмотреть НФТ"
    )

    start_subtitle: str = (
        "Для получения необходимо поставить лайк на комментарий из TikTok,\n"
        "с моим юзом с которого узнали обо мне и написать в ответ на него\n"
        "«правда работает»"
    )

    image_path: Path = START_IMAGE_PATH


def load_config() -> Config:
    token = BOT_TOKEN.strip()
    if not token:
        raise RuntimeError("BOT_TOKEN is empty")
    return Config(bot_token=token)
