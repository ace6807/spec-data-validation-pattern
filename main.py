from spec.person import PersonApiSpec
from dto.person import PersonDTO
from api.person import PersonAPI


if __name__ == "__main__":
    person_client = PersonAPI()
    person_dto = PersonDTO.from_api_dict(person_client.get_person())

    print(person_dto.age)
    print(person_dto.name)
    print(person_dto.address.country)

    spec = PersonApiSpec()
    is_valid = spec.passes(person_dto)

    print(f"Is valid: {is_valid}")
