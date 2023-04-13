from server import loadClubs

def test_verification_number_point_for_each_club(client):

    clubs = loadClubs()
    response = client.get('/clubsPoints')

    for club in clubs:
        assert "club name : " + club['name'] in response.data.decode()
        assert "number of points : " + club['points'] in response.data.decode()