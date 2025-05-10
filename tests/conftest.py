import pytest
from fastapi.testclient import TestClient

from app.database import get_db, reset_db
from app.main import app


@pytest.fixture(autouse=True)
def reset_test_db():
    """각 테스트 전에 데이터베이스를 초기화합니다."""
    reset_db()


def override_get_db():
    """테스트용 인메모리 저장소를 반환합니다."""
    from app.database import posts

    yield posts


@pytest.fixture
def client():
    """테스트 클라이언트를 생성합니다."""
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app, base_url="http://testserver/posts") as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def profanity_list():
    return ["파인애플피자", "민트초코", "파인애플 피자", "민트 초코"]
