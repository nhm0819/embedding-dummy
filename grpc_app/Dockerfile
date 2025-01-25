FROM python:3.11-slim

COPY ./grpc_app/requirements.txt /app/requirements.txt
#RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./grpc_app/ /app/grpc_app/
COPY ./grpc_server.py /app/grpc_server.py
WORKDIR /app/

CMD ["python", "grpc_server.py"]