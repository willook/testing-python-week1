# 게시글 API with 욕설 필터링

FastAPI를 사용한 게시글 API입니다. 게시글의 제목과 내용에 욕설이 포함되어 있는지 검사하는 기능이 포함되어 있습니다.

## 기능

- 게시글 CRUD API
- 욕설 필터링 기능
- SQLite 데이터베이스 사용

## 설치 및 실행

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 서버 실행
```bash
uvicorn app.main:app --reload
```

4. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 테스트 실행

```bash
pytest
```

## API 엔드포인트

- `GET /posts/`: 모든 게시글 조회
- `GET /posts/{post_id}`: 특정 게시글 조회
- `POST /posts/`: 새로운 게시글 생성
- `PUT /posts/{post_id}`: 게시글 수정
- `DELETE /posts/{post_id}`: 게시글 삭제

## 욕설 필터링

현재는 간단한 문자열 매칭을 사용하여 욕설을 검사합니다. 실제 프로덕션 환경에서는 더 정교한 욕설 필터링 알고리즘을 사용하는 것이 좋습니다. 