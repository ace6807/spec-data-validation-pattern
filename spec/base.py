from abc import abstractmethod
from dataclasses import dataclass
from typing import Any


class Spec:
    @abstractmethod
    def passes(self, candidate: Any) -> bool:
        raise NotImplementedError()

    def __call__(self, candidate: Any) -> bool:
        return self.passes(candidate)

    def __and__(self, other: "Spec") -> "And":
        return And(self, other)

    def __or__(self, other: "Spec") -> "Or":
        return Or(self, other)

    def __neg__(self) -> "Not":
        return Not(self)


@dataclass(frozen=True)
class And(Spec):
    first: Spec
    second: Spec

    def passes(self, candidate: Any) -> bool:
        return self.first.passes(candidate) and self.second.passes(candidate)


@dataclass(frozen=True)
class Or(Spec):
    first: Spec
    second: Spec

    def passes(self, candidate: Any) -> bool:
        return self.first.passes(candidate) or self.second.passes(candidate)


@dataclass(frozen=True)
class Not(Spec):
    subject: Spec

    def passes(self, candidate: Any) -> bool:
        return not self.subject.passes(candidate)
