"""
Created on Sun Aug 22 2021
This one is WORKING
@author: galit
"""

from flask import Flask, jsonify
from flask_restful import Resource, Api , reqparse
import pandas as pd
import os
import glob

app=Flask(__name__)
api=Api(app)

  
data_arg=reqparse.RequestParser()
data_arg.add_argument("home_team" , type=str ,help="Enter home_team")
data_arg.add_argument("home_score" , type=int ,help="Enter home_score")
data_arg.add_argument("away_team" , type=str ,help="Enter away_team")
data_arg.add_argument("away_score" , type=int ,help="Enter away_score")
data_arg.add_argument("tournament" , type=str ,help="Enter tournament")
data_arg.add_argument("start_time" , type=str ,help="Enter start_time")


class team_played(Resource):    
    def __init__(self):
        self.data = pd.read_csv('result_played.csv')
    def get(self,home_team): # GET request
        data_fount=self.data.loc[self.data['home_team'] == home_team].to_json(orient="records")
        return jsonify({'Result are': data_fount})        
    
class team_upcoming(Resource):    
    def __init__(self):
        self.data = pd.read_csv('result_upcoming.csv')        
    def get(self,home_team): # GET request
        data_fount=self.data.loc[self.data['home_team'] == home_team].to_json(orient="records")
        return jsonify({'Result are': data_fount})   
    
class tournament_played(Resource):
    def __init__(self):
        self.data = pd.read_csv('result_played.csv')       
    def get(self,tournament): # GET request
        data_fount=self.data.loc[self.data['tournament'] == tournament].to_json(orient="records")
        return jsonify({'Result are': data_fount})
    
class tournament_upcoming(Resource):
    def __init__(self):
        self.data = pd.read_csv('result_upcoming.csv')       
    def get(self,tournament): # GET request
        data_fount=self.data.loc[self.data['tournament'] == tournament].to_json(orient="records")
        return jsonify({'Result are': data_fount}) 
    
class AllTournaments(Resource):
    def __init__(self):
        path = os.getcwd()
        self.csv_files = glob.glob(os.path.join(path, "*.csv"))
        #self.data = pd.read_csv('result_played.csv')      
    def get(self,tournament): # GET request
        data_fount=self.csv_files.loc[self.csv_files['tournament'] == tournament].to_json(orient="records")
        return jsonify({'Result are': data_fount})
    
class AllTeams(Resource):
    def __init__(self):
        path = os.getcwd()
        self.csv_files = glob.glob(os.path.join(path, "*.csv"))
        #self.data = pd.read_csv('result_played.csv')      
    def get(self,home_team): # GET request
        data_fount=self.csv_files.loc[self.csv_files['home_team'] == home_team].to_json(orient="records")
        return jsonify({'Result are': data_fount})


api.add_resource(team_played, '/team_played/<string:home_team>')
api.add_resource(team_upcoming, '/team_upcoming/<string:home_team>')
api.add_resource(AllTeams, '/AllTeams/<string:home_team>')
api.add_resource(tournament_played, '/tournament_played/<string:tournament>')
api.add_resource(tournament_upcoming, '/tournament_upcoming/<string:tournament>')
api.add_resource(AllTournaments, '/AllTournaments/<string:tournament>')

if __name__ == '__main__':
    app.run(debug=False, port=8081)