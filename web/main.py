from os import getenv
import logging

logging.basicConfig(level=getenv("LOG_LEVEL", logging.WARNING))

import uvloop
from aiohttp import web
from app import app

if __name__ == "__main__":
    uvloop.install()
    web.run_app(app)
