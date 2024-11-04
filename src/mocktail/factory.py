import logging
import random
from typing import ClassVar

from mocktail import serializers
from mocktail.fields.base_field import Field
from mocktail.model import create_fields_for_model

logger = logging.getLogger(__name__)


class Factory:
    _mocktail_fields_key: ClassVar = "__mocktail_fields__"
    _serializer: None | serializers.Serializer

    def __init__(self, serializer: None | serializers.Serializer):
        self._serializer = serializer

    def _get_or_create_mocktail_fields(self, model_class: type):
        # Don't use hasattr(model_class, self._mocktail_fields_key) here, it will use
        # super class attribute, which we don't want.
        if self._mocktail_fields_key in model_class.__dict__:
            # Same here, don't use getattr(model_class, self._mocktail_fields_key)
            return model_class.__dict__.get(self._mocktail_fields_key)
        else:
            fields = create_fields_for_model(model_class)
            setattr(model_class, self._mocktail_fields_key, fields)
            return fields

    def _create(self, model_class: type):
        fields = self._get_or_create_mocktail_fields(model_class)
        values = {}
        for key, val in fields.items():
            assert isinstance(val, Field)
            values[key] = val.mock()

        return values

    def make(
        self, model_class: type, quantity: int | None = None, *args, **kwargs
    ):
        if not quantity:
            # TODO: Read default quantity from the ENV var.
            #  For example MT_MAKE_DEFAULT_QUANTITY
            quantity = 1

        data = [self._create(model_class) for _ in range(quantity)]

        if self._serializer:
            return self._serializer.serialize(data)

        return data
