from fastapi.testclient import TestClient
from Testing_API34 import app


client = TestClient(app)

# test home API
def test_home():
    response = client.get("/")
    # status code check
    assert response.status_code == 200
    # Response data check
    assert response.json() =={"message": "Hello Anand"}
    
    
# Test ADD API
def test_add():
    response = client.get("/add?a=5&b=3")
    
    assert response.status_code == 200
    assert response.json() == {"result": 8}
