# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: agent.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'agent.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61gent.proto\"#\n\x08\x41gentMsg\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03\x63md\x18\x02 \x01(\t\"/\n\rAgentResponse\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\r\x12\x0c\n\x04resp\x18\x02 \x01(\t\"2\n\x0f\x41gentResponseML\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\r\x12\r\n\x05lines\x18\x02 \x03(\t\"9\n\rSystemdCmdMsg\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03\x63md\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\";\n\rNetworkCmdMsg\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\x0b\n\x03\x63md\x18\x03 \x01(\t2\xff\x01\n\x05\x41gent\x12\x34\n\x13SendCmdMultipleResp\x12\t.AgentMsg\x1a\x0e.AgentResponse\"\x00\x30\x01\x12\x30\n\x11SendCmdSingleResp\x12\t.AgentMsg\x1a\x0e.AgentResponse\"\x00\x12,\n\rSendCmdNoResp\x12\t.AgentMsg\x1a\x0e.AgentResponse\"\x00\x12\x30\n\nSystemdCmd\x12\x0e.SystemdCmdMsg\x1a\x10.AgentResponseML\"\x00\x12.\n\nNetworkCmd\x12\x0e.NetworkCmdMsg\x1a\x0e.AgentResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AGENTMSG']._serialized_start=15
  _globals['_AGENTMSG']._serialized_end=50
  _globals['_AGENTRESPONSE']._serialized_start=52
  _globals['_AGENTRESPONSE']._serialized_end=99
  _globals['_AGENTRESPONSEML']._serialized_start=101
  _globals['_AGENTRESPONSEML']._serialized_end=151
  _globals['_SYSTEMDCMDMSG']._serialized_start=153
  _globals['_SYSTEMDCMDMSG']._serialized_end=210
  _globals['_NETWORKCMDMSG']._serialized_start=212
  _globals['_NETWORKCMDMSG']._serialized_end=271
  _globals['_AGENT']._serialized_start=274
  _globals['_AGENT']._serialized_end=529
# @@protoc_insertion_point(module_scope)
