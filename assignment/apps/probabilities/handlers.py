import logging

from aiohttp import web

from assignment.server import responses
from .services import ProbabilitiesService


log = logging.getLogger(__name__)


async def handler(request: web.Request) -> web.Response:
    """ Return probabilities of people matching given traits.
    """
    traits = [x.strip() for x in request.match_info['attrs'].split('/') if x.strip()]
    probability_srv = ProbabilitiesService(request.app)
    matches = await probability_srv.get_matching(traits)

    people_probability = [
        {
            'type': 'person',
            'id': m.person.id,
            'attributes':  {
                'name': m.person.name,
                'probability': m.probability,
            }
        }
        for m in matches
    ]
    people_probability.sort(key=lambda x: x['attributes']['probability'], reverse=True)
    return responses.ok(people_probability)
