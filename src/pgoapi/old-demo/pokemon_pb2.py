# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pokemon.proto

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
  name='pokemon.proto',
  package='',
  serialized_pb=_b('\n\rpokemon.proto\"\xc7\x04\n\x0eRequestEnvelop\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x0e\n\x06rpc_id\x18\x03 \x01(\x03\x12*\n\x08requests\x18\x04 \x03(\x0b\x32\x18.RequestEnvelop.Requests\x12*\n\x08unknown6\x18\x06 \x01(\x0b\x32\x18.RequestEnvelop.Unknown6\x12\x10\n\x08latitude\x18\x07 \x01(\x06\x12\x11\n\tlongitude\x18\x08 \x01(\x06\x12\x10\n\x08\x61ltitude\x18\t \x01(\x06\x12&\n\x04\x61uth\x18\n \x01(\x0b\x32\x18.RequestEnvelop.AuthInfo\x12\x11\n\tunknown12\x18\x0c \x01(\x03\x1a\x43\n\x08Requests\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12)\n\x07message\x18\x02 \x01(\x0b\x32\x18.RequestEnvelop.Unknown3\x1a\x1c\n\x08Unknown3\x12\x10\n\x08unknown4\x18\x01 \x02(\t\x1ao\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x33\n\x08unknown2\x18\x02 \x02(\x0b\x32!.RequestEnvelop.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x02(\x0c\x1au\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x02(\t\x12+\n\x05token\x18\x02 \x02(\x0b\x32\x1c.RequestEnvelop.AuthInfo.JWT\x1a*\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x02(\t\x12\x11\n\tunknown13\x18\x02 \x02(\x05\"\xf7\x07\n\x0fResponseEnvelop\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x10\n\x08unknown2\x18\x02 \x01(\x03\x12\x0f\n\x07\x61pi_url\x18\x03 \x01(\t\x12+\n\x08unknown6\x18\x06 \x01(\x0b\x32\x19.ResponseEnvelop.Unknown6\x12+\n\x08unknown7\x18\x07 \x01(\x0b\x32\x19.ResponseEnvelop.Unknown7\x12)\n\x07payload\x18\x64 \x03(\x0b\x32\x18.ResponseEnvelop.Payload\x1ap\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12\x34\n\x08unknown2\x18\x02 \x02(\x0b\x32\".ResponseEnvelop.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x02(\x0c\x1a\x43\n\x08Unknown7\x12\x11\n\tunknown71\x18\x01 \x01(\x0c\x12\x11\n\tunknown72\x18\x02 \x01(\x03\x12\x11\n\tunknown73\x18\x03 \x01(\x0c\x1a\x46\n\x07Payload\x12\x10\n\x08unknown1\x18\x01 \x02(\x05\x12)\n\x07profile\x18\x02 \x01(\x0b\x32\x18.ResponseEnvelop.Profile\x1a\xaa\x04\n\x07Profile\x12\x15\n\rcreation_time\x18\x01 \x02(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04team\x18\x05 \x01(\x05\x12\x10\n\x08tutorial\x18\x07 \x01(\x0c\x12\x36\n\x06\x61vatar\x18\x08 \x01(\x0b\x32&.ResponseEnvelop.Profile.AvatarDetails\x12\x14\n\x0cpoke_storage\x18\t \x01(\x05\x12\x14\n\x0citem_storage\x18\n \x01(\x05\x12\x38\n\x0b\x64\x61ily_bonus\x18\x0b \x01(\x0b\x32#.ResponseEnvelop.Profile.DailyBonus\x12\x11\n\tunknown12\x18\x0c \x01(\x0c\x12\x11\n\tunknown13\x18\r \x01(\x0c\x12\x33\n\x08\x63urrency\x18\x0e \x03(\x0b\x32!.ResponseEnvelop.Profile.Currency\x1aX\n\rAvatarDetails\x12\x10\n\x08unknown2\x18\x02 \x01(\x05\x12\x10\n\x08unknown3\x18\x03 \x01(\x05\x12\x10\n\x08unknown9\x18\t \x01(\x05\x12\x11\n\tunknown10\x18\n \x01(\x05\x1aY\n\nDailyBonus\x12\x1e\n\x16NextCollectTimestampMs\x18\x01 \x01(\x03\x12+\n#NextDefenderBonusCollectTimestampMs\x18\x02 \x01(\x03\x1a(\n\x08\x43urrency\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTENVELOP_REQUESTS = _descriptor.Descriptor(
  name='Requests',
  full_name='RequestEnvelop.Requests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='RequestEnvelop.Requests.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='RequestEnvelop.Requests.message', index=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=339,
)

_REQUESTENVELOP_UNKNOWN3 = _descriptor.Descriptor(
  name='Unknown3',
  full_name='RequestEnvelop.Unknown3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown4', full_name='RequestEnvelop.Unknown3.unknown4', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=369,
)

_REQUESTENVELOP_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='RequestEnvelop.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelop.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=482,
)

_REQUESTENVELOP_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='RequestEnvelop.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelop.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='RequestEnvelop.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=482,
)

_REQUESTENVELOP_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='RequestEnvelop.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='RequestEnvelop.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown13', full_name='RequestEnvelop.AuthInfo.JWT.unknown13', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=601,
)

_REQUESTENVELOP_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='RequestEnvelop.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='RequestEnvelop.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='RequestEnvelop.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=601,
)

_REQUESTENVELOP = _descriptor.Descriptor(
  name='RequestEnvelop',
  full_name='RequestEnvelop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelop.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc_id', full_name='RequestEnvelop.rpc_id', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requests', full_name='RequestEnvelop.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='RequestEnvelop.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='RequestEnvelop.latitude', index=4,
      number=7, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='RequestEnvelop.longitude', index=5,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='RequestEnvelop.altitude', index=6,
      number=9, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth', full_name='RequestEnvelop.auth', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='RequestEnvelop.unknown12', index=8,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_REQUESTS, _REQUESTENVELOP_UNKNOWN3, _REQUESTENVELOP_UNKNOWN6, _REQUESTENVELOP_AUTHINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=601,
)


_RESPONSEENVELOP_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='ResponseEnvelop.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelop.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=482,
)

_RESPONSEENVELOP_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='ResponseEnvelop.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelop.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='ResponseEnvelop.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOP_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=921,
)

_RESPONSEENVELOP_UNKNOWN7 = _descriptor.Descriptor(
  name='Unknown7',
  full_name='ResponseEnvelop.Unknown7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown71', full_name='ResponseEnvelop.Unknown7.unknown71', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown72', full_name='ResponseEnvelop.Unknown7.unknown72', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown73', full_name='ResponseEnvelop.Unknown7.unknown73', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=923,
  serialized_end=990,
)

_RESPONSEENVELOP_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='ResponseEnvelop.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelop.Payload.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='profile', full_name='ResponseEnvelop.Payload.profile', index=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=992,
  serialized_end=1062,
)

_RESPONSEENVELOP_PROFILE_AVATARDETAILS = _descriptor.Descriptor(
  name='AvatarDetails',
  full_name='ResponseEnvelop.Profile.AvatarDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='ResponseEnvelop.Profile.AvatarDetails.unknown2', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown3', full_name='ResponseEnvelop.Profile.AvatarDetails.unknown3', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown9', full_name='ResponseEnvelop.Profile.AvatarDetails.unknown9', index=2,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown10', full_name='ResponseEnvelop.Profile.AvatarDetails.unknown10', index=3,
      number=10, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1398,
  serialized_end=1486,
)

_RESPONSEENVELOP_PROFILE_DAILYBONUS = _descriptor.Descriptor(
  name='DailyBonus',
  full_name='ResponseEnvelop.Profile.DailyBonus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NextCollectTimestampMs', full_name='ResponseEnvelop.Profile.DailyBonus.NextCollectTimestampMs', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NextDefenderBonusCollectTimestampMs', full_name='ResponseEnvelop.Profile.DailyBonus.NextDefenderBonusCollectTimestampMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1488,
  serialized_end=1577,
)

_RESPONSEENVELOP_PROFILE_CURRENCY = _descriptor.Descriptor(
  name='Currency',
  full_name='ResponseEnvelop.Profile.Currency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ResponseEnvelop.Profile.Currency.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ResponseEnvelop.Profile.Currency.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1579,
  serialized_end=1619,
)

_RESPONSEENVELOP_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='ResponseEnvelop.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='ResponseEnvelop.Profile.creation_time', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='ResponseEnvelop.Profile.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='ResponseEnvelop.Profile.team', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tutorial', full_name='ResponseEnvelop.Profile.tutorial', index=3,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='ResponseEnvelop.Profile.avatar', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poke_storage', full_name='ResponseEnvelop.Profile.poke_storage', index=5,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_storage', full_name='ResponseEnvelop.Profile.item_storage', index=6,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_bonus', full_name='ResponseEnvelop.Profile.daily_bonus', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='ResponseEnvelop.Profile.unknown12', index=8,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown13', full_name='ResponseEnvelop.Profile.unknown13', index=9,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency', full_name='ResponseEnvelop.Profile.currency', index=10,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOP_PROFILE_AVATARDETAILS, _RESPONSEENVELOP_PROFILE_DAILYBONUS, _RESPONSEENVELOP_PROFILE_CURRENCY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1065,
  serialized_end=1619,
)

_RESPONSEENVELOP = _descriptor.Descriptor(
  name='ResponseEnvelop',
  full_name='ResponseEnvelop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='ResponseEnvelop.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='ResponseEnvelop.unknown2', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='api_url', full_name='ResponseEnvelop.api_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='ResponseEnvelop.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown7', full_name='ResponseEnvelop.unknown7', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='ResponseEnvelop.payload', index=5,
      number=100, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOP_UNKNOWN6, _RESPONSEENVELOP_UNKNOWN7, _RESPONSEENVELOP_PAYLOAD, _RESPONSEENVELOP_PROFILE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=1619,
)

_REQUESTENVELOP_REQUESTS.fields_by_name['message'].message_type = _REQUESTENVELOP_UNKNOWN3
_REQUESTENVELOP_REQUESTS.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_UNKNOWN3.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_UNKNOWN6_UNKNOWN2.containing_type = _REQUESTENVELOP_UNKNOWN6
_REQUESTENVELOP_UNKNOWN6.fields_by_name['unknown2'].message_type = _REQUESTENVELOP_UNKNOWN6_UNKNOWN2
_REQUESTENVELOP_UNKNOWN6.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_AUTHINFO_JWT.containing_type = _REQUESTENVELOP_AUTHINFO
_REQUESTENVELOP_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOP_AUTHINFO_JWT
_REQUESTENVELOP_AUTHINFO.containing_type = _REQUESTENVELOP
_REQUESTENVELOP.fields_by_name['requests'].message_type = _REQUESTENVELOP_REQUESTS
_REQUESTENVELOP.fields_by_name['unknown6'].message_type = _REQUESTENVELOP_UNKNOWN6
_REQUESTENVELOP.fields_by_name['auth'].message_type = _REQUESTENVELOP_AUTHINFO
_RESPONSEENVELOP_UNKNOWN6_UNKNOWN2.containing_type = _RESPONSEENVELOP_UNKNOWN6
_RESPONSEENVELOP_UNKNOWN6.fields_by_name['unknown2'].message_type = _RESPONSEENVELOP_UNKNOWN6_UNKNOWN2
_RESPONSEENVELOP_UNKNOWN6.containing_type = _RESPONSEENVELOP
_RESPONSEENVELOP_UNKNOWN7.containing_type = _RESPONSEENVELOP
_RESPONSEENVELOP_PAYLOAD.fields_by_name['profile'].message_type = _RESPONSEENVELOP_PROFILE
_RESPONSEENVELOP_PAYLOAD.containing_type = _RESPONSEENVELOP
_RESPONSEENVELOP_PROFILE_AVATARDETAILS.containing_type = _RESPONSEENVELOP_PROFILE
_RESPONSEENVELOP_PROFILE_DAILYBONUS.containing_type = _RESPONSEENVELOP_PROFILE
_RESPONSEENVELOP_PROFILE_CURRENCY.containing_type = _RESPONSEENVELOP_PROFILE
_RESPONSEENVELOP_PROFILE.fields_by_name['avatar'].message_type = _RESPONSEENVELOP_PROFILE_AVATARDETAILS
_RESPONSEENVELOP_PROFILE.fields_by_name['daily_bonus'].message_type = _RESPONSEENVELOP_PROFILE_DAILYBONUS
_RESPONSEENVELOP_PROFILE.fields_by_name['currency'].message_type = _RESPONSEENVELOP_PROFILE_CURRENCY
_RESPONSEENVELOP_PROFILE.containing_type = _RESPONSEENVELOP
_RESPONSEENVELOP.fields_by_name['unknown6'].message_type = _RESPONSEENVELOP_UNKNOWN6
_RESPONSEENVELOP.fields_by_name['unknown7'].message_type = _RESPONSEENVELOP_UNKNOWN7
_RESPONSEENVELOP.fields_by_name['payload'].message_type = _RESPONSEENVELOP_PAYLOAD
DESCRIPTOR.message_types_by_name['RequestEnvelop'] = _REQUESTENVELOP
DESCRIPTOR.message_types_by_name['ResponseEnvelop'] = _RESPONSEENVELOP

RequestEnvelop = _reflection.GeneratedProtocolMessageType('RequestEnvelop', (_message.Message,), dict(

  Requests = _reflection.GeneratedProtocolMessageType('Requests', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOP_REQUESTS,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.Requests)
    ))
  ,

  Unknown3 = _reflection.GeneratedProtocolMessageType('Unknown3', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOP_UNKNOWN3,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.Unknown3)
    ))
  ,

  Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

    Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOP_UNKNOWN6_UNKNOWN2,
      __module__ = 'pokemon_pb2'
      # @@protoc_insertion_point(class_scope:RequestEnvelop.Unknown6.Unknown2)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOP_UNKNOWN6,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.Unknown6)
    ))
  ,

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOP_AUTHINFO_JWT,
      __module__ = 'pokemon_pb2'
      # @@protoc_insertion_point(class_scope:RequestEnvelop.AuthInfo.JWT)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOP_AUTHINFO,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.AuthInfo)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOP,
  __module__ = 'pokemon_pb2'
  # @@protoc_insertion_point(class_scope:RequestEnvelop)
  ))
_sym_db.RegisterMessage(RequestEnvelop)
_sym_db.RegisterMessage(RequestEnvelop.Requests)
_sym_db.RegisterMessage(RequestEnvelop.Unknown3)
_sym_db.RegisterMessage(RequestEnvelop.Unknown6)
_sym_db.RegisterMessage(RequestEnvelop.Unknown6.Unknown2)
_sym_db.RegisterMessage(RequestEnvelop.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelop.AuthInfo.JWT)

ResponseEnvelop = _reflection.GeneratedProtocolMessageType('ResponseEnvelop', (_message.Message,), dict(

  Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

    Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSEENVELOP_UNKNOWN6_UNKNOWN2,
      __module__ = 'pokemon_pb2'
      # @@protoc_insertion_point(class_scope:ResponseEnvelop.Unknown6.Unknown2)
      ))
    ,
    DESCRIPTOR = _RESPONSEENVELOP_UNKNOWN6,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelop.Unknown6)
    ))
  ,

  Unknown7 = _reflection.GeneratedProtocolMessageType('Unknown7', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSEENVELOP_UNKNOWN7,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelop.Unknown7)
    ))
  ,

  Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSEENVELOP_PAYLOAD,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelop.Payload)
    ))
  ,

  Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(

    AvatarDetails = _reflection.GeneratedProtocolMessageType('AvatarDetails', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSEENVELOP_PROFILE_AVATARDETAILS,
      __module__ = 'pokemon_pb2'
      # @@protoc_insertion_point(class_scope:ResponseEnvelop.Profile.AvatarDetails)
      ))
    ,

    DailyBonus = _reflection.GeneratedProtocolMessageType('DailyBonus', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSEENVELOP_PROFILE_DAILYBONUS,
      __module__ = 'pokemon_pb2'
      # @@protoc_insertion_point(class_scope:ResponseEnvelop.Profile.DailyBonus)
      ))
    ,

    Currency = _reflection.GeneratedProtocolMessageType('Currency', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSEENVELOP_PROFILE_CURRENCY,
      __module__ = 'pokemon_pb2'
      # @@protoc_insertion_point(class_scope:ResponseEnvelop.Profile.Currency)
      ))
    ,
    DESCRIPTOR = _RESPONSEENVELOP_PROFILE,
    __module__ = 'pokemon_pb2'
    # @@protoc_insertion_point(class_scope:ResponseEnvelop.Profile)
    ))
  ,
  DESCRIPTOR = _RESPONSEENVELOP,
  __module__ = 'pokemon_pb2'
  # @@protoc_insertion_point(class_scope:ResponseEnvelop)
  ))
_sym_db.RegisterMessage(ResponseEnvelop)
_sym_db.RegisterMessage(ResponseEnvelop.Unknown6)
_sym_db.RegisterMessage(ResponseEnvelop.Unknown6.Unknown2)
_sym_db.RegisterMessage(ResponseEnvelop.Unknown7)
_sym_db.RegisterMessage(ResponseEnvelop.Payload)
_sym_db.RegisterMessage(ResponseEnvelop.Profile)
_sym_db.RegisterMessage(ResponseEnvelop.Profile.AvatarDetails)
_sym_db.RegisterMessage(ResponseEnvelop.Profile.DailyBonus)
_sym_db.RegisterMessage(ResponseEnvelop.Profile.Currency)


# @@protoc_insertion_point(module_scope)
