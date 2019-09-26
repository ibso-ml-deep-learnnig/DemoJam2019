from concurrent import futures
import logging
import time
import os
import grpc
import db as db
from mysql.connector import Error
from datetime import datetime, date
import uuid
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
        port = os.environ.get('DB_PORT')
        conn = db.get_connection(url, port)
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

    def selectAssetById(self, request, context):
        print('start select asset by id :' + request.asset_id)

        response = db_pb2.Asset()
        asset = []

        # Test Data
        # asset = ['1', '3100', 'this is asset', '/path/', 'A001', '6001', '0', 'cc', '20190831', 1000.1, 10, 12, 'i333463', '20190925', '153020']
        # fill_asset_response(response, asset)

        try:
            conn = None
            url = os.environ.get('DB_ADDR', 'localhost')
            port = os.environ.get('DB_PORT', '3306')

            conn = db.get_connection(url, port)
            asset = db.selectAssetById(conn, asset_id=request.asset_id)
            if asset == []:
                print("no asset data")
            else:
              fill_asset_response(response, asset[0])

        except Error as error:
            print("Failed to select asset from table {}".format(error))

        finally:
            if conn is None:
                print("No db connection")
            elif conn.is_connected():
                conn.close()

        return response


    def selectAssetAll(self, request, context):
        print('start select all assets by user_id :' + request.user_id)
        # url = os.environ.get('DB_ADDR')
        # port = os.environ.get('DB_PORT')
        # conn = db.get_connection(url, port)
        # assets = db.selectAssets(conn, asset_id=request.user_id)

        response = db_pb2.ListAssetsResponse()

        # Test Data
        # assets =  [['1', '3100', 'this is asset', '/path/', 'A001', '6001', '0', 'cc', '20190831', 1000.1, 10, 12, 'i333463', '20190925', '153020'],
        #            ['2', '3100', 'this is asset', '/path/', 'A001', '6001', '0', 'cc', '20190831', 1000.1, 10, 12, 'i333463', '20190925', '153020'],
        #            ['3', '3100', 'this is asset', '/path/', 'A001', '6001', '0', 'cc', '20190831', 1000.1, 10, 12, 'i333463', '20190925', '153020']]

        # for asset in assets:
        #     fill_asset_response(response.asset.add(), asset)

        try:

            conn = None
            url = os.environ.get('DB_ADDR', 'localhost')
            port = os.environ.get('DB_PORT', '3306')
            conn = db.get_connection(url, port)

            assets = db.selectAssets(conn, user_id=request.user_id)
            for asset in assets:
                fill_asset_response(response.asset.add(), asset)

        except Error as error:
            print("Failed to select assets from table {}".format(error))

        finally:
            if conn is None:
                print("No db connection")
            elif conn.is_connected():
                conn.close()

        return response

    def insertAsset(self, request, context):
        print('start insert an asset')

        response = db_pb2.NewAssetResponse()

#       Test Data
        # asset = fill_new_asset(request.asset)
        # print(str(asset))

        try:
            conn = None
            url = os.environ.get('DB_ADDR', 'localhost')
            port = os.environ.get('DB_PORT', '3306')
            conn = db.get_connection(url, port)

            response.error = db.insertAsset(conn, fill_new_asset(request.asset))

        except Error as error:
            response.error = True
            print("Failed to insert asset to table {}".format(error))

        finally:
            if conn is None:
                print("No db connection")
            elif conn.is_connected():
                conn.close()

        if response.error is False:
            response.log = 'New asset was created successfully!'
        else:
            response.log = 'Failed to insert asset to table'

        return response

def fill_asset_response(assetResponse, asset):

    # fill the asset Result to gRPC response
    assetResponse.asset_id = str(uuid.uuid1())
    assetResponse.asset_class = asset[1]
    assetResponse.description = asset[2]
    assetResponse.picture = asset[3]
    assetResponse.company_code = asset[4]
    assetResponse.asset_number = asset[5]
    assetResponse.asset_subno = asset[6]
    assetResponse.cost_center = asset[7]
    encode_date(assetResponse.acquisition_date, str(asset[8]))
    assetResponse.amount = asset[9]
    assetResponse.ul_year = asset[10]
    assetResponse.ul_period = asset[11]
    assetResponse.user_id = asset[12]
    encode_date(assetResponse.create_date, str(asset[13]))
    encode_time(assetResponse.create_time, str(asset[14]))

def fill_new_asset(newAssetRequest):

    # a tuple of asset to be inserted
    asset = [
         str(uuid.uuid1()),
         newAssetRequest.asset_class,
         newAssetRequest.description,
         newAssetRequest.picture,
         newAssetRequest.company_code,
         newAssetRequest.asset_number,
         newAssetRequest.asset_subno,
         newAssetRequest.cost_center,
         decode_date(newAssetRequest.acquisition_date),
         newAssetRequest.amount,
         newAssetRequest.ul_year,
         newAssetRequest.ul_period,
         newAssetRequest.user_id,
         datetime.now().strftime("%Y%m%d"),
         datetime.now().strftime("%H%M%S")
    ]

    return asset

def decode_date(dateRequest):
    return date(dateRequest.year, dateRequest.month, dateRequest.day).strftime("%Y%m%d")

def encode_date(dateResponse, date):
    dateResponse.year = int(date[:4])
    dateResponse.month = int(date[4:6])
    dateResponse.day = int(date[6:])

def encode_time(timeResponse, time):
    timeResponse.hour = int(time[:2])
    timeResponse.minute = int(time[2:4])
    timeResponse.second = int(time[4:])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_DBServiceServicer_to_server(DBService(), server)
    health_pb2_grpc.add_HealthServicer_to_server(DBService(), server)
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