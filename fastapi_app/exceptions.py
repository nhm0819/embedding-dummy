import logging
import traceback

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger("uvicorn")


async def exception_handler(_: Request, e: Exception):
    logger.error(f"Exception => {type(e).__name__}: {str(e)}\n{traceback.format_exc()}")
    content = dict(message=str(e))
    return JSONResponse(status_code=500, content=content)


async def http_exception_handler(_: Request, e: HTTPException):
    logger.error(f"Exception => {type(e).__name__}: {str(e)}\n{traceback.format_exc()}")
    content = dict(message=e.detail)
    return JSONResponse(status_code=e.status_code, content=content)


async def validation_exception_handler(_: Request, e: RequestValidationError):
    logger.error(f"Validation Error: {e}\n{traceback.format_exc()}")

    messages = []
    for error in e.errors():
        field = error.get("loc", [])[-1]
        msg = error.get("msg")
        messages.append(f"{field}: {msg}")

    friendly_message = "Please check these parameters: " + ", ".join(messages)
    content = dict(message=friendly_message)
    return JSONResponse(status_code=422, content=content)
