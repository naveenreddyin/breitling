from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

docs = OpenAPIHandler(info=Info(title="News API", version="0.0.1"))

# include only endpoints whose path starts with "/api/"
docs.include = lambda path, _: path.startswith("/api/")
