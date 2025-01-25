from io import BytesIO

import numpy as np
from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response, StreamingResponse

from fastapi_app.enums import BigEndian
from fastapi_app.schemas import UserEmbeddingRequest, UserFeature

embedding_router = APIRouter()


class OctetStreamResponse(Response):
    media_type = "application/octet-stream"


@embedding_router.get("/", response_class=JSONResponse)
async def root():
    """ping"""
    return {"status": "healthy"}


@embedding_router.post("/v1/embedding/user/{user_id}", response_model=UserFeature)
async def embedding(user_id: int, command: UserEmbeddingRequest):
    """
    create dummy vector
    response json
    """
    dtype = command.dtype
    size = command.size

    feature = np.random.standard_normal((1, size)).astype(BigEndian[dtype].value)

    user_vector_list = feature.astype("float64").tolist()  # change to 64bit float type
    return UserFeature(user_vector=user_vector_list)


@embedding_router.post(
    "/v1/embedding/user/{user_id}/octet", response_class=OctetStreamResponse
)
async def embedding_octet(command: UserEmbeddingRequest):
    """
    create dummy vector
    response octet
    """
    dtype = command.dtype
    size = command.size

    feature = np.random.standard_normal((1, size)).astype(BigEndian[dtype].value)
    content = feature.tobytes()

    return Response(content=content, media_type="application/octet-stream")


@embedding_router.post(
    "/v1/embedding/user/{user_id}/octet/stream", response_class=OctetStreamResponse
)
async def embedding_octet_stream(command: UserEmbeddingRequest):
    """
    create dummy vector
    response octet stream
    """
    dtype = command.dtype
    size = command.size

    feature = np.random.standard_normal((1, size)).astype(BigEndian[dtype].value)
    stream = BytesIO(feature.tobytes())

    return StreamingResponse(content=stream, media_type="application/octet-stream")
