from typing import Set

from aiohttp import web

from assignment.services.sql import SQLService
from assignment.server.schemas import PeopleTbl, TraitsTbl
from .entities import Person


class ProbabilitiesService(SQLService):
    def __init__(self, app: web.Application):
        super(ProbabilitiesService, self).__init__(app, PeopleTbl, Person)

    async def get_intersection(self, traits: Set[str]):
        pass