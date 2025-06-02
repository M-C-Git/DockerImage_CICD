from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200, "The webpage load is not successful!"
    assert response.data == b"Hello World!"
