# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: btc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='btc.proto',
  package='shiftcrypto.bitbox02',
  syntax='proto3',
  serialized_pb=_b('\n\tbtc.proto\x12\x14shiftcrypto.bitbox02\x1a\x0c\x63ommon.proto\"\xb5\x02\n\x0f\x42TCScriptConfig\x12G\n\x0bsimple_type\x18\x01 \x01(\x0e\x32\x30.shiftcrypto.bitbox02.BTCScriptConfig.SimpleTypeH\x00\x12\x42\n\x08multisig\x18\x02 \x01(\x0b\x32..shiftcrypto.bitbox02.BTCScriptConfig.MultisigH\x00\x1a`\n\x08Multisig\x12\x11\n\tthreshold\x18\x01 \x01(\r\x12)\n\x05xpubs\x18\x02 \x03(\x0b\x32\x1a.shiftcrypto.bitbox02.XPub\x12\x16\n\x0eour_xpub_index\x18\x03 \x01(\r\")\n\nSimpleType\x12\x0f\n\x0bP2WPKH_P2SH\x10\x00\x12\n\n\x06P2WPKH\x10\x01\x42\x08\n\x06\x63onfig\"\xd7\x02\n\rBTCPubRequest\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12\x0f\n\x07keypath\x18\x02 \x03(\r\x12\x41\n\txpub_type\x18\x03 \x01(\x0e\x32,.shiftcrypto.bitbox02.BTCPubRequest.XPubTypeH\x00\x12>\n\rscript_config\x18\x04 \x01(\x0b\x32%.shiftcrypto.bitbox02.BTCScriptConfigH\x00\x12\x0f\n\x07\x64isplay\x18\x05 \x01(\x08\"j\n\x08XPubType\x12\x08\n\x04TPUB\x10\x00\x12\x08\n\x04XPUB\x10\x01\x12\x08\n\x04YPUB\x10\x02\x12\x08\n\x04ZPUB\x10\x03\x12\x08\n\x04VPUB\x10\x04\x12\x08\n\x04UPUB\x10\x05\x12\x10\n\x0c\x43\x41PITAL_VPUB\x10\x06\x12\x10\n\x0c\x43\x41PITAL_ZPUB\x10\x07\x42\x08\n\x06output\"\xe4\x01\n\x12\x42TCSignInitRequest\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12<\n\rscript_config\x18\x02 \x01(\x0b\x32%.shiftcrypto.bitbox02.BTCScriptConfig\x12\x17\n\x0fkeypath_account\x18\x03 \x03(\r\x12\x0f\n\x07version\x18\x04 \x01(\r\x12\x12\n\nnum_inputs\x18\x05 \x01(\r\x12\x13\n\x0bnum_outputs\x18\x06 \x01(\r\x12\x10\n\x08locktime\x18\x07 \x01(\r\"\xb5\x01\n\x13\x42TCSignNextResponse\x12<\n\x04type\x18\x01 \x01(\x0e\x32..shiftcrypto.bitbox02.BTCSignNextResponse.Type\x12\r\n\x05index\x18\x02 \x01(\r\x12\x15\n\rhas_signature\x18\x03 \x01(\x08\x12\x11\n\tsignature\x18\x04 \x01(\x0c\"\'\n\x04Type\x12\t\n\x05INPUT\x10\x00\x12\n\n\x06OUTPUT\x10\x01\x12\x08\n\x04\x44ONE\x10\x02\"y\n\x13\x42TCSignInputRequest\x12\x13\n\x0bprevOutHash\x18\x01 \x01(\x0c\x12\x14\n\x0cprevOutIndex\x18\x02 \x01(\r\x12\x14\n\x0cprevOutValue\x18\x03 \x01(\x04\x12\x10\n\x08sequence\x18\x04 \x01(\r\x12\x0f\n\x07keypath\x18\x06 \x03(\r\"\x85\x01\n\x14\x42TCSignOutputRequest\x12\x0c\n\x04ours\x18\x01 \x01(\x08\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.shiftcrypto.bitbox02.BTCOutputType\x12\r\n\x05value\x18\x03 \x01(\x04\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12\x0f\n\x07keypath\x18\x05 \x03(\r\"\x99\x01\n\x1b\x42TCScriptConfigRegistration\x12+\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x1d.shiftcrypto.bitbox02.BTCCoin\x12<\n\rscript_config\x18\x02 \x01(\x0b\x32%.shiftcrypto.bitbox02.BTCScriptConfig\x12\x0f\n\x07keypath\x18\x03 \x03(\r\"\x0c\n\nBTCSuccess\"m\n\"BTCIsScriptConfigRegisteredRequest\x12G\n\x0cregistration\x18\x01 \x01(\x0b\x32\x31.shiftcrypto.bitbox02.BTCScriptConfigRegistration\"<\n#BTCIsScriptConfigRegisteredResponse\x12\x15\n\ris_registered\x18\x01 \x01(\x08\"w\n\x1e\x42TCRegisterScriptConfigRequest\x12G\n\x0cregistration\x18\x01 \x01(\x0b\x32\x31.shiftcrypto.bitbox02.BTCScriptConfigRegistration\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xd0\x01\n\nBTCRequest\x12_\n\x1bis_script_config_registered\x18\x01 \x01(\x0b\x32\x38.shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredRequestH\x00\x12V\n\x16register_script_config\x18\x02 \x01(\x0b\x32\x34.shiftcrypto.bitbox02.BTCRegisterScriptConfigRequestH\x00\x42\t\n\x07request\"\xb0\x01\n\x0b\x42TCResponse\x12\x33\n\x07success\x18\x01 \x01(\x0b\x32 .shiftcrypto.bitbox02.BTCSuccessH\x00\x12`\n\x1bis_script_config_registered\x18\x02 \x01(\x0b\x32\x39.shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredResponseH\x00\x42\n\n\x08response*/\n\x07\x42TCCoin\x12\x07\n\x03\x42TC\x10\x00\x12\x08\n\x04TBTC\x10\x01\x12\x07\n\x03LTC\x10\x02\x12\x08\n\x04TLTC\x10\x03*H\n\rBTCOutputType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05P2PKH\x10\x01\x12\x08\n\x04P2SH\x10\x02\x12\n\n\x06P2WPKH\x10\x03\x12\t\n\x05P2WSH\x10\x04\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BTCCOIN = _descriptor.EnumDescriptor(
  name='BTCCoin',
  full_name='shiftcrypto.bitbox02.BTCCoin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BTC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TBTC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LTC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TLTC', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2235,
  serialized_end=2282,
)
_sym_db.RegisterEnumDescriptor(_BTCCOIN)

BTCCoin = enum_type_wrapper.EnumTypeWrapper(_BTCCOIN)
_BTCOUTPUTTYPE = _descriptor.EnumDescriptor(
  name='BTCOutputType',
  full_name='shiftcrypto.bitbox02.BTCOutputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2PKH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2SH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2WPKH', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2WSH', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2284,
  serialized_end=2356,
)
_sym_db.RegisterEnumDescriptor(_BTCOUTPUTTYPE)

BTCOutputType = enum_type_wrapper.EnumTypeWrapper(_BTCOUTPUTTYPE)
BTC = 0
TBTC = 1
LTC = 2
TLTC = 3
UNKNOWN = 0
P2PKH = 1
P2SH = 2
P2WPKH = 3
P2WSH = 4


_BTCSCRIPTCONFIG_SIMPLETYPE = _descriptor.EnumDescriptor(
  name='SimpleType',
  full_name='shiftcrypto.bitbox02.BTCScriptConfig.SimpleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='P2WPKH_P2SH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2WPKH', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=308,
  serialized_end=349,
)
_sym_db.RegisterEnumDescriptor(_BTCSCRIPTCONFIG_SIMPLETYPE)

_BTCPUBREQUEST_XPUBTYPE = _descriptor.EnumDescriptor(
  name='XPubType',
  full_name='shiftcrypto.bitbox02.BTCPubRequest.XPubType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TPUB', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XPUB', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YPUB', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZPUB', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VPUB', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPUB', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAPITAL_VPUB', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAPITAL_ZPUB', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=589,
  serialized_end=695,
)
_sym_db.RegisterEnumDescriptor(_BTCPUBREQUEST_XPUBTYPE)

_BTCSIGNNEXTRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='shiftcrypto.bitbox02.BTCSignNextResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPUT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1081,
  serialized_end=1120,
)
_sym_db.RegisterEnumDescriptor(_BTCSIGNNEXTRESPONSE_TYPE)


_BTCSCRIPTCONFIG_MULTISIG = _descriptor.Descriptor(
  name='Multisig',
  full_name='shiftcrypto.bitbox02.BTCScriptConfig.Multisig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='threshold', full_name='shiftcrypto.bitbox02.BTCScriptConfig.Multisig.threshold', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xpubs', full_name='shiftcrypto.bitbox02.BTCScriptConfig.Multisig.xpubs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='our_xpub_index', full_name='shiftcrypto.bitbox02.BTCScriptConfig.Multisig.our_xpub_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=306,
)

_BTCSCRIPTCONFIG = _descriptor.Descriptor(
  name='BTCScriptConfig',
  full_name='shiftcrypto.bitbox02.BTCScriptConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simple_type', full_name='shiftcrypto.bitbox02.BTCScriptConfig.simple_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multisig', full_name='shiftcrypto.bitbox02.BTCScriptConfig.multisig', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BTCSCRIPTCONFIG_MULTISIG, ],
  enum_types=[
    _BTCSCRIPTCONFIG_SIMPLETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='config', full_name='shiftcrypto.bitbox02.BTCScriptConfig.config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=50,
  serialized_end=359,
)


_BTCPUBREQUEST = _descriptor.Descriptor(
  name='BTCPubRequest',
  full_name='shiftcrypto.bitbox02.BTCPubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='shiftcrypto.bitbox02.BTCPubRequest.coin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='shiftcrypto.bitbox02.BTCPubRequest.keypath', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xpub_type', full_name='shiftcrypto.bitbox02.BTCPubRequest.xpub_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_config', full_name='shiftcrypto.bitbox02.BTCPubRequest.script_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display', full_name='shiftcrypto.bitbox02.BTCPubRequest.display', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BTCPUBREQUEST_XPUBTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='output', full_name='shiftcrypto.bitbox02.BTCPubRequest.output',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=362,
  serialized_end=705,
)


_BTCSIGNINITREQUEST = _descriptor.Descriptor(
  name='BTCSignInitRequest',
  full_name='shiftcrypto.bitbox02.BTCSignInitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.coin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_config', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.script_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypath_account', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.keypath_account', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.version', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_inputs', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.num_inputs', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_outputs', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.num_outputs', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locktime', full_name='shiftcrypto.bitbox02.BTCSignInitRequest.locktime', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=708,
  serialized_end=936,
)


_BTCSIGNNEXTRESPONSE = _descriptor.Descriptor(
  name='BTCSignNextResponse',
  full_name='shiftcrypto.bitbox02.BTCSignNextResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='shiftcrypto.bitbox02.BTCSignNextResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='shiftcrypto.bitbox02.BTCSignNextResponse.index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_signature', full_name='shiftcrypto.bitbox02.BTCSignNextResponse.has_signature', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='shiftcrypto.bitbox02.BTCSignNextResponse.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BTCSIGNNEXTRESPONSE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=939,
  serialized_end=1120,
)


_BTCSIGNINPUTREQUEST = _descriptor.Descriptor(
  name='BTCSignInputRequest',
  full_name='shiftcrypto.bitbox02.BTCSignInputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevOutHash', full_name='shiftcrypto.bitbox02.BTCSignInputRequest.prevOutHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prevOutIndex', full_name='shiftcrypto.bitbox02.BTCSignInputRequest.prevOutIndex', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prevOutValue', full_name='shiftcrypto.bitbox02.BTCSignInputRequest.prevOutValue', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='shiftcrypto.bitbox02.BTCSignInputRequest.sequence', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='shiftcrypto.bitbox02.BTCSignInputRequest.keypath', index=4,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1122,
  serialized_end=1243,
)


_BTCSIGNOUTPUTREQUEST = _descriptor.Descriptor(
  name='BTCSignOutputRequest',
  full_name='shiftcrypto.bitbox02.BTCSignOutputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ours', full_name='shiftcrypto.bitbox02.BTCSignOutputRequest.ours', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='shiftcrypto.bitbox02.BTCSignOutputRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='shiftcrypto.bitbox02.BTCSignOutputRequest.value', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='shiftcrypto.bitbox02.BTCSignOutputRequest.hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='shiftcrypto.bitbox02.BTCSignOutputRequest.keypath', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1246,
  serialized_end=1379,
)


_BTCSCRIPTCONFIGREGISTRATION = _descriptor.Descriptor(
  name='BTCScriptConfigRegistration',
  full_name='shiftcrypto.bitbox02.BTCScriptConfigRegistration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='shiftcrypto.bitbox02.BTCScriptConfigRegistration.coin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='script_config', full_name='shiftcrypto.bitbox02.BTCScriptConfigRegistration.script_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='shiftcrypto.bitbox02.BTCScriptConfigRegistration.keypath', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1382,
  serialized_end=1535,
)


_BTCSUCCESS = _descriptor.Descriptor(
  name='BTCSuccess',
  full_name='shiftcrypto.bitbox02.BTCSuccess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1537,
  serialized_end=1549,
)


_BTCISSCRIPTCONFIGREGISTEREDREQUEST = _descriptor.Descriptor(
  name='BTCIsScriptConfigRegisteredRequest',
  full_name='shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration', full_name='shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredRequest.registration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1551,
  serialized_end=1660,
)


_BTCISSCRIPTCONFIGREGISTEREDRESPONSE = _descriptor.Descriptor(
  name='BTCIsScriptConfigRegisteredResponse',
  full_name='shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_registered', full_name='shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredResponse.is_registered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1662,
  serialized_end=1722,
)


_BTCREGISTERSCRIPTCONFIGREQUEST = _descriptor.Descriptor(
  name='BTCRegisterScriptConfigRequest',
  full_name='shiftcrypto.bitbox02.BTCRegisterScriptConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration', full_name='shiftcrypto.bitbox02.BTCRegisterScriptConfigRequest.registration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='shiftcrypto.bitbox02.BTCRegisterScriptConfigRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1724,
  serialized_end=1843,
)


_BTCREQUEST = _descriptor.Descriptor(
  name='BTCRequest',
  full_name='shiftcrypto.bitbox02.BTCRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_script_config_registered', full_name='shiftcrypto.bitbox02.BTCRequest.is_script_config_registered', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='register_script_config', full_name='shiftcrypto.bitbox02.BTCRequest.register_script_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='request', full_name='shiftcrypto.bitbox02.BTCRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1846,
  serialized_end=2054,
)


_BTCRESPONSE = _descriptor.Descriptor(
  name='BTCResponse',
  full_name='shiftcrypto.bitbox02.BTCResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='shiftcrypto.bitbox02.BTCResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_script_config_registered', full_name='shiftcrypto.bitbox02.BTCResponse.is_script_config_registered', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='response', full_name='shiftcrypto.bitbox02.BTCResponse.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=2057,
  serialized_end=2233,
)

_BTCSCRIPTCONFIG_MULTISIG.fields_by_name['xpubs'].message_type = common__pb2._XPUB
_BTCSCRIPTCONFIG_MULTISIG.containing_type = _BTCSCRIPTCONFIG
_BTCSCRIPTCONFIG.fields_by_name['simple_type'].enum_type = _BTCSCRIPTCONFIG_SIMPLETYPE
_BTCSCRIPTCONFIG.fields_by_name['multisig'].message_type = _BTCSCRIPTCONFIG_MULTISIG
_BTCSCRIPTCONFIG_SIMPLETYPE.containing_type = _BTCSCRIPTCONFIG
_BTCSCRIPTCONFIG.oneofs_by_name['config'].fields.append(
  _BTCSCRIPTCONFIG.fields_by_name['simple_type'])
_BTCSCRIPTCONFIG.fields_by_name['simple_type'].containing_oneof = _BTCSCRIPTCONFIG.oneofs_by_name['config']
_BTCSCRIPTCONFIG.oneofs_by_name['config'].fields.append(
  _BTCSCRIPTCONFIG.fields_by_name['multisig'])
_BTCSCRIPTCONFIG.fields_by_name['multisig'].containing_oneof = _BTCSCRIPTCONFIG.oneofs_by_name['config']
_BTCPUBREQUEST.fields_by_name['coin'].enum_type = _BTCCOIN
_BTCPUBREQUEST.fields_by_name['xpub_type'].enum_type = _BTCPUBREQUEST_XPUBTYPE
_BTCPUBREQUEST.fields_by_name['script_config'].message_type = _BTCSCRIPTCONFIG
_BTCPUBREQUEST_XPUBTYPE.containing_type = _BTCPUBREQUEST
_BTCPUBREQUEST.oneofs_by_name['output'].fields.append(
  _BTCPUBREQUEST.fields_by_name['xpub_type'])
_BTCPUBREQUEST.fields_by_name['xpub_type'].containing_oneof = _BTCPUBREQUEST.oneofs_by_name['output']
_BTCPUBREQUEST.oneofs_by_name['output'].fields.append(
  _BTCPUBREQUEST.fields_by_name['script_config'])
_BTCPUBREQUEST.fields_by_name['script_config'].containing_oneof = _BTCPUBREQUEST.oneofs_by_name['output']
_BTCSIGNINITREQUEST.fields_by_name['coin'].enum_type = _BTCCOIN
_BTCSIGNINITREQUEST.fields_by_name['script_config'].message_type = _BTCSCRIPTCONFIG
_BTCSIGNNEXTRESPONSE.fields_by_name['type'].enum_type = _BTCSIGNNEXTRESPONSE_TYPE
_BTCSIGNNEXTRESPONSE_TYPE.containing_type = _BTCSIGNNEXTRESPONSE
_BTCSIGNOUTPUTREQUEST.fields_by_name['type'].enum_type = _BTCOUTPUTTYPE
_BTCSCRIPTCONFIGREGISTRATION.fields_by_name['coin'].enum_type = _BTCCOIN
_BTCSCRIPTCONFIGREGISTRATION.fields_by_name['script_config'].message_type = _BTCSCRIPTCONFIG
_BTCISSCRIPTCONFIGREGISTEREDREQUEST.fields_by_name['registration'].message_type = _BTCSCRIPTCONFIGREGISTRATION
_BTCREGISTERSCRIPTCONFIGREQUEST.fields_by_name['registration'].message_type = _BTCSCRIPTCONFIGREGISTRATION
_BTCREQUEST.fields_by_name['is_script_config_registered'].message_type = _BTCISSCRIPTCONFIGREGISTEREDREQUEST
_BTCREQUEST.fields_by_name['register_script_config'].message_type = _BTCREGISTERSCRIPTCONFIGREQUEST
_BTCREQUEST.oneofs_by_name['request'].fields.append(
  _BTCREQUEST.fields_by_name['is_script_config_registered'])
_BTCREQUEST.fields_by_name['is_script_config_registered'].containing_oneof = _BTCREQUEST.oneofs_by_name['request']
_BTCREQUEST.oneofs_by_name['request'].fields.append(
  _BTCREQUEST.fields_by_name['register_script_config'])
_BTCREQUEST.fields_by_name['register_script_config'].containing_oneof = _BTCREQUEST.oneofs_by_name['request']
_BTCRESPONSE.fields_by_name['success'].message_type = _BTCSUCCESS
_BTCRESPONSE.fields_by_name['is_script_config_registered'].message_type = _BTCISSCRIPTCONFIGREGISTEREDRESPONSE
_BTCRESPONSE.oneofs_by_name['response'].fields.append(
  _BTCRESPONSE.fields_by_name['success'])
_BTCRESPONSE.fields_by_name['success'].containing_oneof = _BTCRESPONSE.oneofs_by_name['response']
_BTCRESPONSE.oneofs_by_name['response'].fields.append(
  _BTCRESPONSE.fields_by_name['is_script_config_registered'])
_BTCRESPONSE.fields_by_name['is_script_config_registered'].containing_oneof = _BTCRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['BTCScriptConfig'] = _BTCSCRIPTCONFIG
DESCRIPTOR.message_types_by_name['BTCPubRequest'] = _BTCPUBREQUEST
DESCRIPTOR.message_types_by_name['BTCSignInitRequest'] = _BTCSIGNINITREQUEST
DESCRIPTOR.message_types_by_name['BTCSignNextResponse'] = _BTCSIGNNEXTRESPONSE
DESCRIPTOR.message_types_by_name['BTCSignInputRequest'] = _BTCSIGNINPUTREQUEST
DESCRIPTOR.message_types_by_name['BTCSignOutputRequest'] = _BTCSIGNOUTPUTREQUEST
DESCRIPTOR.message_types_by_name['BTCScriptConfigRegistration'] = _BTCSCRIPTCONFIGREGISTRATION
DESCRIPTOR.message_types_by_name['BTCSuccess'] = _BTCSUCCESS
DESCRIPTOR.message_types_by_name['BTCIsScriptConfigRegisteredRequest'] = _BTCISSCRIPTCONFIGREGISTEREDREQUEST
DESCRIPTOR.message_types_by_name['BTCIsScriptConfigRegisteredResponse'] = _BTCISSCRIPTCONFIGREGISTEREDRESPONSE
DESCRIPTOR.message_types_by_name['BTCRegisterScriptConfigRequest'] = _BTCREGISTERSCRIPTCONFIGREQUEST
DESCRIPTOR.message_types_by_name['BTCRequest'] = _BTCREQUEST
DESCRIPTOR.message_types_by_name['BTCResponse'] = _BTCRESPONSE
DESCRIPTOR.enum_types_by_name['BTCCoin'] = _BTCCOIN
DESCRIPTOR.enum_types_by_name['BTCOutputType'] = _BTCOUTPUTTYPE

BTCScriptConfig = _reflection.GeneratedProtocolMessageType('BTCScriptConfig', (_message.Message,), dict(

  Multisig = _reflection.GeneratedProtocolMessageType('Multisig', (_message.Message,), dict(
    DESCRIPTOR = _BTCSCRIPTCONFIG_MULTISIG,
    __module__ = 'btc_pb2'
    # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCScriptConfig.Multisig)
    ))
  ,
  DESCRIPTOR = _BTCSCRIPTCONFIG,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCScriptConfig)
  ))
_sym_db.RegisterMessage(BTCScriptConfig)
_sym_db.RegisterMessage(BTCScriptConfig.Multisig)

BTCPubRequest = _reflection.GeneratedProtocolMessageType('BTCPubRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCPUBREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCPubRequest)
  ))
_sym_db.RegisterMessage(BTCPubRequest)

BTCSignInitRequest = _reflection.GeneratedProtocolMessageType('BTCSignInitRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNINITREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCSignInitRequest)
  ))
_sym_db.RegisterMessage(BTCSignInitRequest)

BTCSignNextResponse = _reflection.GeneratedProtocolMessageType('BTCSignNextResponse', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNNEXTRESPONSE,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCSignNextResponse)
  ))
_sym_db.RegisterMessage(BTCSignNextResponse)

BTCSignInputRequest = _reflection.GeneratedProtocolMessageType('BTCSignInputRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNINPUTREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCSignInputRequest)
  ))
_sym_db.RegisterMessage(BTCSignInputRequest)

BTCSignOutputRequest = _reflection.GeneratedProtocolMessageType('BTCSignOutputRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNOUTPUTREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCSignOutputRequest)
  ))
_sym_db.RegisterMessage(BTCSignOutputRequest)

BTCScriptConfigRegistration = _reflection.GeneratedProtocolMessageType('BTCScriptConfigRegistration', (_message.Message,), dict(
  DESCRIPTOR = _BTCSCRIPTCONFIGREGISTRATION,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCScriptConfigRegistration)
  ))
_sym_db.RegisterMessage(BTCScriptConfigRegistration)

BTCSuccess = _reflection.GeneratedProtocolMessageType('BTCSuccess', (_message.Message,), dict(
  DESCRIPTOR = _BTCSUCCESS,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCSuccess)
  ))
_sym_db.RegisterMessage(BTCSuccess)

BTCIsScriptConfigRegisteredRequest = _reflection.GeneratedProtocolMessageType('BTCIsScriptConfigRegisteredRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCISSCRIPTCONFIGREGISTEREDREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredRequest)
  ))
_sym_db.RegisterMessage(BTCIsScriptConfigRegisteredRequest)

BTCIsScriptConfigRegisteredResponse = _reflection.GeneratedProtocolMessageType('BTCIsScriptConfigRegisteredResponse', (_message.Message,), dict(
  DESCRIPTOR = _BTCISSCRIPTCONFIGREGISTEREDRESPONSE,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCIsScriptConfigRegisteredResponse)
  ))
_sym_db.RegisterMessage(BTCIsScriptConfigRegisteredResponse)

BTCRegisterScriptConfigRequest = _reflection.GeneratedProtocolMessageType('BTCRegisterScriptConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCREGISTERSCRIPTCONFIGREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCRegisterScriptConfigRequest)
  ))
_sym_db.RegisterMessage(BTCRegisterScriptConfigRequest)

BTCRequest = _reflection.GeneratedProtocolMessageType('BTCRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCRequest)
  ))
_sym_db.RegisterMessage(BTCRequest)

BTCResponse = _reflection.GeneratedProtocolMessageType('BTCResponse', (_message.Message,), dict(
  DESCRIPTOR = _BTCRESPONSE,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.BTCResponse)
  ))
_sym_db.RegisterMessage(BTCResponse)


# @@protoc_insertion_point(module_scope)
