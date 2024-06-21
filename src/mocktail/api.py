import typing
from typing import Protocol


class Model(Mockable[typing.Any]):
    pass


mocktail.mock(Model, quantity=2)


model.mock()
model.field.mock()
