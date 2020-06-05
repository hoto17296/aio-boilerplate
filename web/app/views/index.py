from logging import getLogger
from aiohttp import web
from aiohttp_jinja2 import template

logger = getLogger(__name__)

routes = web.RouteTableDef()


@routes.get("/", name="index")
@template("index.jinja")
async def index(request):
    return {}
