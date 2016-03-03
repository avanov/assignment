import asyncio
import argparse
import logging
import logging.config
from pathlib import Path
import sys
from typing import Any, List, Dict

import yaml

from assignment.server import init_app


def main() -> None:
    config = parse_app_config(sys.argv[1:])

    logging.config.dictConfig(config['logging'])
    log = logging.getLogger('assignment')

    loop = asyncio.get_event_loop()
    loop.set_debug(enabled=config['debug'])

    app = loop.run_until_complete(init_app(loop, config))
    handler = app.make_handler()
    f = loop.create_server(handler, config['server']['host'], config['server']['port'])
    srv = loop.run_until_complete(f)
    log.debug('Serving on {}'.format(srv.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        log.debug('[SIGINT] Shutting down the server gracefully...')
    finally:
        # Close database pool (could be implemented better with signals)
        if hasattr(app, 'dbengine'):
            log.debug('Closing database connections...')
            app.dbengine.terminate()
            loop.run_until_complete(app.dbengine.wait_closed())

        # all the rest
        srv.close()
        loop.run_until_complete(srv.wait_closed())
        loop.run_until_complete(app.shutdown())
        loop.run_until_complete(handler.finish_connections(60.0))
        loop.run_until_complete(app.cleanup())

    loop.close()
    log.debug('Done.')
    sys.exit(0)


def parse_app_config(argv: List[str]) -> Dict[str, Any]:
    p = argparse.ArgumentParser()
    p.add_argument("config", help="path to a YAML config.")
    args = p.parse_args(argv)
    with Path(args.config).open() as f:
        config = yaml.load(f.read())
    return config
