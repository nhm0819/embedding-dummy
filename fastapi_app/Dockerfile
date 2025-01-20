FROM python:3.11-slim

COPY ./fastapi_app/requirements.txt /app/requirements.txt
#RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./fastapi_app/ /app/fastapi_app/
WORKDIR /app/

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8002", "fastapi_app.app:app"]