# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WSDK_RequestSetTimeWarpSpeed1X.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WSDK_RequestSetTimeWarpSpeed1X.proto',
  package='wsdk_commands',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n$WSDK_RequestSetTimeWarpSpeed1X.proto\x12\rwsdk_commands\",\n\x1eWSDK_RequestSetTimeWarpSpeed1X\x12\n\n\x02on\x18\x01 \x02(\x08'
)




_WSDK_REQUESTSETTIMEWARPSPEED1X = _descriptor.Descriptor(
  name='WSDK_RequestSetTimeWarpSpeed1X',
  full_name='wsdk_commands.WSDK_RequestSetTimeWarpSpeed1X',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='on', full_name='wsdk_commands.WSDK_RequestSetTimeWarpSpeed1X.on', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=55,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['WSDK_RequestSetTimeWarpSpeed1X'] = _WSDK_REQUESTSETTIMEWARPSPEED1X
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WSDK_RequestSetTimeWarpSpeed1X = _reflection.GeneratedProtocolMessageType('WSDK_RequestSetTimeWarpSpeed1X', (_message.Message,), {
  'DESCRIPTOR' : _WSDK_REQUESTSETTIMEWARPSPEED1X,
  '__module__' : 'WSDK_RequestSetTimeWarpSpeed1X_pb2'
  # @@protoc_insertion_point(class_scope:wsdk_commands.WSDK_RequestSetTimeWarpSpeed1X)
  })
_sym_db.RegisterMessage(WSDK_RequestSetTimeWarpSpeed1X)


# @@protoc_insertion_point(module_scope)
