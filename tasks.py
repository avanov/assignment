from invoke import task, run


@task
def serve():
    run('python -m aiohttp.web -H localhost -P 8000 assignment:init_app')
