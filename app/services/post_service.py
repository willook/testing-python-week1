from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

from fastapi import HTTPException

from app.database import get_next_id
from app.models.database import Post
from app.models.post import PostCreate, PostUpdate
from app.validators.profanity_validator import ProfanityValidator


class PostService:
    def __init__(self, db: Dict[int, dict]):
        self.db = db
        self.profanity_validator = ProfanityValidator()

    def get_posts(self) -> List[Post]:
        """모든 게시글을 조회합니다."""
        return [Post.from_dict(post) for post in self.db.values()]

    def get_post(self, post_id: int) -> Optional[Post]:
        """특정 게시글을 조회합니다."""
        post = self.db.get(post_id)
        return Post.from_dict(post) if post else None

    def create_post(self, post: PostCreate) -> Post:
        """새로운 게시글을 생성합니다."""
        if self.profanity_validator.contains_profanity(
            post.title
        ) or self.profanity_validator.contains_profanity(post.contents):
            raise HTTPException(
                status_code=400, detail="게시글에 욕설이 포함되어 있습니다."
            )

        post_id = get_next_id()
        now = datetime.now(timezone(timedelta(hours=9)))  # KST
        self.db[post_id] = {
            "id": post_id,
            "title": post.title,
            "contents": post.contents,
            "tag": post.tag,
            "created_at": now,
            "updated_at": now,
        }
        return Post.from_dict(self.db[post_id])

    def update_post(self, post_id: int, post: PostUpdate) -> Optional[Post]:
        """게시글을 수정합니다."""
        if self.profanity_validator.contains_profanity(
            post.title
        ) or self.profanity_validator.contains_profanity(post.contents):
            raise HTTPException(
                status_code=400, detail="게시글에 욕설이 포함되어 있습니다."
            )

        if post_id not in self.db:
            return None

        self.db[post_id].update(
            {
                "title": post.title,
                "contents": post.contents,
                "tag": post.tag,
                "updated_at": datetime.now(timezone(timedelta(hours=9))),  # KST
            }
        )
        return Post.from_dict(self.db[post_id])

    def delete_post(self, post_id: int) -> bool:
        """게시글을 삭제합니다."""
        if post_id not in self.db:
            return False

        del self.db[post_id]
        return True
