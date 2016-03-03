import logging
from typing import Set, List

from aiohttp import web
from sqlalchemy.sql.expression import select, text

from assignment.services.sql import SQLService
from assignment.server.schemas import PeopleTbl, TraitsTbl
from .entities import Person, Trait
from .values import Probability


log = logging.getLogger(__name__)


class ProbabilitiesService(SQLService):
    def __init__(self, app: web.Application):
        super(ProbabilitiesService, self).__init__(app, PeopleTbl, Person)
        self.traits_srv = TraitsService(app)

    async def get_matching(self, traits: List[str]) -> List[Probability]:
        if not traits:
            return []

        weight_step = .1 / len(traits) + 1
        weights = {t: 1 * weight_step for t in traits}

        traits = await self.traits_srv.get_many(self.traits_srv.t.c.name, traits)  # type: List[Trait]
        if not traits:
            return []

        trait_weights = {t.id: weights[t.name] for t in traits}

        trait_ids = [t.id for t in traits]
        query = select(self.columns()).where(
            text("{} && :trait_ids".format(self.t.c.traits.key))
        )
        async with self.engine.acquire() as c:
            csr = await c.execute(query, trait_ids=trait_ids)
            result = await csr.fetchall()
            entity = self.e

            tset = set(trait_ids)
            tset_len = len(tset)
            rv = []
            for record in result:
                person = entity(**record)
                probability = 0.8
                intersects = tset & set(person.traits)
                for t_id in intersects:
                    probability *= trait_weights[t_id]
                probability = len(intersects) / tset_len * probability

                rv.append(Probability(person=person,
                                      probability=probability))
            return rv


class TraitsService(SQLService):
    def __init__(self, app: web.Application):
        super(TraitsService, self).__init__(app, TraitsTbl, Trait)
