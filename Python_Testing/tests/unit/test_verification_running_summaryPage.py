
def test_verification_running_summaryPage(client):
    email = "john@simplylift.co"
    response = client.post('/showSummary', data={'email':email})

    assert response.status_code == 200
