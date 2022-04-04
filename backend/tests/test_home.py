from typing import Any

import pytest
from blacksheep.contents import Content
from blacksheep.testing import TestClient


@pytest.mark.asyncio
async def test_index_route(test_client: TestClient) -> None:
    response = await test_client.get(f"/")
    text = await response.text()
    assert response.status == 200
    assert text == "welcome to news api"
