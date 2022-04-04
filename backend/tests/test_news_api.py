from typing import Any

import pytest
import httpx

from configuration.common import Configuration

from blacksheep.contents import Content
from blacksheep.testing import TestClient


@pytest.mark.asyncio
async def test_to_see_if_route_for_news_exists(
    test_client: TestClient,
    test_configuration: Configuration,
    httpx_mock,
) -> None:
    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json={"status": "ok"},
    )
    async with httpx.AsyncClient() as client:
        response = await test_client.get(f"/api/news/")
        assert response.status == 200


@pytest.mark.asyncio
async def test_when_api_works(
    test_client: TestClient,
    test_configuration: Configuration,
    httpx_mock,
) -> None:
    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json={
            "status": "ok",
            "totalResults": 5,
            "articles": [
                {
                    "source": {"id": None, "name": "New York Times"},
                    "author": None,
                    "title": "Latest Ukraine-Russia War News: Live Updates - The New York Times",
                    "description": "Follow Live Coverage of Ukraine",
                    "url": "https://www.nytimes.com/interactive/2022/world/ukraine-live.html",
                    "urlToImage": "https://static01.nyt.com/newsgraphics/images/icons/defaultPromoCrop.png",
                    "publishedAt": "2022-04-02T18:04:09Z",
                    "content": None,
                },
                {
                    "source": {
                        "id": "the-wall-street-journal",
                        "name": "The Wall Street Journal",
                    },
                    "author": "Isabel Coles",
                    "title": "Ukrainians Count Dead, Assess Damage After Russian Pullback Near Kyiv - The Wall Street Journal",
                    "description": "Ukrainian forces were clearing mines and counting the dead around Kyiv following Russian troop withdrawals in recent days, as Moscow shifted military operations to the country’s east.",
                    "url": "https://www.wsj.com/articles/ukrainians-count-dead-assess-damage-after-russian-pullback-near-kyiv-11648895002",
                    "urlToImage": "https://images.wsj.net/im-517349/social",
                    "publishedAt": "2022-04-02T17:59:00Z",
                    "content": "LVIV, UkraineUkrainian forces were clearing mines and counting the dead around Kyiv on Saturday following Russian troop withdrawals in recent days, as Moscow shifted military operations to the countr… [+201 chars]",
                },
                {
                    "source": {"id": "reuters", "name": "Reuters"},
                    "author": None,
                    "title": "Ukraine forces retake areas north of Kyiv as Russians look eastward - Reuters",
                    "description": "Ukrainian forces were advancing on Saturday into areas north of Kyiv littered with debris and destroyed Russian tanks as Ukrainian President Volodymyr Zelenskiy accused departing Russian soldiers of leaving behind mines.",
                    "url": "https://www.reuters.com/world/europe/red-cross-heads-again-mariupol-russia-shifts-ukraine-focus-2022-04-02/",
                    "urlToImage": "https://www.reuters.com/resizer/pgk7uBTd6L8iRt6Go30MfBjIP2w=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/BHDHBKVGINN2FGF7YZTEJERFYA.jpg",
                    "publishedAt": "2022-04-02T17:42:00Z",
                    "content": "ZAPORIZHZHIA, Ukraine, April 2 (Reuters) - Ukrainian forces were advancing on Saturday into areas north of Kyiv littered with debris and destroyed Russian tanks as Ukrainian President Volodymyr Zelen… [+6189 chars]",
                },
                {
                    "source": {"id": None, "name": "ESPN"},
                    "author": "Mike Reiss",
                    "title": "Source - New England Patriots acquire WR DeVante Parker in trade with Miami Dolphins - ESPN",
                    "description": "The Patriots have acquired WR DeVante Parker and a 2022 fifth-round draft pick from the Dolphins in exchange for a 2023 third-round pick, a source told ESPN.",
                    "url": "https://www.espn.com/nfl/story/_/id/33654533/source-new-england-patriots-acquire-wr-devante-parker-trade-miami-dolphins",
                    "urlToImage": "https://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2019%2F1222%2Fr644759_1296x729_16%2D9.jpg",
                    "publishedAt": "2022-04-02T17:19:10Z",
                    "content": "FOXBOROUGH, Mass. -- In a rare trade between AFC East rivals, the New England Patriots have acquired Miami Dolphins wide receiver DeVante Parker and a 2022 fifth-round draft pick in exchange for a 20… [+2607 chars]",
                },
                {
                    "source": {"id": None, "name": "Electrek"},
                    "author": None,
                    "title": "Tesla beats all-time delivery record with 310,000 EVs despite difficult quarter - Electrek.co",
                    "description": "Tesla released its Q1 2022 delivery and production results today and confirmed just over 310,000 deliveries, which is a new all-time delivery record despite a difficult quarter for several reasons. Due to supply chain issues and 2 separate shutdowns at Gigafa…",
                    "url": "https://electrek.co/2022/04/02/tesla-tsla-beats-all-time-delivery-record-q1-2022/",
                    "urlToImage": "https://i0.wp.com/electrek.co/wp-content/uploads/sites/3/2021/12/Tesla-all-casrs-hero.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1",
                    "publishedAt": "2022-04-02T17:12:00Z",
                    "content": "Tesla released its Q1 2022 delivery and production results today and confirmed just over 310,000 deliveries, which is a new all-time delivery record despite a difficult quarter for several reasons.\r\n… [+2575 chars]",
                },
            ],
        },
    )
    async with httpx.AsyncClient() as client:
        response = await test_client.get(f"/api/news/")
        assert response.status == 200
        assert await response.json() == {
            "status": "ok",
            "count": 5,
            "articles": [
                {
                    "source": {"id": None, "name": "New York Times"},
                    "author": None,
                    "title": "Latest Ukraine-Russia War News: Live Updates - The New York Times",
                    "description": "Follow Live Coverage of Ukraine",
                    "url": "https://www.nytimes.com/interactive/2022/world/ukraine-live.html",
                    "urlToImage": "https://static01.nyt.com/newsgraphics/images/icons/defaultPromoCrop.png",
                    "publishedAt": "2022-04-02T18:04:09Z",
                    "content": None,
                },
                {
                    "source": {
                        "id": "the-wall-street-journal",
                        "name": "The Wall Street Journal",
                    },
                    "author": "Isabel Coles",
                    "title": "Ukrainians Count Dead, Assess Damage After Russian Pullback Near Kyiv - The Wall Street Journal",
                    "description": "Ukrainian forces were clearing mines and counting the dead around Kyiv following Russian troop withdrawals in recent days, as Moscow shifted military operations to the country’s east.",
                    "url": "https://www.wsj.com/articles/ukrainians-count-dead-assess-damage-after-russian-pullback-near-kyiv-11648895002",
                    "urlToImage": "https://images.wsj.net/im-517349/social",
                    "publishedAt": "2022-04-02T17:59:00Z",
                    "content": "LVIV, UkraineUkrainian forces were clearing mines and counting the dead around Kyiv on Saturday following Russian troop withdrawals in recent days, as Moscow shifted military operations to the countr… [+201 chars]",
                },
                {
                    "source": {"id": "reuters", "name": "Reuters"},
                    "author": None,
                    "title": "Ukraine forces retake areas north of Kyiv as Russians look eastward - Reuters",
                    "description": "Ukrainian forces were advancing on Saturday into areas north of Kyiv littered with debris and destroyed Russian tanks as Ukrainian President Volodymyr Zelenskiy accused departing Russian soldiers of leaving behind mines.",
                    "url": "https://www.reuters.com/world/europe/red-cross-heads-again-mariupol-russia-shifts-ukraine-focus-2022-04-02/",
                    "urlToImage": "https://www.reuters.com/resizer/pgk7uBTd6L8iRt6Go30MfBjIP2w=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/BHDHBKVGINN2FGF7YZTEJERFYA.jpg",
                    "publishedAt": "2022-04-02T17:42:00Z",
                    "content": "ZAPORIZHZHIA, Ukraine, April 2 (Reuters) - Ukrainian forces were advancing on Saturday into areas north of Kyiv littered with debris and destroyed Russian tanks as Ukrainian President Volodymyr Zelen… [+6189 chars]",
                },
                {
                    "source": {"id": None, "name": "ESPN"},
                    "author": "Mike Reiss",
                    "title": "Source - New England Patriots acquire WR DeVante Parker in trade with Miami Dolphins - ESPN",
                    "description": "The Patriots have acquired WR DeVante Parker and a 2022 fifth-round draft pick from the Dolphins in exchange for a 2023 third-round pick, a source told ESPN.",
                    "url": "https://www.espn.com/nfl/story/_/id/33654533/source-new-england-patriots-acquire-wr-devante-parker-trade-miami-dolphins",
                    "urlToImage": "https://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2019%2F1222%2Fr644759_1296x729_16%2D9.jpg",
                    "publishedAt": "2022-04-02T17:19:10Z",
                    "content": "FOXBOROUGH, Mass. -- In a rare trade between AFC East rivals, the New England Patriots have acquired Miami Dolphins wide receiver DeVante Parker and a 2022 fifth-round draft pick in exchange for a 20… [+2607 chars]",
                },
                {
                    "source": {"id": None, "name": "Electrek"},
                    "author": None,
                    "title": "Tesla beats all-time delivery record with 310,000 EVs despite difficult quarter - Electrek.co",
                    "description": "Tesla released its Q1 2022 delivery and production results today and confirmed just over 310,000 deliveries, which is a new all-time delivery record despite a difficult quarter for several reasons. Due to supply chain issues and 2 separate shutdowns at Gigafa…",
                    "url": "https://electrek.co/2022/04/02/tesla-tsla-beats-all-time-delivery-record-q1-2022/",
                    "urlToImage": "https://i0.wp.com/electrek.co/wp-content/uploads/sites/3/2021/12/Tesla-all-casrs-hero.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1",
                    "publishedAt": "2022-04-02T17:12:00Z",
                    "content": "Tesla released its Q1 2022 delivery and production results today and confirmed just over 310,000 deliveries, which is a new all-time delivery record despite a difficult quarter for several reasons.\r\n… [+2575 chars]",
                },
            ],
        }


@pytest.mark.asyncio
async def test_to_see_if_route_for_news_sends_error_when_api_fails(
    test_client: TestClient,
    test_configuration: Configuration,
    httpx_mock,
) -> None:
    httpx_mock.add_response(
        method="GET",
        status_code=401,
        json={"status": "error", "code": "apiKeyInvalid"},
    )
    async with httpx.AsyncClient() as client:
        response = await test_client.get(f"/api/news/")
        assert response.status == 400
        assert await response.json() == {
            "status": "error",
            "details": "Api key is not valid.",
        }


@pytest.mark.asyncio
async def test_for_remote_conn_error(
    test_client: TestClient,
    test_configuration: Configuration,
    httpx_mock,
) -> None:
    httpx_mock.add_exception(
        httpx.ConnectError("remote server not connecting"),
    )
    async with httpx.AsyncClient() as client:
        response = await test_client.get(f"/api/news/")
        assert response.status == 500
        assert await response.json() == {
            "status": "Connection with remote could not be established."
        }


@pytest.mark.asyncio
async def test_for_not_valid_url_timeout_error(
    test_client: TestClient,
    test_configuration: Configuration,
    httpx_mock,
) -> None:
    fake_url = "https://exa.com"
    httpx_mock.add_exception(
        httpx.TimeoutException("remote server timed out"),
    )
    async with httpx.AsyncClient() as client:
        response = await test_client.get(f"/api/news/")
        assert response.status == 500
        assert await response.json() == {"status": "Connection timedout."}
