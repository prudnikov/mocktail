import sys
from typing import ClassVar

from mocktail.providers import IntProvider, random_int
from .base_field import Field

__all__ = ["Int", "PositiveInt", "NegativeInt"]


class Int(Field[int]):
    _default_min_value: ClassVar[int] = -sys.maxsize
    _default_max_value: ClassVar[int] = sys.maxsize
    min_value: int
    max_value: int
    _provider: IntProvider | None = None

    def __init__(
        self,
        min_value: int | None = None,
        max_value: int | None = None,
        provider: IntProvider | None = None,
    ):
        self.min_value = min_value or self._default_min_value
        self.max_value = max_value or self._default_max_value
        self._provider = provider or random_int(self.min_value, self.max_value)

    def mock(self) -> int:
        self.value = next(self._provider)
        return self.value


class PositiveInt(Int):
    _default_min_value: ClassVar[int] = 0


class NegativeInt(Int):
    _default_max_value: ClassVar[int] = 0
