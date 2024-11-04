import pathlib
from collections.abc import Collection
from typing import Any

from mocktail import serializers
from mocktail.factory import Factory


def mocktail(
    model_class: type,
    quantity: int,
    serializer: serializers.Serializer | None = None,
) -> Collection[dict[str, Any]] | str | pathlib.Path:
    """Generate list of dictionaries.

    Return type of str and pathlib.Path is not supported yet, but it is
    intended for serializer outputs. For example if we use serializers.JsonlFile,
    the output would be the path to the created file in the filsystem.
    """
    return Factory(serializer=serializer).make(model_class, quantity=quantity)
