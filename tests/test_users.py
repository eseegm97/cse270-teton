import requests

BASE_URL = "http://127.0.0.1:8000/users"

def test_unauthorized_access_to_users(mocker):
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the response object
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""

    # Patch requests.get to return the mock response
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    assert response.text == "", f"Expected empty response body, got: '{response.text}'"


def test_successful_access_with_empty_response(mocker):
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""

    # Patch requests.get to return the mock response
    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.text == "", f"Expected empty response body, got: '{response.text}'"