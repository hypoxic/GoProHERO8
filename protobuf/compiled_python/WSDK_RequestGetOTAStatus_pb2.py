# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WSDK_RequestGetOTAStatus.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wsdkCommands import WSDK_EnumRegisterOTAStatus_pb2 as wsdkCommands_dot_WSDK__EnumRegisterOTAStatus__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WSDK_RequestGetOTAStatus.proto',
  package='wsdk_commands',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x1eWSDK_RequestGetOTAStatus.proto\x12\rwsdk_commands\x1a-wsdkCommands/WSDK_EnumRegisterOTAStatus.proto\"\xac\x01\n\x18WSDK_RequestGetOTAStatus\x12\x46\n\x13register_ota_status\x18\x01 \x03(\x0e\x32).wsdk_commands.WSDK_EnumRegisterOTAStatus\x12H\n\x15unregister_ota_status\x18\x02 \x03(\x0e\x32).wsdk_commands.WSDK_EnumRegisterOTAStatus'
  ,
  dependencies=[wsdkCommands_dot_WSDK__EnumRegisterOTAStatus__pb2.DESCRIPTOR,])




_WSDK_REQUESTGETOTASTATUS = _descriptor.Descriptor(
  name='WSDK_RequestGetOTAStatus',
  full_name='wsdk_commands.WSDK_RequestGetOTAStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='register_ota_status', full_name='wsdk_commands.WSDK_RequestGetOTAStatus.register_ota_status', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unregister_ota_status', full_name='wsdk_commands.WSDK_RequestGetOTAStatus.unregister_ota_status', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=269,
)

_WSDK_REQUESTGETOTASTATUS.fields_by_name['register_ota_status'].enum_type = wsdkCommands_dot_WSDK__EnumRegisterOTAStatus__pb2._WSDK_ENUMREGISTEROTASTATUS
_WSDK_REQUESTGETOTASTATUS.fields_by_name['unregister_ota_status'].enum_type = wsdkCommands_dot_WSDK__EnumRegisterOTAStatus__pb2._WSDK_ENUMREGISTEROTASTATUS
DESCRIPTOR.message_types_by_name['WSDK_RequestGetOTAStatus'] = _WSDK_REQUESTGETOTASTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WSDK_RequestGetOTAStatus = _reflection.GeneratedProtocolMessageType('WSDK_RequestGetOTAStatus', (_message.Message,), {
  'DESCRIPTOR' : _WSDK_REQUESTGETOTASTATUS,
  '__module__' : 'WSDK_RequestGetOTAStatus_pb2'
  # @@protoc_insertion_point(class_scope:wsdk_commands.WSDK_RequestGetOTAStatus)
  })
_sym_db.RegisterMessage(WSDK_RequestGetOTAStatus)


# @@protoc_insertion_point(module_scope)
