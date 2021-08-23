from flask import Flask, jsonify
from flask_restful import Resource, Api
import pandas as pd
import os

from pandas.core.reshape.merge import merge

app=Flask(__name__)
api=Api(app)

# CONSTS
# PATHS
RESULTS_PLAYED='result_played.csv'
RESULTS_UPCOMING='result_upcoming.csv'
DATABASE_FOLDER='database'

# COLUMNS
HOME_TEAM='home_team'
TOURNAMENT='tournament'
AWAY_TEAM='away_team'


class team_played(Resource):
    def __init__(self):
        self.data = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_PLAYED))
    
    def get(self, team): # GET request
        played_records_home=self.data.loc[self.data['home_team'] == team].to_dict(orient="records")
        played_records_away=self.data.loc[self.data['away_team'] == team].to_dict(orient="records")
        return jsonify({'data': played_records_home + played_records_away})  


class team_upcoming(Resource):    
    def __init__(self):
        #reading CSV file
        self.data = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_UPCOMING))
         # GET request
    def get(self,team):
        # Finding the desired values and converting them to JSON format
        played_records_home=self.data.loc[self.data['home_team'] == team].to_dict(orient="records")
        played_records_away=self.data.loc[self.data['away_team'] == team].to_dict(orient="records")
        return jsonify({'data': played_records_home + played_records_away})
    
class tournament_played(Resource):
    def __init__(self):
        #reading CSV file
        self.data = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_PLAYED))
         # GET request
    def get(self, tournament):
        # Finding the desired values and converting them to JSON format
        records=self.data.loc[self.data[TOURNAMENT] == tournament].to_dict(orient="records")
        return {'data': records}
    
class tournament_upcoming(Resource):
    def __init__(self):
        #reading CSV file
        self.data = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_UPCOMING))
         # GET request
    def get(self, tournament):
        # Finding the desired values and converting them to JSON format
        records=self.data.loc[self.data[TOURNAMENT] == tournament].to_dict(orient="records")
        return {'data': records}
    
class AllTournaments(Resource):
    def __init__(self):
        #reading CSV files
        self.results_played_db = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_PLAYED))
        self.results_upcoming_db = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_UPCOMING))
         # GET request
    def get(self, tournament):
        # Finding the desired values and converting them to JSON format
        played_records=self.results_played_db.loc[self.results_played_db[TOURNAMENT] == tournament].to_dict(orient="records")
        upcoming_records=self.results_upcoming_db.loc[self.results_upcoming_db[TOURNAMENT] == tournament].to_dict(orient="records")
        return {"data": played_records + upcoming_records}
    
class AllTeams(Resource):
    def __init__(self):
        #reading CSV files
        self.results_played_db = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_PLAYED))
        self.results_upcoming_db = pd.read_csv(os.path.join(DATABASE_FOLDER, RESULTS_UPCOMING))
         # GET request
    def get(self,team):
        # Finding the desired values and converting them to JSON format
        played_records_home=self.results_played_db.loc[self.results_played_db[HOME_TEAM] == team].to_dict(orient="records")
        upcoming_records_home=self.results_upcoming_db.loc[self.results_upcoming_db[HOME_TEAM] == team].to_dict(orient="records")
        played_records_away=self.results_played_db.loc[self.results_played_db[AWAY_TEAM] == team].to_dict(orient="records")
        upcoming_records_away=self.results_upcoming_db.loc[self.results_upcoming_db[AWAY_TEAM] == team].to_dict(orient="records")
        return {'data': played_records_home + played_records_away + upcoming_records_home + upcoming_records_away}

def router():
    api.add_resource(team_played, '/team-played/<string:team>')
    api.add_resource(team_upcoming, '/team-upcoming/<string:team>')
    api.add_resource(AllTeams, '/matches-by-team/<string:team>')
    api.add_resource(tournament_played, '/tournament-played/<string:tournament>')
    api.add_resource(tournament_upcoming, '/tournament-upcoming/<string:tournament>')
    api.add_resource(AllTournaments, '/matches-by-tournament/<string:tournament>')

if __name__ == '__main__':
    router()
    app.run(debug=False, port=8081)
