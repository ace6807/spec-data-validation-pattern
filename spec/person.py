from dataclasses import dataclass
from . import Spec
from dto.person import PersonDTO


@dataclass
class HasNameSpec(Spec):
    def passes(self, candidate: PersonDTO) -> bool:
        return candidate.name is not None and candidate.name != ""


@dataclass
class HasAgeSpec(Spec):
    def passes(self, candidate: PersonDTO) -> bool:
        return candidate.age is not None


@dataclass
class AgeIsLessThan(Spec):
    age: int

    def passes(self, candidate: PersonDTO) -> bool:
        return candidate.age < self.age


@dataclass
class AgeIsGreaterThan(Spec):
    age: int

    def passes(self, candidate: PersonDTO) -> bool:
        return candidate.age > self.age


@dataclass
class IsFromCountry(Spec):
    country: str

    def passes(self, candidate: PersonDTO) -> bool:
        return candidate.address.country == self.country


@dataclass
class PersonApiSpec(Spec):
    has_name_spec = HasNameSpec()
    has_age_spec = HasAgeSpec()
    age_less_than_spec = AgeIsLessThan(55)
    age_greater_than_spec = AgeIsGreaterThan(18)
    is_domestic = IsFromCountry("US")

    def passes(self, candidate: PersonDTO) -> bool:
        tests = (
            self.has_age_spec
            & self.has_name_spec
            & self.age_less_than_spec
            & self.age_greater_than_spec
            & -self.is_domestic
        )

        return tests.passes(candidate)
