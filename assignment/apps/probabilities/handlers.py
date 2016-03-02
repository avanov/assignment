from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    attrs = request.match_info['attrs'].strip().strip('/').split('/')

    return web.Response(text=str(attrs))
