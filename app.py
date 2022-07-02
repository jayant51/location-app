from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import urllib.parse
import urllib.request
import os
  
# creating the flask app
app = Flask(__name__)
CORS(app) 
# creating an API object
api = Api(app)
  
class Init(Resource):  
    def get(self):
        return('Location Api init')

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Location(Resource):
    def get(self):
        address = 'Washington DC\n'
        wresponse="Location- Service\n"
        returnurl = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

        x = urllib.request.urlopen(returnurl)
        response = request.get(returnurl).json()
        wresponse += address
        wresponse += "Lattitude = " + response[0]["lat"]
        wresponse += "\nlongitude = " + response[0]["lon"]
        return jsonify({'data': wresponse}), 201
  
api.add_resource(Init, '/')
api.add_resource(Location, '/getlocation')


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')

