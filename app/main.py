from fastapi import FastAPI

from app.api import posts

app = FastAPI(
    title="Post API",
    description="게시글 API with 욕설 필터링",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# 라우터 등록
app.include_router(posts.router, prefix="/posts", tags=["posts"])
