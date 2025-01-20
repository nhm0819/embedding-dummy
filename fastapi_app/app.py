from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException

from fastapi_app import exceptions
from fastapi_app.router import embedding_router


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="embedding server",
        description="dummy embedding server",
    )

    app_.include_router(embedding_router)

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app_


app = create_app()
app.add_exception_handler(Exception, exceptions.exception_handler)
app.add_exception_handler(HTTPException, exceptions.http_exception_handler)
app.add_exception_handler(
    RequestValidationError, exceptions.validation_exception_handler
)
