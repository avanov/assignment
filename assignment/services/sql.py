from typing import List

from aiohttp import web
from sqlalchemy import Table

from ..server.entities import BaseEntity


class SQLService:

    def __init__(self, app: web.Application, table: Table, entity: BaseEntity):
        self.app = app
        self.engine = app.dbengine  # type: aiopg.sa.Engine
        self.table = table
        self.entity = entity

    async def get_many(self,
                 limit: int = 100,
                 offset: int = 0) -> List[BaseEntity]:
        query = self.table.select('1')
        async with self.engine.acquire() as c:
            rv = await c.execute(query)
        return []
