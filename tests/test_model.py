import random

import pytest

from mocktail import mocktail
from mocktail.fields.int import Int
from mocktail.fields.str import Str
from mocktail.model import Model, create_fields_for_model


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
