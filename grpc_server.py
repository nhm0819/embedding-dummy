import asyncio
import logging
import os
from concurrent import futures

import grpc
import numpy as np

from grpc_app import embedding_pb2, embedding_pb2_grpc
from grpc_app.enums import BigEndian

logger = logging.getLogger(__name__)


class EmbeddingService(embedding_pb2_grpc.EmbeddingServiceServicer):
    def EmbeddingUser(
        self,
        request: embedding_pb2.EmbeddingUserRequest,
        context: grpc.ServicerContext,
    ) -> embedding_pb2.EmbeddingUserResponse:
        # logger.info(request.__str__())
        bvector = (
            np.random.standard_normal((1, request.size))
            .astype(BigEndian[request.dtype].value)
            .tobytes()
        )
        return embedding_pb2.EmbeddingUserResponse(bvector=bvector)

    async def aEmbeddingUser(
        self,
        request: embedding_pb2.EmbeddingUserRequest,
        context: grpc.aio.ServicerContext,
    ) -> embedding_pb2.EmbeddingUserResponse:
        # return embedding_pb2.EmbeddingUserResponse(bvector=bvector)
        return self.EmbeddingUser(request=request, context=context)


async def async_serve():
    server = grpc.aio.server()
    embedding_pb2_grpc.add_EmbeddingServiceServicer_to_server(
        EmbeddingService(), server
    )
    server.add_insecure_port(f"[::]:{os.getenv('grpc_port', '8004')}")
    await server.start()
    logger.info(
        f"gRPC async server is running on port {os.getenv('grpc_port', '8004')}"
    )
    await server.wait_for_termination()


def async_run():
    asyncio.run(async_serve())


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    embedding_pb2_grpc.add_EmbeddingServiceServicer_to_server(
        EmbeddingService(), server
    )
    server.add_insecure_port(f"localhost:{os.getenv('grpc_port', '8004')}")
    server.start()
    logger.info(f"gRPC server is running on port {os.getenv('grpc_port', '8004')}")
    server.wait_for_termination()


if __name__ == "__main__":
    async_run()
    # run()
