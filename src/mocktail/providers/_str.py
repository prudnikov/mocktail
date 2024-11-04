import random
import string
from collections.abc import Generator, Iterator
from functools import cached_property
from typing import TypeAlias, Final

from faker import Faker

__all__ = [
    "StrProvider",
    "random_str",
    "Username",
    "FirstName",
    "FirstNameMale",
    "FirstNameFemale",
    "LastName",
    "FullName",
    "Country",
    "City",
    "Address",
    "Ipv4Address",
    "Ipv6Address",
]


_StrProvider: TypeAlias = Generator[str, None, None] | Iterator[str]
_StrProviderWithProbability: TypeAlias = list[tuple[float, _StrProvider]]
StrProvider: TypeAlias = _StrProvider | _StrProviderWithProbability

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


class BaseFaker:
    _locale: Final[str]

    def __init__(self, locale: str = "en_US"):
        self._locale = locale

    def __iter__(self) -> Iterator[str]:
        return self

    @cached_property
    def _faker(self) -> Faker:
        return Faker(self._locale)

    def __next__(self) -> str:
        return self._faker.name()


class Username(BaseFaker):
    def __next__(self) -> str:
        return self._faker.user_name()


class FirstName(BaseFaker):
    def __next__(self) -> str:
        return self._faker.first_name()


class FirstNameMale(BaseFaker):
    def __next__(self) -> str:
        return self._faker.first_name_male()


class FirstNameFemale(BaseFaker):
    def __next__(self) -> str:
        return self._faker.first_name_female()


class LastName(BaseFaker):
    def __next__(self) -> str:
        return self._faker.last_name()


class FullName(BaseFaker):
    def __next__(self) -> str:
        return self._faker.name()


class Country(BaseFaker):
    def __next__(self) -> str:
        return self._faker.country()


class City(BaseFaker):
    def __next__(self) -> str:
        return self._faker.city()


class Address(BaseFaker):
    def __next__(self) -> str:
        return self._faker.address()


class Ipv4Address(BaseFaker):
    def __next__(self) -> str:
        return self._faker.ipv4()


class Ipv6Address(BaseFaker):
    def __next__(self) -> str:
        return self._faker.ipv6()
