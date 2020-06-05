from os import environ
from aiohttp import web
import aiohttp_jinja2
import jinja2
from .views.index import routes as routes_index

app = web.Application()

app["static_root_url"] = environ["STATIC_ROOT_URL"]

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))

app.add_routes(routes_index)
