from typing import Set, List

from aiohttp import web
from sqlalchemy.sql.expression import select, text

from assignment.services.sql import SQLService
from assignment.server.schemas import PeopleTbl, TraitsTbl
from .entities import Person, Trait


class ProbabilitiesService(SQLService):
    def __init__(self, app: web.Application):
        super(ProbabilitiesService, self).__init__(app, PeopleTbl, Person)

    async def get_matching(self, traits: List[Trait]) -> List[Person]:
        if not traits:
            return []
        trait_ids = [t.id for t in traits]
        query = select(self.columns()).where(
            text("{} && :trait_ids".format(self.t.c.traits.key))
        )
        async with self.engine.acquire() as c:
            csr = await c.execute(query, trait_ids=trait_ids)
            result = await csr.fetchall()
            entity = self.e
            return [entity(**record) for record in result]


class TraitsService(SQLService):
    def __init__(self, app: web.Application):
        super(TraitsService, self).__init__(app, TraitsTbl, Trait)
