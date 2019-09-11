import db as db
from concurrent import futures
import logging
import time
import os
import grpc

from genproto import db_pb2
from genproto import db_pb2_grpc
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DBService(db_pb2_grpc.DBServiceServicer):
    def register_db(self, request, context):

        response = db_pb2.RegisterResponse_db()
        response.user_id_db = request.user_id_db
        response.user_name_db = request.user_name_db
        return response

    def login_db(self, request, context):
        print('start connect to DB')
        url = os.environ.get('DB_ADDR')
        conn = db.get_connection(url)
        response = db_pb2.LoginResponse_db()
        response.user_name_db = db.select_user_by_user_id(conn, id=request.user_id_db, password=request.password_db)
        return response

    def updatelog_db(self, request, context):
        print('a user request to login')
        response = db_pb2.db_log_db()
        response.user_name_db = 'myNameIsEric'
        return response

    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_DBServiceServicer_to_server(DBService(), server)
    health_pb2_grpc.add_HealthServicer_to_server(AccountService(), server)
    port = os.environ.get('PORT', '8001')

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