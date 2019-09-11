from concurrent import futures
import logging
import time
import os
import grpc

from genproto import account_pb2
from genproto import account_pb2_grpc
from genproto import db_pb2
from genproto import db_pb2_grpc
# from grpc_health.v1 import health_pb2
# from grpc_health.v1 import health_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AccountService(account_pb2_grpc.AccountServiceServicer):
    def register(self, request, context):

        response = account_pb2.RegisterResponse()
        response.user_id = request.user_id
        response.user_name = request.user_name
        # conn = db.get_connection()
        # user_name = db.select_user_by_user_id(conn, request.user_id)
        #
        # if user_name == '':
        #     db.create_user(db.get_connection(), request.user_id, request.user_name, request.password)


        return response

    def login(self, request, context):
        print('a user request to login')
        response = account_pb2.LoginResponse()
        # response.user_name = 'myNameIsEric'
        url = os.environ.get('DB_SERVER_SERVICE_ADDR')
        if url is None:
            if request.user_id == 'i333463' and request.password == '123456':
              response.user_name = 'Eric Wu'
            else:
                response.user_name = ''
        else:
          with grpc.insecure_channel(url) as channel:
            stub = db_pb2_grpc.DBServiceStub(channel)
            response_db = stub.login_db(db_pb2.LoginRequest_db(user_id_db=request.user_id, password_db=request.password))
            response.user_name = response_db.user_name_db
        return response

    # def Check(self, request, context):
    #     return health_pb2.HealthCheckResponse(
    #         status=health_pb2.HealthCheckResponse.SERVING)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_pb2_grpc.add_AccountServiceServicer_to_server(AccountService(), server)
    # health_pb2_grpc.add_HealthServicer_to_server(AccountService(), server)
    port = os.environ.get('PORT', "50050")

    # start server
    server.add_insecure_port('[::]:'+port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()