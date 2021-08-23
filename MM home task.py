"""
Created on Sun Aug 22 2021

@author: galit
"""

from flask import Flask, jsonify
from flask_restful import Resource, Api , reqparse
import pandas as pd

app=Flask(__name__)
api=Api(app)

  
data_arg=reqparse.RequestParser()
data_arg.add_argument("home_team" , type=str ,help="Enter home_team")
data_arg.add_argument("home_score" , type=int ,help="Enter home_score")
data_arg.add_argument("away_team" , type=str ,help="Enter away_team")
data_arg.add_argument("away_score" , type=int ,help="Enter away_score")
data_arg.add_argument("tournament" , type=str ,help="Enter tournament")
data_arg.add_argument("start_time" , type=str ,help="Enter start_time")


class findTeam(Resource):    
    def __init__(self):
        self.data = pd.read_csv('result_played.csv') # reading csv file        
    def get(self,ht): # GET request
        data_fount=self.data.loc[self.data['home_team'] == ht].to_json(orient="records")
        return jsonify({'Result are': data_fount})        
    
class findTournament(Resource):
    def __init__(self):
        self.data = pd.read_csv('result_played.csv') # reading csv file        
    def get(self,tournament): # GET request
        data_fount=self.data.loc[self.data['tournament'] == tournament].to_json(orient="records")
        return jsonify({'Result are': data_fount}) 

api.add_resource(findTeam, '/findTeam/<string:ht>')
api.add_resource(findTournament, '/findTournament/<string:tournament>')

if __name__ == '__main__':
    app.run(debug=False, port=8081)