import random
from collections.abc import Generator, Iterator
from unittest import mock

from mocktail.fields.int import Int
from mocktail.fields.str import Str


def test_str_defaults():
    f = Str()
    f.mock()
    assert f.value is not None
    assert isinstance(f.value, str)


def test_str_with_generator() -> None:
    values = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
    ]

    def create_str_generator(
        _values: list[str],
    ) -> Generator[str, None, None]:
        while True:
            yield random.choice(_values)

    test_provider = create_str_generator(values)
    for _ in range(1000):
        f = Str(provider=test_provider)
        f.mock()
        assert f.value in values


def test_str_with_iterator() -> None:
    size = 10
    data_list: list[str] = [
        f"str_{random.randint(0, 10_000)}" for i in range(size)
    ]
    data: Iterator[str] = iter(data_list)

    f = Str(provider=data)
    for i in range(size):
        val = f.mock()
        assert val == data_list[i]


def test_str_generator_called() -> None:
    mock_provider = mock.Mock()
    mock_provider.__next__ = mock.Mock()
    f = Int(provider=mock_provider)
    f.mock()
    mock_provider.__next__.assert_called_once()
