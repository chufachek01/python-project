from typing import Dict, Optional

ROOT_MESSAGE_BY_USER: Dict[int, int] = {}
CURRENT_GIFT_BY_USER: Dict[int, int] = {}
HAS_SCREENSHOT_BY_USER: Dict[int, bool] = {}


def set_root_message(user_id: int, message_id: int) -> None:
    ROOT_MESSAGE_BY_USER[user_id] = message_id


def get_root_message(user_id: int) -> Optional[int]:
    return ROOT_MESSAGE_BY_USER.get(user_id)


def set_current_gift(user_id: int, gift_id: int) -> None:
    CURRENT_GIFT_BY_USER[user_id] = gift_id


def get_current_gift(user_id: int) -> Optional[int]:
    return CURRENT_GIFT_BY_USER.get(user_id)


def set_has_screenshot(user_id: int, value: bool) -> None:
    HAS_SCREENSHOT_BY_USER[user_id] = value


def get_has_screenshot(user_id: int) -> bool:
    return HAS_SCREENSHOT_BY_USER.get(user_id, False)
