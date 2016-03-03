import logging
from typing import List

from aiohttp import web

from assignment.server import responses
from .entities import Trait
from .services import ProbabilitiesService, TraitsService


log = logging.getLogger(__name__)


async def handler(request: web.Request) -> web.Response:
    """ Return probabilities of people matching given traits.
    """
    traits = [x.strip() for x in request.match_info['attrs'].split('/') if x.strip()]
    traits_srv = TraitsService(request.app)
    service = ProbabilitiesService(request.app)
    traits = await traits_srv.get_many(traits_srv.t.c.name, traits)  # type: List[Trait]
    people = await service.get_matching(traits)
    tset = set([t.id for t in traits])
    tset_len = len(tset)
    people_probability = [
        {
            'type': 'person',
            'id': p.id,
            'attributes':  {
                'name': p.name,
                'probability': len(tset & set(p.traits)) / tset_len * 0.8,
            }
        }
        for p in people
    ]
    people_probability.sort(key=lambda x: x['attributes']['probability'], reverse=True)
    return responses.ok(people_probability)
