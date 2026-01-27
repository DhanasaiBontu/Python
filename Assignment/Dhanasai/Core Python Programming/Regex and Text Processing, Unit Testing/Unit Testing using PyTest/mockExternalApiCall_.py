import pytest
from unittest.mock import patch
import requests
def get_temperature(city: str) -> int:
    response = requests.get(f"https://fake-weather-api.com/{city}")
    data = response.json()
    return data["temperature"]
def test_get_temperature():
    fake_response = {"temperature": 20}
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        temp = get_temperature("London")
        assert temp == 20
        mock_get.assert_called_once_with("https://fake-weather-api.com/London")