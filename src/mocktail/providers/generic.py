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


def single_int(value: int) -> Generator[int, None, None]:
    while True:
        yield value


def random_range_int(start: int, end: int) -> Generator[int, None, None]:
    while True:
        yield random.randint(start, end)
