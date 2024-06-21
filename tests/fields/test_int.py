import random
import sys
from collections.abc import Generator, Iterator
from unittest import mock

from mocktail.fields.int import Int


def test_int_defaults():
    f = Int()
    val = f.mock()
    assert val == f.value
    assert f.value is not None
    assert isinstance(f.value, int)
    assert Int._default_min_value <= f.value <= Int._default_max_value
    assert Int._default_min_value == f.min_value
    assert Int._default_max_value == f.max_value


def test_int_in_range() -> None:
    for _ in range(1000):
        min_value = random.randint(-sys.maxsize, sys.maxsize - 1_000)
        max_value = min_value + random.randint(0, 1_000)
        f = Int(min_value=min_value, max_value=max_value)
        f.mock()
        assert f.value >= min_value
        assert f.value <= max_value


def test_int_with_generator() -> None:
    def create_random_int_generator(
        _min_value: int, _max_value: int
    ) -> Generator[int, None, None]:
        while True:
            yield random.randint(_min_value, _max_value)

    min_value, max_value = (
        Int._default_min_value // 2,
        Int._default_max_value // 2,
    )
    test_provider = create_random_int_generator(
        min_value,
        max_value,
    )
    for _ in range(1000):
        f = Int(provider=test_provider)
        f.mock()
        assert min_value <= f.value <= max_value


def test_int_with_iterator() -> None:
    size = 10
    data_list: list[int] = [random.randint(0, 10_000) for i in range(size)]
    data: Iterator[int] = iter(data_list)

    f = Int(provider=data)
    for i in range(size):
        val = f.mock()
        assert val == data_list[i]


def test_int_generator_called() -> None:
    mock_provider = mock.Mock()
    mock_provider.__next__ = mock.Mock()
    f = Int(provider=mock_provider)
    f.mock()
    mock_provider.__next__.assert_called_once()
