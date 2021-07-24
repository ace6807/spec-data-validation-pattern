from copy import deepcopy
from dataclasses import dataclass
from . import DataTransportObject


@dataclass
class AddressDTO(DataTransportObject):
    street: str
    state: str
    country: str
    zip: int


@dataclass
class PersonDTO(DataTransportObject):
    name: str
    age: int
    address: AddressDTO

    @classmethod
    def from_api_dict(cls, data: dict) -> "PersonDTO":
        data_copy = deepcopy(data)
        data_copy["address"] = AddressDTO.from_dict(data_copy.pop("address"))
        return cls.from_dict(data_copy)
