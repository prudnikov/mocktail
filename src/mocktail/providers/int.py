import random
import sys
from typing import TypeAlias
from collections.abc import Generator, Iterator

__all__ = ["IntProvider", "random_int"]


IntProvider: TypeAlias = Generator[int, None, None] | Iterator[int]
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
    if not min_value:
        min_value = -1 * sys.maxsize

    if not max_value:
        max_value = sys.maxsize

    while True:
        yield random.randint(min_value, max_value)
