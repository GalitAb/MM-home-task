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

class read(Resource):
    
    def __init__(self):        
        self.data = pd.read_csv('result_played.csv') # reading csv file
        
    def get(self,hs): # GET request
        data_fount=self.data.loc[self.data['home_score'] == hs].to_json(orient="records")
        return jsonify({'Result': data_fount})
        

api.add_resource(read, '/<int:hs>')
#api.add_resource(read_Delete, '/<str:hs>')

if __name__ == '__main__':
    app.run(debug=False, port=8081)
    
