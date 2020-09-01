# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wsdkCommands/WSDK_EnumDeviceMgrState.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wsdkCommands/WSDK_EnumDeviceMgrState.proto',
  package='wsdk_commands',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n*wsdkCommands/WSDK_EnumDeviceMgrState.proto\x12\rwsdk_commands*\xff\x01\n\x17WSDK_EnumDeviceMgrState\x12\"\n\x1eWSDK_DEVICE_MGR_STATE_INACTIVE\x10\x00\x12&\n\"WSDK_DEVICE_MGR_STATE_PROVISIONING\x10\x01\x12%\n!WSDK_DEVICE_MGR_STATE_AUTHORIZING\x10\x02\x12$\n WSDK_DEVICE_MGR_STATE_AUTHORIZED\x10\x03\x12(\n$WSDK_DEVICE_MGR_STATE_SETUP_COMPLETE\x10\x04\x12!\n\x1dWSDK_DEVICE_MGR_STATE_CSI_ERR\x10\x7f*\xbf\x01\n\x15WSDK_EnumDeviceMgrCat\x12\x19\n\x15WSDK_DEVICE_MGR_CAT_0\x10\x00\x12\x19\n\x15WSDK_DEVICE_MGR_CAT_1\x10\x01\x12\x19\n\x15WSDK_DEVICE_MGR_CAT_2\x10\x02\x12\x19\n\x15WSDK_DEVICE_MGR_CAT_3\x10\x03\x12\x19\n\x15WSDK_DEVICE_MGR_CAT_4\x10\x04\x12\x1f\n\x1bWSDK_DEVICE_MGR_CAT_CSI_ERR\x10\x7f*\xbf\x01\n\x15WSDK_EnumDeviceMgrSub\x12\x19\n\x15WSDK_DEVICE_MGR_SUB_0\x10\x00\x12\x19\n\x15WSDK_DEVICE_MGR_SUB_1\x10\x01\x12\x19\n\x15WSDK_DEVICE_MGR_SUB_2\x10\x02\x12\x19\n\x15WSDK_DEVICE_MGR_SUB_3\x10\x03\x12\x19\n\x15WSDK_DEVICE_MGR_SUB_4\x10\x04\x12\x1f\n\x1bWSDK_DEVICE_MGR_SUB_CSI_ERR\x10\x7f*\xbf\x01\n\x15WSDK_EnumDeviceMgrErr\x12\x19\n\x15WSDK_DEVICE_MGR_ERR_0\x10\x00\x12\x19\n\x15WSDK_DEVICE_MGR_ERR_1\x10\x01\x12\x19\n\x15WSDK_DEVICE_MGR_ERR_2\x10\x02\x12\x19\n\x15WSDK_DEVICE_MGR_ERR_3\x10\x03\x12\x19\n\x15WSDK_DEVICE_MGR_ERR_4\x10\x04\x12\x1f\n\x1bWSDK_DEVICE_MGR_ERR_CSI_ERR\x10\x7f'
)

_WSDK_ENUMDEVICEMGRSTATE = _descriptor.EnumDescriptor(
  name='WSDK_EnumDeviceMgrState',
  full_name='wsdk_commands.WSDK_EnumDeviceMgrState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_STATE_INACTIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_STATE_PROVISIONING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_STATE_AUTHORIZING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_STATE_AUTHORIZED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_STATE_SETUP_COMPLETE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_STATE_CSI_ERR', index=5, number=127,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=62,
  serialized_end=317,
)
_sym_db.RegisterEnumDescriptor(_WSDK_ENUMDEVICEMGRSTATE)

WSDK_EnumDeviceMgrState = enum_type_wrapper.EnumTypeWrapper(_WSDK_ENUMDEVICEMGRSTATE)
_WSDK_ENUMDEVICEMGRCAT = _descriptor.EnumDescriptor(
  name='WSDK_EnumDeviceMgrCat',
  full_name='wsdk_commands.WSDK_EnumDeviceMgrCat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_CAT_0', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_CAT_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_CAT_2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_CAT_3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_CAT_4', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_CAT_CSI_ERR', index=5, number=127,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=320,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_WSDK_ENUMDEVICEMGRCAT)

WSDK_EnumDeviceMgrCat = enum_type_wrapper.EnumTypeWrapper(_WSDK_ENUMDEVICEMGRCAT)
_WSDK_ENUMDEVICEMGRSUB = _descriptor.EnumDescriptor(
  name='WSDK_EnumDeviceMgrSub',
  full_name='wsdk_commands.WSDK_EnumDeviceMgrSub',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_SUB_0', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_SUB_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_SUB_2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_SUB_3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_SUB_4', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_SUB_CSI_ERR', index=5, number=127,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=514,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_WSDK_ENUMDEVICEMGRSUB)

WSDK_EnumDeviceMgrSub = enum_type_wrapper.EnumTypeWrapper(_WSDK_ENUMDEVICEMGRSUB)
_WSDK_ENUMDEVICEMGRERR = _descriptor.EnumDescriptor(
  name='WSDK_EnumDeviceMgrErr',
  full_name='wsdk_commands.WSDK_EnumDeviceMgrErr',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_ERR_0', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_ERR_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_ERR_2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_ERR_3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_ERR_4', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WSDK_DEVICE_MGR_ERR_CSI_ERR', index=5, number=127,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=708,
  serialized_end=899,
)
_sym_db.RegisterEnumDescriptor(_WSDK_ENUMDEVICEMGRERR)

WSDK_EnumDeviceMgrErr = enum_type_wrapper.EnumTypeWrapper(_WSDK_ENUMDEVICEMGRERR)
WSDK_DEVICE_MGR_STATE_INACTIVE = 0
WSDK_DEVICE_MGR_STATE_PROVISIONING = 1
WSDK_DEVICE_MGR_STATE_AUTHORIZING = 2
WSDK_DEVICE_MGR_STATE_AUTHORIZED = 3
WSDK_DEVICE_MGR_STATE_SETUP_COMPLETE = 4
WSDK_DEVICE_MGR_STATE_CSI_ERR = 127
WSDK_DEVICE_MGR_CAT_0 = 0
WSDK_DEVICE_MGR_CAT_1 = 1
WSDK_DEVICE_MGR_CAT_2 = 2
WSDK_DEVICE_MGR_CAT_3 = 3
WSDK_DEVICE_MGR_CAT_4 = 4
WSDK_DEVICE_MGR_CAT_CSI_ERR = 127
WSDK_DEVICE_MGR_SUB_0 = 0
WSDK_DEVICE_MGR_SUB_1 = 1
WSDK_DEVICE_MGR_SUB_2 = 2
WSDK_DEVICE_MGR_SUB_3 = 3
WSDK_DEVICE_MGR_SUB_4 = 4
WSDK_DEVICE_MGR_SUB_CSI_ERR = 127
WSDK_DEVICE_MGR_ERR_0 = 0
WSDK_DEVICE_MGR_ERR_1 = 1
WSDK_DEVICE_MGR_ERR_2 = 2
WSDK_DEVICE_MGR_ERR_3 = 3
WSDK_DEVICE_MGR_ERR_4 = 4
WSDK_DEVICE_MGR_ERR_CSI_ERR = 127


DESCRIPTOR.enum_types_by_name['WSDK_EnumDeviceMgrState'] = _WSDK_ENUMDEVICEMGRSTATE
DESCRIPTOR.enum_types_by_name['WSDK_EnumDeviceMgrCat'] = _WSDK_ENUMDEVICEMGRCAT
DESCRIPTOR.enum_types_by_name['WSDK_EnumDeviceMgrSub'] = _WSDK_ENUMDEVICEMGRSUB
DESCRIPTOR.enum_types_by_name['WSDK_EnumDeviceMgrErr'] = _WSDK_ENUMDEVICEMGRERR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)