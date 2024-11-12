import random
import sys
from collections.abc import Generator, Iterator
from typing import TypeAlias, ClassVar

__all__ = ["IntProvider", "random_int", "Age"]


_IntProvider: TypeAlias = Generator[int, None, None] | Iterator[int]
_IntProviderWithProbability: TypeAlias = list[tuple[float, _IntProvider]]
IntProvider: TypeAlias = _IntProvider | _IntProviderWithProbability


# try:
#     from typing import TypeAlias
#
#     IntProvider: TypeAlias = Generator[int, None, None]
# except ImportError:
#
#     # TypeAlias is deprecated in Python 3.10, this block is for compatibility on newer versions of Python
#     type IntProvider = Generator[int, None, None]


def random_int(
    min_value: int | None = None, max_value: int | None = None
) -> IntProvider:
    if min_value is None:
        min_value = -1 * sys.maxsize

    if max_value is None:
        max_value = sys.maxsize

    while True:
        yield random.randint(min_value, max_value)


class Age:
    _min: ClassVar[int] = 0
    _max: ClassVar[int] = 100

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        return random.randint(self._min, self._max)
