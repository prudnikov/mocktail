import random
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
        if type(self._provider) is list:
            probabilities = 0
            for probability, _ in self._provider:
                probabilities += probability

            if probabilities != 1:
                raise ValueError("The sum of the probabilities must be 1")

            pick = random.random()
            start_probability: float | None = None
            end_probability: float | None = None
            for probability, provider in self._provider:
                if start_probability is None:
                    start_probability = 0
                else:
                    start_probability = end_probability

                if end_probability is None:
                    end_probability = probability
                else:
                    end_probability += probability

                end_probability += probability
                if start_probability <= pick < end_probability:
                    return next(provider)
        else:
            return next(self._provider)

    def __repr__(self):
        return (
            f"Str(min_length={self.min_length}, max_length={self.max_length})"
        )
