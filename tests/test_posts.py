from fastapi.testclient import TestClient


def test_create_post(client: TestClient):
    """게시글 생성 테스트"""
    response = client.post(
        "",
        json={"title": "테스트 제목", "contents": "테스트 내용", "tag": "테스트"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "테스트 제목"
    assert data["contents"] == "테스트 내용"
    assert data["tag"] == "테스트"
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_create_post_with_profanity(client: TestClient):
    """욕설이 포함된 게시글 생성 테스트"""
    response = client.post(
        "",
        json={
            "title": "비속어1이 포함된 제목",
            "contents": "테스트 내용",
            "tag": "테스트",
        },
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "게시글에 욕설이 포함되어 있습니다."


def test_get_posts(client: TestClient):
    """게시글 목록 조회 테스트"""
    # 테스트 데이터 생성
    client.post(
        "",
        json={"title": "테스트 제목 1", "contents": "테스트 내용 1", "tag": "테스트"},
    )
    client.post(
        "",
        json={"title": "테스트 제목 2", "contents": "테스트 내용 2", "tag": "테스트"},
    )

    response = client.get("")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "테스트 제목 1"
    assert data[1]["title"] == "테스트 제목 2"


def test_get_post(client: TestClient):
    """특정 게시글 조회 테스트"""
    # 테스트 데이터 생성
    create_response = client.post(
        "",
        json={"title": "테스트 제목", "contents": "테스트 내용", "tag": "테스트"},
    )
    post_id = create_response.json()["id"]

    response = client.get(f"/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "테스트 제목"
    assert data["contents"] == "테스트 내용"
    assert data["tag"] == "테스트"


def test_get_nonexistent_post(client: TestClient):
    """존재하지 않는 게시글 조회 테스트"""
    response = client.get("/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "게시글을 찾을 수 없습니다."


def test_update_post(client: TestClient):
    """게시글 수정 테스트"""
    # 테스트 데이터 생성
    create_response = client.post(
        "",
        json={"title": "테스트 제목", "contents": "테스트 내용", "tag": "테스트"},
    )
    post_id = create_response.json()["id"]

    response = client.put(
        f"/{post_id}",
        json={"title": "수정된 제목", "contents": "수정된 내용", "tag": "수정된 태그"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "수정된 제목"
    assert data["contents"] == "수정된 내용"
    assert data["tag"] == "수정된 태그"


def test_update_post_with_profanity(client: TestClient):
    """욕설이 포함된 게시글 수정 테스트"""
    # 테스트 데이터 생성
    create_response = client.post(
        "",
        json={"title": "테스트 제목", "contents": "테스트 내용", "tag": "테스트"},
    )
    post_id = create_response.json()["id"]

    response = client.put(
        f"/{post_id}",
        json={
            "title": "비속어1이 포함된 제목",
            "contents": "테스트 내용",
            "tag": "테스트",
        },
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "게시글에 욕설이 포함되어 있습니다."


def test_delete_post(client: TestClient):
    """게시글 삭제 테스트"""
    # 테스트 데이터 생성
    create_response = client.post(
        "",
        json={"title": "테스트 제목", "contents": "테스트 내용", "tag": "테스트"},
    )
    post_id = create_response.json()["id"]

    response = client.delete(f"/{post_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "게시글이 삭제되었습니다."

    # 삭제 확인
    get_response = client.get(f"/{post_id}")
    assert get_response.status_code == 404
