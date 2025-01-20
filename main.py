import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "fastapi_app.app:app",
        host="127.0.0.1",
        port=8002,
        log_level="debug",
        reload=True,
    )
