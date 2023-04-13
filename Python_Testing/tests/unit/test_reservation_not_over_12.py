from server import loadClubs, loadCompetitions, purchasePlaces
def test_actualisation_point_club(client):

    clubs = loadClubs()
    competitions = loadCompetitions()

    number_of_place = 2

    response = client.post('/purchasePlaces', data={ 'club' : clubs[0]['name'], 'competition' : competitions[0]['name'], 'places' : number_of_place})

    if  number_of_place <= 12:

        number_of_remaining_point = int(clubs[0]['points']) - number_of_place
        assert "Points available: " + str(number_of_remaining_point) in response.data.decode()

    else :
        print('vous ne pouvez pas réserver plus de 12 places par compétition')
        assert "Points available: " + clubs[0]['points'] in response.data.decode()


    