import pytest
import httpx

from app.model_client import ModelClient


@pytest.mark.anyio("asyncio")
async def test_model_client_generate():
    async def handler(request):
        """
        Return a fixed HTTP 200 response with JSON payload {"output": "ok"}.
        
        Parameters:
            request (httpx.Request): Incoming HTTP request (unused).
        
        Returns:
            httpx.Response: Response with status code 200 and JSON body {"output": "ok"}.
        """
        return httpx.Response(200, json={"output": "ok"})

    transport = httpx.MockTransport(handler)
    async with httpx.AsyncClient(transport=transport) as mock_client:
        client = ModelClient(base_url="http://test", client=mock_client)
        result = await client.generate("hi")
    assert result["output"] == "ok"
