import pytest
from app import app


@pytest.fixture
def client():
    """
    Pytest fixture that provides a Flask test client.
    Enables testing of Flask routes without running a live server.
    
    Yields:
        FlaskClient: A test client for making requests to the Flask app
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    """
    Test the main hello endpoint.
    
    Verifies:
        - HTTP 200 status code is returned
        - Response contains correct greeting message
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}


def test_health_endpoint(client):
    """
    Test the health check endpoint.
    
    Verifies:
        - HTTP 200 status code is returned
        - Response indicates service is healthy
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_product_endpoint(client):
    """
    Test the product page navigation endpoint.
    
    Verifies:
        - HTTP 200 status code is returned
        - Response contains product page navigation message
    """
    response = client.get('/product')
    assert response.status_code == 200
    assert response.json == {"message": "Pointing to product page"}
