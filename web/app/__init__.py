from aiohttp import web
from .views.index import routes as routes_index

app = web.Application()

app.add_routes(routes_index)
