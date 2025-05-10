from unittest.mock import patch

import requests


# 배달 요청을 보내는 함수
def request_delivery(address, menu):
    response = requests.post(
        "https://delivery-api.example.com/order",
        json={"address": address, "menu": menu},
    )
    return response.json()


@patch("requests.post")
def test_request_delivery(mock_post):
    # 실제 배달은 안 가지만, 성공했다고 응답을 설정
    mock_post.return_value.json.return_value = {
        "status": "success",
        "delivery_id": "12345",
        "eta": "30분 후 도착 완료함",
    }

    result = request_delivery("서울시 강남구", ["치킨", "콜라"])

    # 결과 검증
    assert result["status"] == "success"
    assert result["delivery_id"] == "12345"
    mock_post.assert_called_with(
        "https://delivery-api.example.com/order",
        json={"address": "서울시 강남구", "menu": ["치킨", "콜라"]},
    )
