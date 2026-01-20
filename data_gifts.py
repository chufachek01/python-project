from dataclasses import dataclass


@dataclass(frozen=True)
class Gift:
    id: int
    title: str
    nft_url: str  # реальная ссылка вида https://t.me/nft/...


# ⚠️ ВАЖНО:
# - nft_url ДОЛЖЕН быть реальным, иначе Telegram покажет STARGIFT_SLUG_INVALID
# - если ссылки пока нет — оставляй пустую строку ""
# - бот это обработает корректно (покажет "нет ссылки")

GIFTS: list[Gift] = [
    Gift(
        id=1,
        title="Toy Bear #18350",
        nft_url="https://t.me/nft/toybear-18350",
    ),
    Gift(
        id=2,
        title="Toy Bear #24112",
        nft_url="https://t.me/nft/toybear-24112",  # пока нет ссылки
    ),
    Gift(
        id=3,
        title="Toy Bear #55781",
        nft_url="https://t.me/nft/toybear-55781",
    ),
    Gift(
        id=4,
        title="Pixel Cat #12004",
        nft_url="https://t.me/nft/pixelcat-12004",
    ),
    Gift(
        id=5,
        title="Pixel Cat #33291",
        nft_url="https://t.me/nft/pixelcat-33291",
    ),
    Gift(
        id=6,
        title="Star Duck #9911",
        nft_url="https://t.me/nft/starduck-9911",
    ),
    Gift(
        id=7,
        title="Star Duck #18220",
        nft_url="https://t.me/nft/starduck-18220",
    ),
    Gift(
        id=8,
        title="Mini Bot #501",
        nft_url="https://t.me/nft/minibot-501",
    ),
    Gift(
        id=9,
        title="Mini Bot #774",
        nft_url="https://t.me/nft/minibot-774",
    ),
    Gift(
        id=10,
        title="Mini Bot #902",
        nft_url="https://t.me/nft/minibot-902",
    ),
]
