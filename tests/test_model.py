import random

import pytest

from mocktail import mocktail, providers, serializers
from mocktail.fields.int import Int
from mocktail.fields.str import Str
from mocktail.model import Model, create_fields_for_model
from mocktail.providers import single_int


class User(Model):
    id = Int(min_value=1, max_value=1000)
    username = Str()
    age: int


class ABInt:
    b: int


class ABStr:
    b: str


test_data = [(ABInt, Int), (ABStr, Str)]


@pytest.mark.parametrize("model_class, field_class", test_data)
def test_create_fields_for_model(model_class, field_class):
    fields = create_fields_for_model(model_class)
    assert len(fields) == 1
    assert "b" in fields
    assert isinstance(fields["b"], field_class)


def test_model():
    quantity = random.randint(1, 100)
    m = mocktail(User, quantity)
    assert len(m) == quantity


def test_model_inheritance():
    """hasattr and getattr was used in the original code, but it was
    not working as expected as it was using the super class attribute.
    But when we use A for the first time, A's fields are cached, and
    when we use B, it uses the cached fields of A. So, we will test
    this case in this unittest"""

    class A:
        a = Int(min_value=0, max_value=1000)

    m = mocktail(A, 1)
    assert 0 <= m[0]["a"] <= 1000

    class B(A):
        a = Int(min_value=1001, max_value=2000)

    m = mocktail(B, 1)
    assert 1001 <= m[0]["a"] <= 2000


def test_model3():
    class User2:
        username: str
        age = Int(min_value=0, max_value=120)

    m = mocktail(User2, 1)
    assert len(m) == 1


def test4():
    class User3:
        username = Str(provider=providers.Username())
        first_name = Str(provider=providers.FirstName())
        last_name = Str(provider=providers.LastName())
        age = Int(provider=providers.Age())
        city = Str(provider=providers.City())
        country = Str(provider=providers.Country())
        host = Str(provider=providers.Ipv4Address())

    print(
        mocktail(
            User3,
            5000,
            serializer=serializers.CsvFile("__mocktail_output.csv"),
        ).as_posix()
    )
    print(mocktail(User3, 5, serializer=serializers.CsvString()))


def test5():
    class User3:
        age = Int(provider=[(0.40, single_int(1)), (0.60, single_int(2))])
        name = Str(provider=providers.FullName())

    # print(mocktail(User3, 1000, serializer=serializers.CsvString()))

    data = mocktail(User3, 1000)
    print(len(list(filter(lambda x: x["age"] == 1, data))))
