from typing import List
from aiohttp import web

from assignment.apps import probabilities


def init_app(args: List[str]) -> web.Application:
    app = web.Application()
    app.router.add_route("GET", "/probabilities/{attrs:[.+]}",
                         probabilities.handlers.handler)
    return app
