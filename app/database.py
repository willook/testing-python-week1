from typing import Dict, Generator

# 인메모리 저장소
posts: Dict[int, dict] = {}
current_id = 1


def get_db() -> Generator[Dict[int, dict], None, None]:
    """인메모리 저장소를 반환합니다."""
    yield posts


def get_next_id() -> int:
    """다음 ID를 가져오고 current_id를 증가시킵니다."""
    global current_id
    next_id = current_id
    current_id += 1
    return next_id


def reset_db() -> None:
    """테스트용 DB 초기화 함수"""
    global posts, current_id
    posts = {}
    current_id = 1
