import random
from collections.abc import Generator, Sequence
from typing import TypeVar

T = TypeVar("T")


def random_choice(choices: Sequence[T]) -> Generator[T, None, None]:
    while True:
        yield random.choice(choices)


def sequence(options: Sequence[T]) -> Generator[T, None, None]:
    for item in options:
        yield item