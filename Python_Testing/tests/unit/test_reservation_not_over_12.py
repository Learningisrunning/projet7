

def test_reservation_not_over_12(client):

    """Le test a pour but de vérifier que les 
        club n'achète pas plus de 12 places
        sur une compétition"""
    
    clubs =  {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    }

    competitions =  {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
    }

    number_of_place = 2

    response = client.post('/purchasePlaces', data={ 'club' : clubs['name'], 'competition' : competitions['name'], 'places' : number_of_place})

    if  number_of_place <= 12:

        number_of_remaining_point = int(clubs['points']) - number_of_place
        assert "Points available: " + str(number_of_remaining_point) in response.data.decode()

    else :
        print('vous ne pouvez pas réserver plus de 12 places par compétition')
        assert "Points available: " + clubs['points'] in response.data.decode()
