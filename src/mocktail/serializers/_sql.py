from typing import Any, Collection, Final

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.expression import values

__all__ = ["SqlCte"]


class SqlCte:
    _model_name: Final[str]

    def __init__(self, model_name: str):
        self._model_name = model_name

    def serialize(self, data: Collection[dict[str, Any]]) -> str:

        # column_names = data[0].keys()
        rows = [tuple(row.values()) for row in data]
        mock_data = values(
            sa.column("username", sa.String),
            sa.column("first_name", sa.String),
            sa.column("last_name", sa.String),
            sa.column("age", sa.Integer),
        ).data(rows)

        mock_data_cte = sa.select(mock_data).cte(self._model_name)

        query = sa.select(mock_data_cte)

        return str(
            query.compile(
                dialect=postgresql.dialect(),
                compile_kwargs={"literal_binds": True},
            )
        )
