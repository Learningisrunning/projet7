import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask('__name__')
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():

    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if placesRequired <=12 :
        if int(competition['numberOfPlaces']) - placesRequired >= 0 and int(club['points']) - placesRequired >=0:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club['points'] = int(club['points']) - placesRequired

            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)

        elif  int(club['points']) - placesRequired < 0:

            flash("Vous n'avez pas assez de points pour réserver " + str(placesRequired) + " places")
            return render_template('welcome.html', club=club, competitions=competitions)
        
        elif int(competition['numberOfPlaces']) - placesRequired < 0: 

            flash("Vous ne pouvez pas réserver plus de place qu'il n'y en a de disponible")
            return render_template('welcome.html', club=club, competitions=competitions)
    else :
        flash("Vous ne pouvez pas réserver plus de 12 place sur une compétition")
        return render_template('welcome.html', club=club, competitions=competitions)
    
    


# TODO: Add route for points display
@app.route('/clubsPoints', methods=['GET'])
def clubsPoints():
    return render_template('clubspoints.html', clubs = clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)