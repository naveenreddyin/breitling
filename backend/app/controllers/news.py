import httpx


from configuration.common import Configuration

from blacksheep.server.controllers import Controller, get
from blacksheep import json

from app import resolve_error


class News(Controller):
    @get("/api/news/")
    async def index(self, configuration: Configuration):
        async with httpx.AsyncClient() as client:
            try:
                url = f"{configuration.news_api_url}?country=us&apiKey={configuration.news_api_key}"
                news_api_response = await client.get(url)
            except httpx.ConnectError as ex:
                return json(
                    {"status": "Connection with remote could not be established."},
                    status=500,
                )
            except httpx.TimeoutException as ex:
                return json(
                    {"status": "Connection timedout."},
                    status=500,
                )
        if news_api_response.status_code == 200:
            response = json(
                {
                    "status": news_api_response.json().get("status"),
                    "count": news_api_response.json().get("totalResults"),
                    "articles": news_api_response.json().get("articles"),
                },
                status=200,
            )
        else:
            response = json(
                {
                    "status": news_api_response.json().get("status"),
                    "details": await resolve_error(
                        news_api_response.json().get("code"),
                    ),
                },
                status=400,
            )
        return response
