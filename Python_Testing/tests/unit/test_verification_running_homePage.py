

def test_verification_running_homePage(client):

    response = client.get('/')

    assert response.status_code == 200