import pathlib
from typing import Protocol, Collection, Any


class Serializer(Protocol):
    def serialize(
        self, data: Collection[dict[str, Any]]
    ) -> str | pathlib.Path:
        ...
