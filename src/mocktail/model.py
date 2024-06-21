import builtins
import inspect
from inspect import isclass

from mocktail import fields
from mocktail.fields.base_field import Field
from mocktail.fields.int import Int
from mocktail.fields.str import Str


def create_fields_for_model(model: type):
    _fields = {}
    # Fields defined directly on model
    for key, val in model.__dict__.items():
        if isinstance(val, Field):
            _fields[key] = val

    # Create fields from annotated fields
    for key, val in inspect.get_annotations(model).items():
        match val:
            case builtins.int:
                _fields[key] = Int()
            case builtins.str:
                _fields[key] = Str()
            case _:
                print(f"{key} type is unknown")

    return _fields


class ModelMetaclass(type):
    # def __new__(cls, *args, **kwargs):
    #     print("NEW METACLASS")
    #     return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        _fields = create_fields_for_model(self)
        self.__fields = _fields
        self._mocktail_fields = _fields
        self.mocktail_fields = _fields


class Model(metaclass=ModelMetaclass):
    def __new__(cls, *args, **kwargs):
        # print("NEW MODEL")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        # print("INIT MODEL", self)
        super().__init__()


if __name__ == "__main__":

    class User(Model):
        id = Int(min_value=1, max_value=1000)
        nammme: str

    # m = mocktail.mocktail(User, 10)

    # m = Factory().make(User, quantity=10)
    print("----2")
    print(f"User class: {User}")
    print("Creating User() instance")
    # u = User()

    # assert isinstance(u, User)
    # assert isinstance(m, list)
    # assert len(m) == 10
    # for mm in m:
    #     assert mm is not None
