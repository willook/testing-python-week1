from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    contents: str = Field(..., min_length=1)
    tag: Optional[str] = Field(None, max_length=50)


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
