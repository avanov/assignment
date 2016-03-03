from aiohttp import web

from assignment.server import responses
from .services import ProbabilitiesService


async def handler(request: web.Request) -> web.Response:
    traits = set([x.strip() for x in request.match_info['attrs'].split('/') if x.strip()])
    service = ProbabilitiesService(request.app)
    people = await service.get_intersection(traits)

    return responses.ok({'people': [p.to_dict() for p in people]})
