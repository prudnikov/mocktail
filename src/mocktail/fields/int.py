import logging
import random
import sys
from typing import ClassVar

from mocktail.providers import IntProvider, random_int
from .base_field import Field

__all__ = ["Int", "PositiveInt", "NegativeInt"]


logger = logging.getLogger(__name__)


class Int(Field[int]):
    _default_min_value: ClassVar[int] = -sys.maxsize
    _default_max_value: ClassVar[int] = sys.maxsize
    min_value: int
    max_value: int
    _provider: IntProvider

    def __init__(
        self,
        min_value: int | None = None,
        max_value: int | None = None,
        provider: IntProvider | None = None,
    ):
        self.min_value = (
            min_value if min_value is not None else self._default_min_value
        )
        self.max_value = (
            max_value if max_value is not None else self._default_max_value
        )
        self._provider = provider or random_int(self.min_value, self.max_value)

    def mock(self) -> int:
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
            logger.debug("--------1")
            for probability, provider in self._provider:
                if start_probability is None:
                    start_probability = 0
                else:
                    start_probability = end_probability

                if end_probability is None:
                    end_probability = probability
                else:
                    end_probability += probability

                logging.debug(
                    f"{start_probability=}, {end_probability=}, {pick=}"
                )

                if start_probability <= pick < end_probability:
                    return next(provider)
            return next(self._provider)
        else:
            return next(self._provider)

    def __repr__(self) -> str:
        return f"Int(min_value={self.min_value}, max_value={self.max_value})"


class PositiveInt(Int):
    _default_min_value: ClassVar[int] = 0


class NegativeInt(Int):
    _default_max_value: ClassVar[int] = 0
