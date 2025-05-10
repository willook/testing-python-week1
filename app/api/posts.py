from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.database import get_db
from app.models.post import Post, PostCreate, PostUpdate
from app.services.post_service import PostService

router = APIRouter()


class PostIdRequest(BaseModel):
    post_id: int


@router.get("/", response_model=List[Post])
async def get_posts(
    skip: int = 0, limit: int = 100, db: Dict[int, dict] = Depends(get_db)
):
    """모든 게시글을 조회합니다."""
    service = PostService(db)
    return service.get_posts()


@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int, db: Dict[int, dict] = Depends(get_db)):
    """특정 게시글을 조회합니다."""
    service = PostService(db)
    post = service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return post


@router.post("/", response_model=Post)
async def create_post(post: PostCreate, db: Dict[int, dict] = Depends(get_db)):
    """새로운 게시글을 생성합니다."""
    service = PostService(db)
    return service.create_post(post)


@router.put("/{post_id}", response_model=Post)
async def update_post(
    post_id: int, post: PostUpdate, db: Dict[int, dict] = Depends(get_db)
):
    """게시글을 수정합니다."""
    service = PostService(db)
    updated_post = service.update_post(post_id, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return updated_post


@router.delete("/{post_id}")
async def delete_post(post_id: int, db: Dict[int, dict] = Depends(get_db)):
    """게시글을 삭제합니다."""
    service = PostService(db)
    if not service.delete_post(post_id):
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return {"message": "게시글이 삭제되었습니다."}
