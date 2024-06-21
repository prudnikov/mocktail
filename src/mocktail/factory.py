import random

from mocktail.fields.base_field import Field


class Factory:
    def _create(self, model_class: type):
        print("----------111")
        fields = getattr(model_class, "_mocktail_fields")
        values = {}
        for key, val in fields.items():
            assert isinstance(val, Field)
            values[key] = val.mock()

        return values

    def make(
        self, model_class: type, quantity: int | None = None, *args, **kwargs
    ):
        if not quantity:
            quantity = random.randint(1, 100)

        return [self._create(model_class) for _ in range(quantity)]
