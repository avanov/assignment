import json
from typing import Optional, Any, List, Dict
from aiohttp import web


def ok(data: Optional[Dict[str, Any]] = None) -> web.Response:
    if data is None:
        data = {}
    return _response(200, data)

def _response(status: int, data: Dict[str, Any]) -> web.Response:
    return web.Response(status=status, text=json.dumps(data))
