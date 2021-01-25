from flask import Flask , request
import json
import pickle
import sklearn
import pandas as pd
import numpy as np

from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    
    def post(self):
        filename = "pickle_model.pkl"
        pickle_model = pd.read_pickle(filename)
        
        data = request.get_json()['tweet']
        
        
        data = np.array(data)
        data = data.reshape((1,3))
        res = pickle_model.predict(data)
        print(res)
        return {"response" : str(res)}
        
        


api.add_resource(HelloWorld , "/")

if __name__ == "__main__":
    app.run(debug=True)


