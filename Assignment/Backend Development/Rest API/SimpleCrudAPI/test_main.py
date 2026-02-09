from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    # Setup/Teardown logic for test DB would go here
    pass

def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "test@example.com"}
    )

    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert "id" in response.json()
