from server import loadCompetitions


def test_overbooking_not_possible(client):
    """Le test a pour but de vérifier que les 
        club n'achète pas plus de place que disponible."""


    competitions =  {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
    }

    number_of_place = 8
    
    client.post('/purchasePlaces', data={ 'club' : 'Simply Lift', 'competition' : competitions['name'], 'places' : number_of_place})

    response_seconde_two = client.get('/book/Fall%20Classic/Simply%20Lift')

    if (int(competitions['numberOfPlaces'])-number_of_place) >= 0 :

        assert str(int(competitions['numberOfPlaces'])-number_of_place) in response_seconde_two.data.decode()

    else:

        assert competitions['numberOfPlaces'] in response_seconde_two.data.decode()




   

