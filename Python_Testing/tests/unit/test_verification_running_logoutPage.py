
def test_verification_running_logoutPage(client):

    response = client.get('/logout')

    response.status_code == 200