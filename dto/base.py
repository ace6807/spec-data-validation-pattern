from dataclasses import dataclass, fields
from typing import TypeVar, Type


T = TypeVar("T")


@dataclass
class DataTransportObject:
    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T:
        field_names = {field.name for field in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in field_names})  # type: ignore
