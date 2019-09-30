# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='db.proto',
  package='demojam2019',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x08\x64\x62.proto\x12\x0b\x64\x65mojam2019\"p\n\x12RegisterRequest_db\x12\x12\n\nuser_id_db\x18\x01 \x01(\t\x12\x14\n\x0cuser_name_db\x18\x02 \x01(\t\x12\x13\n\x0bpassword_db\x18\x03 \x01(\t\x12\x1b\n\x13password_confirm_db\x18\x04 \x01(\t\"?\n\x13RegisterResponse_db\x12\x12\n\nuser_id_db\x18\x01 \x01(\t\x12\x14\n\x0cuser_name_db\x18\x02 \x01(\t\":\n\x0fLoginRequest_db\x12\x12\n\nuser_id_db\x18\x01 \x01(\t\x12\x13\n\x0bpassword_db\x18\x02 \x01(\t\"(\n\x10LoginResponse_db\x12\x14\n\x0cuser_name_db\x18\x01 \x01(\t\"\x1d\n\napi_log_db\x12\x0f\n\x07text_db\x18\x01 \x01(\t\"\x1c\n\tdb_log_db\x12\x0f\n\x07text_db\x18\x01 \x01(\t\"\x1b\n\x07\x41ssetId\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\"\xec\x02\n\x05\x41sset\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61sset_class\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12\x14\n\x0c\x63ompany_code\x18\x05 \x01(\t\x12\x14\n\x0c\x61sset_number\x18\x06 \x01(\t\x12\x13\n\x0b\x61sset_subno\x18\x07 \x01(\t\x12\x13\n\x0b\x63ost_center\x18\x08 \x01(\t\x12+\n\x10\x61\x63quisition_date\x18\t \x01(\x0b\x32\x11.demojam2019.Date\x12\x0e\n\x06\x61mount\x18\n \x01(\x01\x12\x0f\n\x07ul_year\x18\x0b \x01(\x05\x12\x11\n\tul_period\x18\x0c \x01(\x05\x12\x0f\n\x07user_id\x18\r \x01(\t\x12&\n\x0b\x63reate_date\x18\x0e \x01(\x0b\x32\x11.demojam2019.Date\x12&\n\x0b\x63reate_time\x18\x0f \x01(\x0b\x32\x11.demojam2019.Time\"$\n\x11ListAssetsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"7\n\x12ListAssetsResponse\x12!\n\x05\x61sset\x18\x01 \x03(\x0b\x32\x12.demojam2019.Asset\"4\n\x0fNewAssetRequest\x12!\n\x05\x61sset\x18\x01 \x01(\x0b\x32\x12.demojam2019.Asset\"@\n\x10NewAssetResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\t\x12\x0b\n\x03log\x18\x03 \x01(\t\"0\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\"4\n\x04Time\x12\x0c\n\x04hour\x18\x01 \x01(\x05\x12\x0e\n\x06minute\x18\x02 \x01(\x05\x12\x0e\n\x06second\x18\x03 \x01(\x05\x32\xcc\x03\n\tDBService\x12R\n\x0bregister_db\x12\x1f.demojam2019.RegisterRequest_db\x1a .demojam2019.RegisterResponse_db\"\x00\x12I\n\x08login_db\x12\x1c.demojam2019.LoginRequest_db\x1a\x1d.demojam2019.LoginResponse_db\"\x00\x12>\n\taddlog_db\x12\x17.demojam2019.api_log_db\x1a\x16.demojam2019.db_log_db\"\x00\x12=\n\x0fselectAssetById\x12\x14.demojam2019.AssetId\x1a\x12.demojam2019.Asset\"\x00\x12S\n\x0eselectAssetAll\x12\x1e.demojam2019.ListAssetsRequest\x1a\x1f.demojam2019.ListAssetsResponse\"\x00\x12L\n\x0binsertAsset\x12\x1c.demojam2019.NewAssetRequest\x1a\x1d.demojam2019.NewAssetResponse\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_REGISTERREQUEST_DB = _descriptor.Descriptor(
  name='RegisterRequest_db',
  full_name='demojam2019.RegisterRequest_db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id_db', full_name='demojam2019.RegisterRequest_db.user_id_db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name_db', full_name='demojam2019.RegisterRequest_db.user_name_db', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password_db', full_name='demojam2019.RegisterRequest_db.password_db', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password_confirm_db', full_name='demojam2019.RegisterRequest_db.password_confirm_db', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=137,
)


_REGISTERRESPONSE_DB = _descriptor.Descriptor(
  name='RegisterResponse_db',
  full_name='demojam2019.RegisterResponse_db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id_db', full_name='demojam2019.RegisterResponse_db.user_id_db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name_db', full_name='demojam2019.RegisterResponse_db.user_name_db', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=202,
)


_LOGINREQUEST_DB = _descriptor.Descriptor(
  name='LoginRequest_db',
  full_name='demojam2019.LoginRequest_db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id_db', full_name='demojam2019.LoginRequest_db.user_id_db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password_db', full_name='demojam2019.LoginRequest_db.password_db', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=262,
)


_LOGINRESPONSE_DB = _descriptor.Descriptor(
  name='LoginResponse_db',
  full_name='demojam2019.LoginResponse_db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name_db', full_name='demojam2019.LoginResponse_db.user_name_db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=304,
)


_API_LOG_DB = _descriptor.Descriptor(
  name='api_log_db',
  full_name='demojam2019.api_log_db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_db', full_name='demojam2019.api_log_db.text_db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=335,
)


_DB_LOG_DB = _descriptor.Descriptor(
  name='db_log_db',
  full_name='demojam2019.db_log_db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_db', full_name='demojam2019.db_log_db.text_db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=365,
)


_ASSETID = _descriptor.Descriptor(
  name='AssetId',
  full_name='demojam2019.AssetId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='demojam2019.AssetId.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=394,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='demojam2019.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='demojam2019.Asset.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_class', full_name='demojam2019.Asset.asset_class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='demojam2019.Asset.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='picture', full_name='demojam2019.Asset.picture', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='company_code', full_name='demojam2019.Asset.company_code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_number', full_name='demojam2019.Asset.asset_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_subno', full_name='demojam2019.Asset.asset_subno', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_center', full_name='demojam2019.Asset.cost_center', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acquisition_date', full_name='demojam2019.Asset.acquisition_date', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='demojam2019.Asset.amount', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ul_year', full_name='demojam2019.Asset.ul_year', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ul_period', full_name='demojam2019.Asset.ul_period', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='demojam2019.Asset.user_id', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_date', full_name='demojam2019.Asset.create_date', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='demojam2019.Asset.create_time', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=761,
)


_LISTASSETSREQUEST = _descriptor.Descriptor(
  name='ListAssetsRequest',
  full_name='demojam2019.ListAssetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='demojam2019.ListAssetsRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=799,
)


_LISTASSETSRESPONSE = _descriptor.Descriptor(
  name='ListAssetsResponse',
  full_name='demojam2019.ListAssetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset', full_name='demojam2019.ListAssetsResponse.asset', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=856,
)


_NEWASSETREQUEST = _descriptor.Descriptor(
  name='NewAssetRequest',
  full_name='demojam2019.NewAssetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset', full_name='demojam2019.NewAssetRequest.asset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=910,
)


_NEWASSETRESPONSE = _descriptor.Descriptor(
  name='NewAssetResponse',
  full_name='demojam2019.NewAssetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='demojam2019.NewAssetResponse.error', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='demojam2019.NewAssetResponse.asset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='demojam2019.NewAssetResponse.log', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=976,
)


_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='demojam2019.Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='demojam2019.Date.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='demojam2019.Date.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='demojam2019.Date.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=978,
  serialized_end=1026,
)


_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='demojam2019.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hour', full_name='demojam2019.Time.hour', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='demojam2019.Time.minute', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='demojam2019.Time.second', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1028,
  serialized_end=1080,
)

_ASSET.fields_by_name['acquisition_date'].message_type = _DATE
_ASSET.fields_by_name['create_date'].message_type = _DATE
_ASSET.fields_by_name['create_time'].message_type = _TIME
_LISTASSETSRESPONSE.fields_by_name['asset'].message_type = _ASSET
_NEWASSETREQUEST.fields_by_name['asset'].message_type = _ASSET
DESCRIPTOR.message_types_by_name['RegisterRequest_db'] = _REGISTERREQUEST_DB
DESCRIPTOR.message_types_by_name['RegisterResponse_db'] = _REGISTERRESPONSE_DB
DESCRIPTOR.message_types_by_name['LoginRequest_db'] = _LOGINREQUEST_DB
DESCRIPTOR.message_types_by_name['LoginResponse_db'] = _LOGINRESPONSE_DB
DESCRIPTOR.message_types_by_name['api_log_db'] = _API_LOG_DB
DESCRIPTOR.message_types_by_name['db_log_db'] = _DB_LOG_DB
DESCRIPTOR.message_types_by_name['AssetId'] = _ASSETID
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['ListAssetsRequest'] = _LISTASSETSREQUEST
DESCRIPTOR.message_types_by_name['ListAssetsResponse'] = _LISTASSETSRESPONSE
DESCRIPTOR.message_types_by_name['NewAssetRequest'] = _NEWASSETREQUEST
DESCRIPTOR.message_types_by_name['NewAssetResponse'] = _NEWASSETRESPONSE
DESCRIPTOR.message_types_by_name['Date'] = _DATE
DESCRIPTOR.message_types_by_name['Time'] = _TIME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterRequest_db = _reflection.GeneratedProtocolMessageType('RegisterRequest_db', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST_DB,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.RegisterRequest_db)
  })
_sym_db.RegisterMessage(RegisterRequest_db)

RegisterResponse_db = _reflection.GeneratedProtocolMessageType('RegisterResponse_db', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE_DB,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.RegisterResponse_db)
  })
_sym_db.RegisterMessage(RegisterResponse_db)

LoginRequest_db = _reflection.GeneratedProtocolMessageType('LoginRequest_db', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST_DB,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.LoginRequest_db)
  })
_sym_db.RegisterMessage(LoginRequest_db)

LoginResponse_db = _reflection.GeneratedProtocolMessageType('LoginResponse_db', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE_DB,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.LoginResponse_db)
  })
_sym_db.RegisterMessage(LoginResponse_db)

api_log_db = _reflection.GeneratedProtocolMessageType('api_log_db', (_message.Message,), {
  'DESCRIPTOR' : _API_LOG_DB,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.api_log_db)
  })
_sym_db.RegisterMessage(api_log_db)

db_log_db = _reflection.GeneratedProtocolMessageType('db_log_db', (_message.Message,), {
  'DESCRIPTOR' : _DB_LOG_DB,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.db_log_db)
  })
_sym_db.RegisterMessage(db_log_db)

AssetId = _reflection.GeneratedProtocolMessageType('AssetId', (_message.Message,), {
  'DESCRIPTOR' : _ASSETID,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.AssetId)
  })
_sym_db.RegisterMessage(AssetId)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.Asset)
  })
_sym_db.RegisterMessage(Asset)

ListAssetsRequest = _reflection.GeneratedProtocolMessageType('ListAssetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTASSETSREQUEST,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.ListAssetsRequest)
  })
_sym_db.RegisterMessage(ListAssetsRequest)

ListAssetsResponse = _reflection.GeneratedProtocolMessageType('ListAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTASSETSRESPONSE,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.ListAssetsResponse)
  })
_sym_db.RegisterMessage(ListAssetsResponse)

NewAssetRequest = _reflection.GeneratedProtocolMessageType('NewAssetRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWASSETREQUEST,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.NewAssetRequest)
  })
_sym_db.RegisterMessage(NewAssetRequest)

NewAssetResponse = _reflection.GeneratedProtocolMessageType('NewAssetResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWASSETRESPONSE,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.NewAssetResponse)
  })
_sym_db.RegisterMessage(NewAssetResponse)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.Date)
  })
_sym_db.RegisterMessage(Date)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
  'DESCRIPTOR' : _TIME,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:demojam2019.Time)
  })
_sym_db.RegisterMessage(Time)


DESCRIPTOR._options = None

_DBSERVICE = _descriptor.ServiceDescriptor(
  name='DBService',
  full_name='demojam2019.DBService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1083,
  serialized_end=1543,
  methods=[
  _descriptor.MethodDescriptor(
    name='register_db',
    full_name='demojam2019.DBService.register_db',
    index=0,
    containing_service=None,
    input_type=_REGISTERREQUEST_DB,
    output_type=_REGISTERRESPONSE_DB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='login_db',
    full_name='demojam2019.DBService.login_db',
    index=1,
    containing_service=None,
    input_type=_LOGINREQUEST_DB,
    output_type=_LOGINRESPONSE_DB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='addlog_db',
    full_name='demojam2019.DBService.addlog_db',
    index=2,
    containing_service=None,
    input_type=_API_LOG_DB,
    output_type=_DB_LOG_DB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='selectAssetById',
    full_name='demojam2019.DBService.selectAssetById',
    index=3,
    containing_service=None,
    input_type=_ASSETID,
    output_type=_ASSET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='selectAssetAll',
    full_name='demojam2019.DBService.selectAssetAll',
    index=4,
    containing_service=None,
    input_type=_LISTASSETSREQUEST,
    output_type=_LISTASSETSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='insertAsset',
    full_name='demojam2019.DBService.insertAsset',
    index=5,
    containing_service=None,
    input_type=_NEWASSETREQUEST,
    output_type=_NEWASSETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DBSERVICE)

DESCRIPTOR.services_by_name['DBService'] = _DBSERVICE

# @@protoc_insertion_point(module_scope)
