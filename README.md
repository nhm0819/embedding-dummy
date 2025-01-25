# FastAPI Boilerplate

### Install dependency

```shell
> poetry shell
> poetry install
```

### Run server

```shell
> python3 main.py # FastAPI
```

### Launch docker

```shell
IMAGE_NAME = embedding-dummy
TAG_NAME = v0.0
docker build -t ${IMAGE_NAME}:${TAG_NAME} -f fastapi_app/Dockerfile .
docker run -d -p 8002:8002 --name embedding-dummy ${IMAGE_NAME}:${TAG_NAME}
```

### Traffic Test

```shell
locust -f locust.py
```
