from invoke import task, run


@task
def serve():
    run('runme ./config.yml')
