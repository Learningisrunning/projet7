from server import loadCompetitions

"""
def test_overbooking_not_possible(client):

    competitions = loadCompetitions()
    number_of_place = 8
    
    client.post('/purchasePlaces', data={ 'club' : 'Simply Lift', 'competition' : competitions[0]['name'], 'places' : number_of_place})

    response_seconde_two = client.get('/book/Spring%20Festival/Simply%20Lift')

    if (int(competitions[0]['numberOfPlaces'])-number_of_place) >= 0 :

        assert str(int(competitions[0]['numberOfPlaces'])-number_of_place) in response_seconde_two.data.decode()

    else:

        assert competitions[0]['numberOfPlaces'] in response_seconde_two.data.decode()

"""



   

