import os
import grpc
from genproto import db_pb2
from genproto import db_pb2_grpc

url = os.environ.get('DB_SERVER_SERVICE_ADDR', 'db_server:8001')

with grpc.insecure_channel(url) as channel:
    stub = db_pb2_grpc.DBServiceStub(channel)

    # insert Asset
    newAsset = {
        'asset_id': '9',
        'asset_class': '3100',
        'description': 'this is a new asset',
        'picture': '/root/',
        'company_code': 'A001',
        'asset_number': '9001',
        'asset_subno': '0',
        'cost_center': 'CC_A001',
        'acquisition_date': {'year': 2019, 'month': 8, 'day': 31},
        'amount': 1000.10,
        'ul_year': 10,
        'ul_period': 12,
        'user_id': 'i333463'
    }
    newAssetRequest = db_pb2.NewAssetRequest(asset=newAsset)
    newAssetResponse = stub.insertAsset(newAssetRequest)

    # select all assets
    assets = stub.selectAssetAll(db_pb2.ListAssetsRequest(user_id='i333463'))


    for asset in assets.asset:
        # select asset by ID
        a = stub.selectAssetById(db_pb2.AssetId(asset_id=asset.asset_id))

print(str(newAssetResponse))

print(str(len(assets.asset)))
for asset in assets.asset:
  print(str(asset))

print(str(a))
