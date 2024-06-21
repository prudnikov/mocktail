from typing import ClassVar

from mocktail.providers import StrProvider, random_str
from .base_field import Field


class Str(Field[int]):
    # TODO: Read defaults from the ENV vars
    _default_min_length: ClassVar[int] = 10
    _default_max_length: ClassVar[int] = 20
    min_length: int
    max_length: int
    _provider: StrProvider | None = None

    def __init__(
        self,
        min_length: int | None = None,
        max_length: int | None = None,
        provider: StrProvider | None = None,
    ):
        self.min_length = min_length or self._default_min_length
        self.max_length = max_length or self._default_max_length
        self._provider = provider or random_str(10)

    def mock(self) -> str:
        self.value = self.provide_value()
        return self.value

    def provide_value(self):
        return next(self._provider)
