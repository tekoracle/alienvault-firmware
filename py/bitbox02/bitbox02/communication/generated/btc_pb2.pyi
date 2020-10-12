# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .common_pb2 import (
    XPub as common_pb2___XPub,
)

from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class BTCCoin(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> BTCCoin: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[BTCCoin]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, BTCCoin]]: ...
    BTC = typing___cast(BTCCoin, 0)
    TBTC = typing___cast(BTCCoin, 1)
    LTC = typing___cast(BTCCoin, 2)
    TLTC = typing___cast(BTCCoin, 3)
BTC = typing___cast(BTCCoin, 0)
TBTC = typing___cast(BTCCoin, 1)
LTC = typing___cast(BTCCoin, 2)
TLTC = typing___cast(BTCCoin, 3)

class BTCOutputType(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> BTCOutputType: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[BTCOutputType]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, BTCOutputType]]: ...
    UNKNOWN = typing___cast(BTCOutputType, 0)
    P2PKH = typing___cast(BTCOutputType, 1)
    P2SH = typing___cast(BTCOutputType, 2)
    P2WPKH = typing___cast(BTCOutputType, 3)
    P2WSH = typing___cast(BTCOutputType, 4)
UNKNOWN = typing___cast(BTCOutputType, 0)
P2PKH = typing___cast(BTCOutputType, 1)
P2SH = typing___cast(BTCOutputType, 2)
P2WPKH = typing___cast(BTCOutputType, 3)
P2WSH = typing___cast(BTCOutputType, 4)

class BTCScriptConfig(google___protobuf___message___Message):
    class SimpleType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BTCScriptConfig.SimpleType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BTCScriptConfig.SimpleType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BTCScriptConfig.SimpleType]]: ...
        P2WPKH_P2SH = typing___cast(BTCScriptConfig.SimpleType, 0)
        P2WPKH = typing___cast(BTCScriptConfig.SimpleType, 1)
    P2WPKH_P2SH = typing___cast(BTCScriptConfig.SimpleType, 0)
    P2WPKH = typing___cast(BTCScriptConfig.SimpleType, 1)

    class Multisig(google___protobuf___message___Message):
        class ScriptType(int):
            DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
            @classmethod
            def Name(cls, number: int) -> str: ...
            @classmethod
            def Value(cls, name: str) -> BTCScriptConfig.Multisig.ScriptType: ...
            @classmethod
            def keys(cls) -> typing___List[str]: ...
            @classmethod
            def values(cls) -> typing___List[BTCScriptConfig.Multisig.ScriptType]: ...
            @classmethod
            def items(cls) -> typing___List[typing___Tuple[str, BTCScriptConfig.Multisig.ScriptType]]: ...
            P2WSH = typing___cast(BTCScriptConfig.Multisig.ScriptType, 0)
            P2WSH_P2SH = typing___cast(BTCScriptConfig.Multisig.ScriptType, 1)
        P2WSH = typing___cast(BTCScriptConfig.Multisig.ScriptType, 0)
        P2WSH_P2SH = typing___cast(BTCScriptConfig.Multisig.ScriptType, 1)

        threshold = ... # type: int
        our_xpub_index = ... # type: int
        script_type = ... # type: BTCScriptConfig.Multisig.ScriptType

        @property
        def xpubs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[common_pb2___XPub]: ...

        def __init__(self,
            *,
            threshold : typing___Optional[int] = None,
            xpubs : typing___Optional[typing___Iterable[common_pb2___XPub]] = None,
            our_xpub_index : typing___Optional[int] = None,
            script_type : typing___Optional[BTCScriptConfig.Multisig.ScriptType] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> BTCScriptConfig.Multisig: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"our_xpub_index",u"script_type",u"threshold",u"xpubs"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"our_xpub_index",b"our_xpub_index",u"script_type",b"script_type",u"threshold",b"threshold",u"xpubs",b"xpubs"]) -> None: ...

    simple_type = ... # type: BTCScriptConfig.SimpleType

    @property
    def multisig(self) -> BTCScriptConfig.Multisig: ...

    def __init__(self,
        *,
        simple_type : typing___Optional[BTCScriptConfig.SimpleType] = None,
        multisig : typing___Optional[BTCScriptConfig.Multisig] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCScriptConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"config",u"multisig",u"simple_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",u"multisig",u"simple_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"config",b"config",u"multisig",b"multisig",u"simple_type",b"simple_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"multisig",b"multisig",u"simple_type",b"simple_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"config",b"config"]) -> typing_extensions___Literal["simple_type","multisig"]: ...

class BTCPubRequest(google___protobuf___message___Message):
    class XPubType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BTCPubRequest.XPubType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BTCPubRequest.XPubType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BTCPubRequest.XPubType]]: ...
        TPUB = typing___cast(BTCPubRequest.XPubType, 0)
        XPUB = typing___cast(BTCPubRequest.XPubType, 1)
        YPUB = typing___cast(BTCPubRequest.XPubType, 2)
        ZPUB = typing___cast(BTCPubRequest.XPubType, 3)
        VPUB = typing___cast(BTCPubRequest.XPubType, 4)
        UPUB = typing___cast(BTCPubRequest.XPubType, 5)
        CAPITAL_VPUB = typing___cast(BTCPubRequest.XPubType, 6)
        CAPITAL_ZPUB = typing___cast(BTCPubRequest.XPubType, 7)
        CAPITAL_UPUB = typing___cast(BTCPubRequest.XPubType, 8)
        CAPITAL_YPUB = typing___cast(BTCPubRequest.XPubType, 9)
    TPUB = typing___cast(BTCPubRequest.XPubType, 0)
    XPUB = typing___cast(BTCPubRequest.XPubType, 1)
    YPUB = typing___cast(BTCPubRequest.XPubType, 2)
    ZPUB = typing___cast(BTCPubRequest.XPubType, 3)
    VPUB = typing___cast(BTCPubRequest.XPubType, 4)
    UPUB = typing___cast(BTCPubRequest.XPubType, 5)
    CAPITAL_VPUB = typing___cast(BTCPubRequest.XPubType, 6)
    CAPITAL_ZPUB = typing___cast(BTCPubRequest.XPubType, 7)
    CAPITAL_UPUB = typing___cast(BTCPubRequest.XPubType, 8)
    CAPITAL_YPUB = typing___cast(BTCPubRequest.XPubType, 9)

    coin = ... # type: BTCCoin
    keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    xpub_type = ... # type: BTCPubRequest.XPubType
    display = ... # type: bool

    @property
    def script_config(self) -> BTCScriptConfig: ...

    def __init__(self,
        *,
        coin : typing___Optional[BTCCoin] = None,
        keypath : typing___Optional[typing___Iterable[int]] = None,
        xpub_type : typing___Optional[BTCPubRequest.XPubType] = None,
        script_config : typing___Optional[BTCScriptConfig] = None,
        display : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCPubRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"output",u"script_config",u"xpub_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",u"display",u"keypath",u"output",u"script_config",u"xpub_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"output",b"output",u"script_config",b"script_config",u"xpub_type",b"xpub_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",b"coin",u"display",b"display",u"keypath",b"keypath",u"output",b"output",u"script_config",b"script_config",u"xpub_type",b"xpub_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"output",b"output"]) -> typing_extensions___Literal["xpub_type","script_config"]: ...

class BTCScriptConfigWithKeypath(google___protobuf___message___Message):
    keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    @property
    def script_config(self) -> BTCScriptConfig: ...

    def __init__(self,
        *,
        script_config : typing___Optional[BTCScriptConfig] = None,
        keypath : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCScriptConfigWithKeypath: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"keypath",u"script_config"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"script_config",b"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"keypath",b"keypath",u"script_config",b"script_config"]) -> None: ...

class BTCSignInitRequest(google___protobuf___message___Message):
    coin = ... # type: BTCCoin
    version = ... # type: int
    num_inputs = ... # type: int
    num_outputs = ... # type: int
    locktime = ... # type: int

    @property
    def script_configs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[BTCScriptConfigWithKeypath]: ...

    def __init__(self,
        *,
        coin : typing___Optional[BTCCoin] = None,
        script_configs : typing___Optional[typing___Iterable[BTCScriptConfigWithKeypath]] = None,
        version : typing___Optional[int] = None,
        num_inputs : typing___Optional[int] = None,
        num_outputs : typing___Optional[int] = None,
        locktime : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSignInitRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",u"locktime",u"num_inputs",u"num_outputs",u"script_configs",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",b"coin",u"locktime",b"locktime",u"num_inputs",b"num_inputs",u"num_outputs",b"num_outputs",u"script_configs",b"script_configs",u"version",b"version"]) -> None: ...

class BTCSignNextResponse(google___protobuf___message___Message):
    class Type(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BTCSignNextResponse.Type: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BTCSignNextResponse.Type]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BTCSignNextResponse.Type]]: ...
        INPUT = typing___cast(BTCSignNextResponse.Type, 0)
        OUTPUT = typing___cast(BTCSignNextResponse.Type, 1)
        DONE = typing___cast(BTCSignNextResponse.Type, 2)
        PREVTX_INIT = typing___cast(BTCSignNextResponse.Type, 3)
        PREVTX_INPUT = typing___cast(BTCSignNextResponse.Type, 4)
        PREVTX_OUTPUT = typing___cast(BTCSignNextResponse.Type, 5)
    INPUT = typing___cast(BTCSignNextResponse.Type, 0)
    OUTPUT = typing___cast(BTCSignNextResponse.Type, 1)
    DONE = typing___cast(BTCSignNextResponse.Type, 2)
    PREVTX_INIT = typing___cast(BTCSignNextResponse.Type, 3)
    PREVTX_INPUT = typing___cast(BTCSignNextResponse.Type, 4)
    PREVTX_OUTPUT = typing___cast(BTCSignNextResponse.Type, 5)

    type = ... # type: BTCSignNextResponse.Type
    index = ... # type: int
    has_signature = ... # type: bool
    signature = ... # type: bytes
    prev_index = ... # type: int

    def __init__(self,
        *,
        type : typing___Optional[BTCSignNextResponse.Type] = None,
        index : typing___Optional[int] = None,
        has_signature : typing___Optional[bool] = None,
        signature : typing___Optional[bytes] = None,
        prev_index : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSignNextResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"has_signature",u"index",u"prev_index",u"signature",u"type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"has_signature",b"has_signature",u"index",b"index",u"prev_index",b"prev_index",u"signature",b"signature",u"type",b"type"]) -> None: ...

class BTCSignInputRequest(google___protobuf___message___Message):
    prevOutHash = ... # type: bytes
    prevOutIndex = ... # type: int
    prevOutValue = ... # type: int
    sequence = ... # type: int
    keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    script_config_index = ... # type: int

    def __init__(self,
        *,
        prevOutHash : typing___Optional[bytes] = None,
        prevOutIndex : typing___Optional[int] = None,
        prevOutValue : typing___Optional[int] = None,
        sequence : typing___Optional[int] = None,
        keypath : typing___Optional[typing___Iterable[int]] = None,
        script_config_index : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSignInputRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"keypath",u"prevOutHash",u"prevOutIndex",u"prevOutValue",u"script_config_index",u"sequence"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"keypath",b"keypath",u"prevOutHash",b"prevOutHash",u"prevOutIndex",b"prevOutIndex",u"prevOutValue",b"prevOutValue",u"script_config_index",b"script_config_index",u"sequence",b"sequence"]) -> None: ...

class BTCSignOutputRequest(google___protobuf___message___Message):
    ours = ... # type: bool
    type = ... # type: BTCOutputType
    value = ... # type: int
    hash = ... # type: bytes
    keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    script_config_index = ... # type: int

    def __init__(self,
        *,
        ours : typing___Optional[bool] = None,
        type : typing___Optional[BTCOutputType] = None,
        value : typing___Optional[int] = None,
        hash : typing___Optional[bytes] = None,
        keypath : typing___Optional[typing___Iterable[int]] = None,
        script_config_index : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSignOutputRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",u"keypath",u"ours",u"script_config_index",u"type",u"value"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",b"hash",u"keypath",b"keypath",u"ours",b"ours",u"script_config_index",b"script_config_index",u"type",b"type",u"value",b"value"]) -> None: ...

class BTCScriptConfigRegistration(google___protobuf___message___Message):
    coin = ... # type: BTCCoin
    keypath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    @property
    def script_config(self) -> BTCScriptConfig: ...

    def __init__(self,
        *,
        coin : typing___Optional[BTCCoin] = None,
        script_config : typing___Optional[BTCScriptConfig] = None,
        keypath : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCScriptConfigRegistration: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",u"keypath",u"script_config"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"script_config",b"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",b"coin",u"keypath",b"keypath",u"script_config",b"script_config"]) -> None: ...

class BTCSuccess(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSuccess: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class BTCIsScriptConfigRegisteredRequest(google___protobuf___message___Message):

    @property
    def registration(self) -> BTCScriptConfigRegistration: ...

    def __init__(self,
        *,
        registration : typing___Optional[BTCScriptConfigRegistration] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCIsScriptConfigRegisteredRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"registration"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"registration"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"registration",b"registration"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"registration",b"registration"]) -> None: ...

class BTCIsScriptConfigRegisteredResponse(google___protobuf___message___Message):
    is_registered = ... # type: bool

    def __init__(self,
        *,
        is_registered : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCIsScriptConfigRegisteredResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"is_registered"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"is_registered",b"is_registered"]) -> None: ...

class BTCRegisterScriptConfigRequest(google___protobuf___message___Message):
    class XPubType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BTCRegisterScriptConfigRequest.XPubType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BTCRegisterScriptConfigRequest.XPubType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BTCRegisterScriptConfigRequest.XPubType]]: ...
        AUTO_ELECTRUM = typing___cast(BTCRegisterScriptConfigRequest.XPubType, 0)
        AUTO_XPUB_TPUB = typing___cast(BTCRegisterScriptConfigRequest.XPubType, 1)
    AUTO_ELECTRUM = typing___cast(BTCRegisterScriptConfigRequest.XPubType, 0)
    AUTO_XPUB_TPUB = typing___cast(BTCRegisterScriptConfigRequest.XPubType, 1)

    name = ... # type: typing___Text
    xpub_type = ... # type: BTCRegisterScriptConfigRequest.XPubType

    @property
    def registration(self) -> BTCScriptConfigRegistration: ...

    def __init__(self,
        *,
        registration : typing___Optional[BTCScriptConfigRegistration] = None,
        name : typing___Optional[typing___Text] = None,
        xpub_type : typing___Optional[BTCRegisterScriptConfigRequest.XPubType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCRegisterScriptConfigRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"registration"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",u"registration",u"xpub_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"registration",b"registration"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"registration",b"registration",u"xpub_type",b"xpub_type"]) -> None: ...

class BTCPrevTxInitRequest(google___protobuf___message___Message):
    version = ... # type: int
    num_inputs = ... # type: int
    num_outputs = ... # type: int
    locktime = ... # type: int

    def __init__(self,
        *,
        version : typing___Optional[int] = None,
        num_inputs : typing___Optional[int] = None,
        num_outputs : typing___Optional[int] = None,
        locktime : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCPrevTxInitRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"locktime",u"num_inputs",u"num_outputs",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"locktime",b"locktime",u"num_inputs",b"num_inputs",u"num_outputs",b"num_outputs",u"version",b"version"]) -> None: ...

class BTCPrevTxInputRequest(google___protobuf___message___Message):
    prev_out_hash = ... # type: bytes
    prev_out_index = ... # type: int
    signature_script = ... # type: bytes
    sequence = ... # type: int

    def __init__(self,
        *,
        prev_out_hash : typing___Optional[bytes] = None,
        prev_out_index : typing___Optional[int] = None,
        signature_script : typing___Optional[bytes] = None,
        sequence : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCPrevTxInputRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"prev_out_hash",u"prev_out_index",u"sequence",u"signature_script"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"prev_out_hash",b"prev_out_hash",u"prev_out_index",b"prev_out_index",u"sequence",b"sequence",u"signature_script",b"signature_script"]) -> None: ...

class BTCPrevTxOutputRequest(google___protobuf___message___Message):
    value = ... # type: int
    pubkey_script = ... # type: bytes

    def __init__(self,
        *,
        value : typing___Optional[int] = None,
        pubkey_script : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCPrevTxOutputRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"pubkey_script",u"value"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"pubkey_script",b"pubkey_script",u"value",b"value"]) -> None: ...

class BTCSignMessageRequest(google___protobuf___message___Message):
    coin = ... # type: BTCCoin
    msg = ... # type: bytes

    @property
    def script_config(self) -> BTCScriptConfigWithKeypath: ...

    def __init__(self,
        *,
        coin : typing___Optional[BTCCoin] = None,
        script_config : typing___Optional[BTCScriptConfigWithKeypath] = None,
        msg : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSignMessageRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",u"msg",u"script_config"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"script_config",b"script_config"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"coin",b"coin",u"msg",b"msg",u"script_config",b"script_config"]) -> None: ...

class BTCSignMessageResponse(google___protobuf___message___Message):
    signature = ... # type: bytes

    def __init__(self,
        *,
        signature : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCSignMessageResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"signature"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"signature",b"signature"]) -> None: ...

class BTCRequest(google___protobuf___message___Message):

    @property
    def is_script_config_registered(self) -> BTCIsScriptConfigRegisteredRequest: ...

    @property
    def register_script_config(self) -> BTCRegisterScriptConfigRequest: ...

    @property
    def prevtx_init(self) -> BTCPrevTxInitRequest: ...

    @property
    def prevtx_input(self) -> BTCPrevTxInputRequest: ...

    @property
    def prevtx_output(self) -> BTCPrevTxOutputRequest: ...

    @property
    def sign_message(self) -> BTCSignMessageRequest: ...

    def __init__(self,
        *,
        is_script_config_registered : typing___Optional[BTCIsScriptConfigRegisteredRequest] = None,
        register_script_config : typing___Optional[BTCRegisterScriptConfigRequest] = None,
        prevtx_init : typing___Optional[BTCPrevTxInitRequest] = None,
        prevtx_input : typing___Optional[BTCPrevTxInputRequest] = None,
        prevtx_output : typing___Optional[BTCPrevTxOutputRequest] = None,
        sign_message : typing___Optional[BTCSignMessageRequest] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",u"prevtx_init",u"prevtx_input",u"prevtx_output",u"register_script_config",u"request",u"sign_message"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",u"prevtx_init",u"prevtx_input",u"prevtx_output",u"register_script_config",u"request",u"sign_message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",b"is_script_config_registered",u"prevtx_init",b"prevtx_init",u"prevtx_input",b"prevtx_input",u"prevtx_output",b"prevtx_output",u"register_script_config",b"register_script_config",u"request",b"request",u"sign_message",b"sign_message"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",b"is_script_config_registered",u"prevtx_init",b"prevtx_init",u"prevtx_input",b"prevtx_input",u"prevtx_output",b"prevtx_output",u"register_script_config",b"register_script_config",u"request",b"request",u"sign_message",b"sign_message"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"request",b"request"]) -> typing_extensions___Literal["is_script_config_registered","register_script_config","prevtx_init","prevtx_input","prevtx_output","sign_message"]: ...

class BTCResponse(google___protobuf___message___Message):

    @property
    def success(self) -> BTCSuccess: ...

    @property
    def is_script_config_registered(self) -> BTCIsScriptConfigRegisteredResponse: ...

    @property
    def sign_next(self) -> BTCSignNextResponse: ...

    @property
    def sign_message(self) -> BTCSignMessageResponse: ...

    def __init__(self,
        *,
        success : typing___Optional[BTCSuccess] = None,
        is_script_config_registered : typing___Optional[BTCIsScriptConfigRegisteredResponse] = None,
        sign_next : typing___Optional[BTCSignNextResponse] = None,
        sign_message : typing___Optional[BTCSignMessageResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BTCResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",u"response",u"sign_message",u"sign_next",u"success"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",u"response",u"sign_message",u"sign_next",u"success"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",b"is_script_config_registered",u"response",b"response",u"sign_message",b"sign_message",u"sign_next",b"sign_next",u"success",b"success"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"is_script_config_registered",b"is_script_config_registered",u"response",b"response",u"sign_message",b"sign_message",u"sign_next",b"sign_next",u"success",b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"response",b"response"]) -> typing_extensions___Literal["success","is_script_config_registered","sign_next","sign_message"]: ...
