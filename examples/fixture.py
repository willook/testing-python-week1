import pytest


@pytest.fixture
def sample_data():
    return {"name": "이종화", "age": 20}


def test_name(sample_data):
    assert sample_data["name"] == "이종화"


def test_age(sample_data):
    assert sample_data["age"] == 20
