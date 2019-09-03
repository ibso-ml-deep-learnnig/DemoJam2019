# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import createAsset_pb2 as createAsset__pb2


class CRUDStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create = channel.unary_unary(
        '/asset.CRUD/create',
        request_serializer=createAsset__pb2.asset.SerializeToString,
        response_deserializer=createAsset__pb2.log.FromString,
        )


class CRUDServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CRUDServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create': grpc.unary_unary_rpc_method_handler(
          servicer.create,
          request_deserializer=createAsset__pb2.asset.FromString,
          response_serializer=createAsset__pb2.log.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'asset.CRUD', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class DBStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.update = channel.unary_unary(
        '/asset.DB/update',
        request_serializer=createAsset__pb2.api_log.SerializeToString,
        response_deserializer=createAsset__pb2.db_log.FromString,
        )


class DBServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=createAsset__pb2.api_log.FromString,
          response_serializer=createAsset__pb2.db_log.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'asset.DB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
