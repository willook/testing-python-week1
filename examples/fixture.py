import pytest


class Spoon:
    def __init__(self):
        self.clean = True

    def use(self):
        self.clean = False


@pytest.fixture
def spoon():
    # 매 테스트마다 새 숟가락 제공
    return Spoon()


def test_soup(spoon):
    assert spoon.clean
    spoon.use()
    assert not spoon.clean


def test_stew(spoon):
    # 이전 테스트에서 사용된 흔적 없음
    assert spoon.clean
    spoon.use()
    assert not spoon.clean
