import csv
import json
import pathlib
import tempfile
import typing
from io import StringIO, FileIO
from os import supports_effective_ids
from typing import Any, Collection, Final
from ._serializer import Serializer

__all__ = ["CsvString", "CsvFile"]

T = typing.TypeVar("T")


class SupportsWrite(typing.Protocol[T]):
    def write(self, __s: str) -> T:
        ...


class Csv(Serializer):
    _delimiter: Final[str]
    _header: Final[bool]
    _fieldnames: Collection[str]

    def __init__(self, delimiter: str = ",", header: bool = True) -> None:
        self._delimiter = delimiter
        self._header = header

    def get_writer(self, output: SupportsWrite[str]) -> csv.DictWriter:
        return csv.DictWriter(
            output,
            fieldnames=self._fieldnames,
            quoting=csv.QUOTE_NONNUMERIC,
            delimiter=self._delimiter,
        )


class CsvString(Csv):
    def serialize(self, data: list[dict[str, Any]]) -> str:
        if not data:
            return ""

        self._fieldnames = data[0].keys()

        output = StringIO()
        writer = self.get_writer(output)

        if self._header:
            writer.writeheader()

        writer.writerows(data)

        return output.getvalue()


class CsvFile(Csv):
    _output_file_path: typing.Final[pathlib.Path]

    def __init__(
        self,
        output_file_path: pathlib.Path | str | None = None,
        delimiter: str = ",",
        header: bool = True,
    ) -> None:
        super().__init__(delimiter=delimiter, header=header)

        if output_file_path is None:
            self._output_file_path = pathlib.Path(
                tempfile.NamedTemporaryFile(delete=False).name
            )
        elif type(output_file_path) is str:
            self._output_file_path = pathlib.Path(output_file_path)
        elif isinstance(output_file_path, pathlib.Path):
            self._output_file_path = output_file_path
        else:
            raise ValueError(
                f"`output_file_path` must be a string, pathlib.Path or None. "
                f"Got {type(output_file_path)}."
            )

    def serialize(self, data: list[dict[str, Any]]) -> pathlib.Path:
        if not data:
            raise ValueError("Data is empty")

        self._fieldnames = data[0].keys()

        with self._output_file_path.open("w") as f:
            writer = self.get_writer(f)

            if self._header:
                writer.writeheader()

            writer.writerows(data)

        return self._output_file_path
