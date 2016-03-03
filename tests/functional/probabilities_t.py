import pytest
from aiohttp import ClientSession


@pytest.mark.run_loop
async def test_probabilities_endpoint(create_server, loop):
    app, app_url = await create_server()
    with ClientSession(loop=loop) as s:
        # Test empty traits
        r = await s.get(app_url + '/probabilities')
        async with r:
            assert r.status == 404

        # Test multiple empty traits
        r = await s.get(app_url + '/probabilities/ //   //')
        async with r:
            assert r.status == 200
            data = (await r.json())['data']
            assert data == []

        # Test existing traits
        r = await s.get(app_url + '/probabilities/american/politician')
        async with r:
            assert r.status == 200
            data = (await r.json())['data']
            assert len(data)
