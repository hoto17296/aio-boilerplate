from logging import getLogger
from aiohttp import web

logger = getLogger(__name__)

routes = web.RouteTableDef()


@routes.get("/", name="index")
async def index(request):
    return web.Response(text="ok")
