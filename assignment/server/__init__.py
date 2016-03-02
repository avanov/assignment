import asyncio
from typing import Any, Dict, Tuple

from aiohttp import web

from assignment.apps import probabilities
from . import db


def init_app(config: Dict[str, Any]) -> Tuple[asyncio.AbstractEventLoop, web.Application]:
    loop = asyncio.get_event_loop()
    app = web.Application()

    # Setup routes
    # ------------
    app.router.add_route("GET", "/probabilities/{attrs:.+}",
                         probabilities.handlers.handler)

    # Setup database connection pool
    # ------------------------------
    engine = loop.run_until_complete(db.setup_database(loop, config))
    setattr(app, 'dbengine', engine)
    return loop, app
