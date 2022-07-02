from flask import Flask, jsonify
from flask_restful import Resource, Api 
import jsons
from flask_cors import CORS
import urllib.parse
import urllib.request
import os
  
# creating the flask app
app = Flask(__name__)
CORS(app) 
# creating an API object
api = Api(app)
  
class init(Resource):  
    def get(self):
        return('Location Api init')

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class location(Resource):
    def get(self):
        address = 'Washington DC\n'
        wresponse="Location- Service\n"
        returnurl = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

        x = urllib.request.urlopen(returnurl)
        print(x)
        response = urllib.request.urlopen(returnurl)
        data = jsons.loads(response.read().decode(response.info().get_param('charset') ))
        print(data)
        wresponse += address
        wresponse += "Lattitude = " + response[0]["lat"]
        wresponse += "\nlongitude = " + response[0]["lon"]
        return jsonify({'data': wresponse}), 201
  
#api.add_resource(init, '/')
api.add_resource(location, '/')


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')

