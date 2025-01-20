from typing import List, Literal

from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    # user_id: str = Field(..., description="User ID")
    email: str = Field(..., description="Email")
    nickname: str = Field(..., description="Nickname")
    favorite: str | None = Field(default=None, description="Favorite")
    lat: float | None = Field(default=None, description="Lat")
    lng: float | None = Field(default=None, description="Lng")


class UserEmbeddingRequest(UserInfo):
    size: int = Field(default=2048, description="Vector size : (1, size)")
    dtype: Literal["float16", "float32", "float64"] = Field(
        default="float16", description="Vector Data Type (float16, float32, float64)"
    )


class UserFeature(BaseModel):
    user_vector: List[List[float]]
