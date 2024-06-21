import random
import string
from typing import TypeAlias
from collections.abc import Generator, Iterator

__all__ = ["StrProvider", "random_str"]


StrProvider: TypeAlias = Generator[str, None, None] | Iterator[str]
# try:
#     from typing import TypeAlias
#
#     IntProvider: TypeAlias = Generator[int, None, None]
# except ImportError:
#
#     # TypeAlias is deprecated in Python 3.10, this block is for compatibility on newer versions of Python
#     type IntProvider = Generator[int, None, None]


def random_str(
    length: int | None, min_length: int | None = None
) -> StrProvider:
    """

    Args:
        length: length of the string. If min_length is provided it will
        generate string of length from `min_length` to `length`
        min_length: Minimal length of the string

    Returns:

    """
    if length is not None and min_length is not None and length < min_length:
        raise ValueError(
            "The `min_length` value must be lower that the `length` value"
        )

    if not length:
        length = 10

    if min_length is not None:
        length = random.randint(min_length, length)

    while True:
        yield "".join(
            [random.choice(string.ascii_letters) for _ in range(length)]
        )
