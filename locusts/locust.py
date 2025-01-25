# import gevent
from locust import HttpUser, User, between, constant, events, tag, task

from grpc_app import embedding_pb2, embedding_pb2_grpc

# from grpc_server import run
from locusts.grpc_client import GrpcUser

HOST = "http://localhost:8002"


class User_1(HttpUser):
    host = "http://localhost:8082"
    user_id = 1
    # wait_time = constant(0.5)

    @tag("http")
    @task
    def embedding_http_test(self):
        params = {
            "email": "string",
            "nickname": "string",
            "favorite": "string",
            "lat": 0,
            "lng": 0,
            "size": 2048,
            "dtype": "float16",
        }
        with self.client.post(
            f"/v1/embedding/user/{self.user_id}",
            name="embedding http rate limit test",
            catch_response=True,
            json=params,
        ) as response:
            # print(response)
            data = response.json()
            assert response.status_code == 200


class User_2(HttpUser):
    host = "http://localhost:8083"
    user_id = 2
    # wait_time = constant(0.5)

    @tag("octet")
    @task
    def embedding_http_octet_test(self):
        params = {
            "email": "string",
            "nickname": "string",
            "favorite": "string",
            "lat": 0,
            "lng": 0,
            "size": 2048,
            "dtype": "float16",
        }
        with self.client.post(
            f"/v1/embedding/user/{self.user_id}/octet",
            name="embedding http-octet rate limit test",
            catch_response=True,
            json=params,
        ) as response:
            # print(response)
            data = response.content
            assert response.status_code == 200


class User_3(GrpcUser):
    host = "localhost:8004"
    stub_class = embedding_pb2_grpc.EmbeddingServiceStub
    # wait_time = constant(0.5)

    @tag("grpc")
    @task
    def embedding_grpc(self):
        params = {
            "email": "string",
            "nickname": "string",
            "favorite": "string",
            "lat": 0,
            "lng": 0,
            "size": 2048,
            "dtype": "float16",
        }
        response = self.stub.EmbeddingUser(embedding_pb2.EmbeddingUserRequest(**params))
