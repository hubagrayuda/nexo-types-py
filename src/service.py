from enum import StrEnum
from typing import Sequence, TypeVar


ServiceKeyT = TypeVar("ServiceKeyT", bound=StrEnum)
OptServiceKeyT = TypeVar("OptServiceKeyT", bound=StrEnum | None)
ServiceKeysT = TypeVar("ServiceKeysT", bound=Sequence[StrEnum])
OptServiceKeysT = TypeVar("OptServiceKeysT", bound=Sequence[StrEnum] | None)

ServiceNameT = TypeVar("ServiceNameT", bound=StrEnum)
OptServiceNameT = TypeVar("OptServiceNameT", bound=StrEnum | None)
ServiceNamesT = TypeVar("ServiceNamesT", bound=Sequence[StrEnum])
OptServiceNamesT = TypeVar("OptServiceNamesT", bound=Sequence[StrEnum] | None)
