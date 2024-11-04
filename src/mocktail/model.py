import builtins
import inspect
import logging
import sys

from mocktail.fields.base_field import Field
from mocktail.fields.int import Int
from mocktail.fields.str import Str


logger = logging.getLogger(__name__)


def create_fields_for_model(model: type):
    # Fields defined directly on model
    logger.debug("Model class %s", model)

    _fields1 = {}
    for key, val in model.__dict__.items():
        if isinstance(val, Field):
            _fields1[key] = val
    logger.debug("Fields defined directly on model %s", _fields1)

    # Create fields from annotated fields
    _fields2 = {}
    for key, val in inspect.get_annotations(model).items():
        match val:
            case builtins.int:
                _fields2[key] = Int()
            case builtins.str:
                _fields2[key] = Str()
            case _:
                logger.warning(
                    f"{key} has unknown type {val}. This field will be ignored."
                )

    logger.debug("Fields defined as annotations on model %s", _fields2)

    return {**_fields1, **_fields2}


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
