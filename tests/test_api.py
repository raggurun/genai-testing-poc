from fastapi.testclient import TestClient # pyright: ignore[reportMissingImports]

from app.main import app


client = TestClient(app)


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "UP"
    )


def test_chat_api():

    response = client.post(
        "/api/chat",
        json={
            "message":
            "What is my account balance?"
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert (
        body["intent"]
        == "get_balance"
    )

    assert (
        body["tool_call"]["name"]
        == "get_balance"
    )

    assert (
        body["tool_result"]["balance"]
        == 25000
    )

    assert (
        "25,000"
        in body["answer"]
    )