from typing import List

DEFAULT_PROFANITY_LIST = ["비속어"]


class ProfanityValidator:
    def __init__(self, profanity_list: List[str] = None):
        self.profanity_list = profanity_list or DEFAULT_PROFANITY_LIST

    def contains_profanity(self, text: str) -> bool:
        """주어진 텍스트에 욕설이 포함되어 있는지 확인합니다."""
        return any(profanity in text for profanity in self.profanity_list)
