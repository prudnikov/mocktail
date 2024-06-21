import abc
import typing
from abc import abstractmethod


class FieldMetaclass(type):
    pass


T = typing.TypeVar("T")


class Mockable(typing.Protocol[T]):
    def mock(self) -> T:
        ...


class Field(abc.ABC, Mockable[T]):
    value: T

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

    def __set_name__(self, owner, name):
        self.private_name = "__" + name

    @abstractmethod
    def mock(self) -> T:
        ...
