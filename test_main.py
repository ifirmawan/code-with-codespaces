from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_calc_addition():
    response = client.get("/calc?a=4&operator=%2B&b=2")
    assert response.status_code == 200
    assert response.json() == {
        "a": 4,
        "operator": "+",
        "b": 2,
        "result": 6,
    }


def test_calc_division_by_zero_returns_400():
    response = client.get("/calc?a=4&operator=/&b=0")
    assert response.status_code == 400
