import json
from typing import Any, Collection

__all__ = ["Json", "Jsonl"]


class Json:
    def serialize(self, data: Collection[dict[str, Any]]) -> str:
        return json.dumps(data)


class Jsonl:
    def serialize(self, data: Collection[dict[str, Any]]) -> str:
        return "\n".join(json.dumps(record) for record in data)
