from server import loadClubs, loadCompetitions



def test_actualisation_point_club(client):
    """expliquer le test"""

    clubs =  {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    }

    competitions =  {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
    }

    number_of_place = 3

    response = client.post('/purchasePlaces', data={ 'club' : clubs['name'], 'competition' : competitions['name'], 'places' : number_of_place})

    if int(clubs['points']) - number_of_place >= 0:

        number_of_remaining_point = int(clubs['points']) - number_of_place
        assert "Points available: " + str(number_of_remaining_point) in response.data.decode()

    else :
        print('vous ne pouvez pas réserver plus de place que votre nombre de points')
        assert "Points available: " + clubs['points'] in response.data.decode()
