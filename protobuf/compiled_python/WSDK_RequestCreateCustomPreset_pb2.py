# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WSDK_RequestCreateCustomPreset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wsdkCommands import WSDK_EnumPresetGroup_pb2 as wsdkCommands_dot_WSDK__EnumPresetGroup__pb2
from wsdkCommands import WSDK_EnumPresetIcon_pb2 as wsdkCommands_dot_WSDK__EnumPresetIcon__pb2
from wsdkCommands import WSDK_EnumPresetTitle_pb2 as wsdkCommands_dot_WSDK__EnumPresetTitle__pb2
from wsdkCommands import WSDK_EnumFlatMode_pb2 as wsdkCommands_dot_WSDK__EnumFlatMode__pb2
from generic import EnumResultGeneric_pb2 as generic_dot_EnumResultGeneric__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WSDK_RequestCreateCustomPreset.proto',
  package='wsdk_commands',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n$WSDK_RequestCreateCustomPreset.proto\x12\rwsdk_commands\x1a\'wsdkCommands/WSDK_EnumPresetGroup.proto\x1a&wsdkCommands/WSDK_EnumPresetIcon.proto\x1a\'wsdkCommands/WSDK_EnumPresetTitle.proto\x1a$wsdkCommands/WSDK_EnumFlatMode.proto\x1a\x1fgeneric/EnumResultGeneric.proto\"\x89\x02\n\x1eWSDK_RequestCreateCustomPreset\x12\x35\n\x08group_id\x18\x01 \x01(\x0e\x32#.wsdk_commands.WSDK_EnumPresetGroup\x12.\n\x04mode\x18\x02 \x01(\x0e\x32 .wsdk_commands.WSDK_EnumFlatMode\x12\x33\n\x07icon_id\x18\x03 \x01(\x0e\x32\".wsdk_commands.WSDK_EnumPresetIcon\x12\x35\n\x08title_id\x18\x04 \x01(\x0e\x32#.wsdk_commands.WSDK_EnumPresetTitle\x12\x14\n\x0ctitle_number\x18\x05 \x01(\x05\"f\n\x1fWSDK_ResponseCreateCustomPreset\x12\x11\n\tpreset_id\x18\x01 \x01(\x05\x12\x30\n\x06result\x18\x02 \x01(\x0e\x32 .wsdk_commands.EnumResultGeneric'
  ,
  dependencies=[wsdkCommands_dot_WSDK__EnumPresetGroup__pb2.DESCRIPTOR,wsdkCommands_dot_WSDK__EnumPresetIcon__pb2.DESCRIPTOR,wsdkCommands_dot_WSDK__EnumPresetTitle__pb2.DESCRIPTOR,wsdkCommands_dot_WSDK__EnumFlatMode__pb2.DESCRIPTOR,generic_dot_EnumResultGeneric__pb2.DESCRIPTOR,])




_WSDK_REQUESTCREATECUSTOMPRESET = _descriptor.Descriptor(
  name='WSDK_RequestCreateCustomPreset',
  full_name='wsdk_commands.WSDK_RequestCreateCustomPreset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='wsdk_commands.WSDK_RequestCreateCustomPreset.group_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='wsdk_commands.WSDK_RequestCreateCustomPreset.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_id', full_name='wsdk_commands.WSDK_RequestCreateCustomPreset.icon_id', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_id', full_name='wsdk_commands.WSDK_RequestCreateCustomPreset.title_id', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_number', full_name='wsdk_commands.WSDK_RequestCreateCustomPreset.title_number', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=249,
  serialized_end=514,
)


_WSDK_RESPONSECREATECUSTOMPRESET = _descriptor.Descriptor(
  name='WSDK_ResponseCreateCustomPreset',
  full_name='wsdk_commands.WSDK_ResponseCreateCustomPreset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preset_id', full_name='wsdk_commands.WSDK_ResponseCreateCustomPreset.preset_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='wsdk_commands.WSDK_ResponseCreateCustomPreset.result', index=1,
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
  serialized_start=516,
  serialized_end=618,
)

_WSDK_REQUESTCREATECUSTOMPRESET.fields_by_name['group_id'].enum_type = wsdkCommands_dot_WSDK__EnumPresetGroup__pb2._WSDK_ENUMPRESETGROUP
_WSDK_REQUESTCREATECUSTOMPRESET.fields_by_name['mode'].enum_type = wsdkCommands_dot_WSDK__EnumFlatMode__pb2._WSDK_ENUMFLATMODE
_WSDK_REQUESTCREATECUSTOMPRESET.fields_by_name['icon_id'].enum_type = wsdkCommands_dot_WSDK__EnumPresetIcon__pb2._WSDK_ENUMPRESETICON
_WSDK_REQUESTCREATECUSTOMPRESET.fields_by_name['title_id'].enum_type = wsdkCommands_dot_WSDK__EnumPresetTitle__pb2._WSDK_ENUMPRESETTITLE
_WSDK_RESPONSECREATECUSTOMPRESET.fields_by_name['result'].enum_type = generic_dot_EnumResultGeneric__pb2._ENUMRESULTGENERIC
DESCRIPTOR.message_types_by_name['WSDK_RequestCreateCustomPreset'] = _WSDK_REQUESTCREATECUSTOMPRESET
DESCRIPTOR.message_types_by_name['WSDK_ResponseCreateCustomPreset'] = _WSDK_RESPONSECREATECUSTOMPRESET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WSDK_RequestCreateCustomPreset = _reflection.GeneratedProtocolMessageType('WSDK_RequestCreateCustomPreset', (_message.Message,), {
  'DESCRIPTOR' : _WSDK_REQUESTCREATECUSTOMPRESET,
  '__module__' : 'WSDK_RequestCreateCustomPreset_pb2'
  # @@protoc_insertion_point(class_scope:wsdk_commands.WSDK_RequestCreateCustomPreset)
  })
_sym_db.RegisterMessage(WSDK_RequestCreateCustomPreset)

WSDK_ResponseCreateCustomPreset = _reflection.GeneratedProtocolMessageType('WSDK_ResponseCreateCustomPreset', (_message.Message,), {
  'DESCRIPTOR' : _WSDK_RESPONSECREATECUSTOMPRESET,
  '__module__' : 'WSDK_RequestCreateCustomPreset_pb2'
  # @@protoc_insertion_point(class_scope:wsdk_commands.WSDK_ResponseCreateCustomPreset)
  })
_sym_db.RegisterMessage(WSDK_ResponseCreateCustomPreset)


# @@protoc_insertion_point(module_scope)
