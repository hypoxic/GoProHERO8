# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WSDK_RequestSetAssociationState.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wsdkCommands import WSDK_EnumAssociationState_pb2 as wsdkCommands_dot_WSDK__EnumAssociationState__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WSDK_RequestSetAssociationState.proto',
  package='wsdk_commands',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n%WSDK_RequestSetAssociationState.proto\x12\rwsdk_commands\x1a,wsdkCommands/WSDK_EnumAssociationState.proto\"}\n\x1fWSDK_RequestSetAssociationState\x12\x15\n\rgopro_user_id\x18\x01 \x01(\t\x12\x43\n\x11\x61ssociation_state\x18\x02 \x01(\x0e\x32(.wsdk_commands.WSDK_EnumAssociationState'
  ,
  dependencies=[wsdkCommands_dot_WSDK__EnumAssociationState__pb2.DESCRIPTOR,])




_WSDK_REQUESTSETASSOCIATIONSTATE = _descriptor.Descriptor(
  name='WSDK_RequestSetAssociationState',
  full_name='wsdk_commands.WSDK_RequestSetAssociationState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gopro_user_id', full_name='wsdk_commands.WSDK_RequestSetAssociationState.gopro_user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='association_state', full_name='wsdk_commands.WSDK_RequestSetAssociationState.association_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=227,
)

_WSDK_REQUESTSETASSOCIATIONSTATE.fields_by_name['association_state'].enum_type = wsdkCommands_dot_WSDK__EnumAssociationState__pb2._WSDK_ENUMASSOCIATIONSTATE
DESCRIPTOR.message_types_by_name['WSDK_RequestSetAssociationState'] = _WSDK_REQUESTSETASSOCIATIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WSDK_RequestSetAssociationState = _reflection.GeneratedProtocolMessageType('WSDK_RequestSetAssociationState', (_message.Message,), {
  'DESCRIPTOR' : _WSDK_REQUESTSETASSOCIATIONSTATE,
  '__module__' : 'WSDK_RequestSetAssociationState_pb2'
  # @@protoc_insertion_point(class_scope:wsdk_commands.WSDK_RequestSetAssociationState)
  })
_sym_db.RegisterMessage(WSDK_RequestSetAssociationState)


# @@protoc_insertion_point(module_scope)
