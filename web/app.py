from os import environ
from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncpg
from views.index import routes as routes_index


async def startup(app: web.Application):
    app["pg"] = await asyncpg.create_pool(dsn=environ["DATABASE_URL"])


async def cleanup(app: web.Application):
    await app["pg"].close()


app = web.Application()

app["static_root_url"] = environ["STATIC_ROOT_URL"]

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))

app.add_routes(routes_index)

app.on_startup.append(startup)
app.on_cleanup.append(cleanup)
