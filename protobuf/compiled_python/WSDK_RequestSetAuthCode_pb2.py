# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WSDK_RequestSetAuthCode.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WSDK_RequestSetAuthCode.proto',
  package='wsdk_commands',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x1dWSDK_RequestSetAuthCode.proto\x12\rwsdk_commands\",\n\x17WSDK_RequestSetAuthCode\x12\x11\n\tauth_code\x18\x01 \x02(\t'
)




_WSDK_REQUESTSETAUTHCODE = _descriptor.Descriptor(
  name='WSDK_RequestSetAuthCode',
  full_name='wsdk_commands.WSDK_RequestSetAuthCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_code', full_name='wsdk_commands.WSDK_RequestSetAuthCode.auth_code', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['WSDK_RequestSetAuthCode'] = _WSDK_REQUESTSETAUTHCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WSDK_RequestSetAuthCode = _reflection.GeneratedProtocolMessageType('WSDK_RequestSetAuthCode', (_message.Message,), {
  'DESCRIPTOR' : _WSDK_REQUESTSETAUTHCODE,
  '__module__' : 'WSDK_RequestSetAuthCode_pb2'
  # @@protoc_insertion_point(class_scope:wsdk_commands.WSDK_RequestSetAuthCode)
  })
_sym_db.RegisterMessage(WSDK_RequestSetAuthCode)


# @@protoc_insertion_point(module_scope)
