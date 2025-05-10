from datetime import datetime, timedelta, timezone
from typing import Optional


class Post:
    def __init__(
        self,
        id: int,
        title: str,
        contents: str,
        tag: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.title = title
        self.contents = contents
        self.tag = tag
        now = datetime.now(timezone(timedelta(hours=9)))  # KST
        self.created_at = created_at or now
        self.updated_at = updated_at or now

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "contents": self.contents,
            "tag": self.tag,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Post":
        return cls(
            id=data["id"],
            title=data["title"],
            contents=data["contents"],
            tag=data.get("tag"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
