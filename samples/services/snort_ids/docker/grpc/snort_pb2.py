# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snort.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='snort.proto',
  package='snort',
  syntax='proto3',
  serialized_pb=_b('\n\x0bsnort.proto\x12\x05snort\"\x1b\n\x0c\x43ontrolSnort\x12\x0b\n\x03pid\x18\x01 \x01(\t\"\x99\x01\n\x07\x41\x64\x64Rule\x12\x10\n\x08protocol\x18\x01 \x01(\t\x12\x11\n\tdest_port\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65st_ip\x18\x03 \x01(\t\x12\x10\n\x08src_port\x18\x04 \x01(\t\x12\x0e\n\x06src_ip\x18\x05 \x01(\t\x12\x0b\n\x03msg\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\x0b\n\x03sid\x18\x08 \x01(\t\x12\x0b\n\x03rev\x18\t \x01(\t\"\x1d\n\nSnortReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xac\x01\n\nController\x12/\n\x08\x41\x64\x64Rules\x12\x0e.snort.AddRule\x1a\x11.snort.SnortReply\"\x00\x12\x36\n\nStartSnort\x12\x13.snort.ControlSnort\x1a\x11.snort.SnortReply\"\x00\x12\x35\n\tStopSnort\x12\x13.snort.ControlSnort\x1a\x11.snort.SnortReply\"\x00\x62\x06proto3')
)




_CONTROLSNORT = _descriptor.Descriptor(
  name='ControlSnort',
  full_name='snort.ControlSnort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='snort.ControlSnort.pid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=22,
  serialized_end=49,
)


_ADDRULE = _descriptor.Descriptor(
  name='AddRule',
  full_name='snort.AddRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='snort.AddRule.protocol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_port', full_name='snort.AddRule.dest_port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_ip', full_name='snort.AddRule.dest_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_port', full_name='snort.AddRule.src_port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_ip', full_name='snort.AddRule.src_ip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='snort.AddRule.msg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='snort.AddRule.content', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid', full_name='snort.AddRule.sid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rev', full_name='snort.AddRule.rev', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=52,
  serialized_end=205,
)


_SNORTREPLY = _descriptor.Descriptor(
  name='SnortReply',
  full_name='snort.SnortReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='snort.SnortReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=207,
  serialized_end=236,
)

DESCRIPTOR.message_types_by_name['ControlSnort'] = _CONTROLSNORT
DESCRIPTOR.message_types_by_name['AddRule'] = _ADDRULE
DESCRIPTOR.message_types_by_name['SnortReply'] = _SNORTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlSnort = _reflection.GeneratedProtocolMessageType('ControlSnort', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLSNORT,
  __module__ = 'snort_pb2'
  # @@protoc_insertion_point(class_scope:snort.ControlSnort)
  ))
_sym_db.RegisterMessage(ControlSnort)

AddRule = _reflection.GeneratedProtocolMessageType('AddRule', (_message.Message,), dict(
  DESCRIPTOR = _ADDRULE,
  __module__ = 'snort_pb2'
  # @@protoc_insertion_point(class_scope:snort.AddRule)
  ))
_sym_db.RegisterMessage(AddRule)

SnortReply = _reflection.GeneratedProtocolMessageType('SnortReply', (_message.Message,), dict(
  DESCRIPTOR = _SNORTREPLY,
  __module__ = 'snort_pb2'
  # @@protoc_insertion_point(class_scope:snort.SnortReply)
  ))
_sym_db.RegisterMessage(SnortReply)



_CONTROLLER = _descriptor.ServiceDescriptor(
  name='Controller',
  full_name='snort.Controller',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=239,
  serialized_end=411,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddRules',
    full_name='snort.Controller.AddRules',
    index=0,
    containing_service=None,
    input_type=_ADDRULE,
    output_type=_SNORTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartSnort',
    full_name='snort.Controller.StartSnort',
    index=1,
    containing_service=None,
    input_type=_CONTROLSNORT,
    output_type=_SNORTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopSnort',
    full_name='snort.Controller.StopSnort',
    index=2,
    containing_service=None,
    input_type=_CONTROLSNORT,
    output_type=_SNORTREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLER)

DESCRIPTOR.services_by_name['Controller'] = _CONTROLLER

# @@protoc_insertion_point(module_scope)
