import flask
import flask_restful
import urllib.parse
import urllib.request
import jsons

app = flask.Flask(__name__)
api = flask_restful.Api(app)

class location(flask_restful.Resource):
    def get(self):
        address = 'Washington DC'
        returnurl = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
        response = urllib.request.urlopen(returnurl)
        data = jsons.loads(response.read().decode(response.info().get_param('charset') ))
        wresponse = "Lattitude = " + data[0]["lat"]
        wresponse += "\nlongitude = " + data[0]["lon"]

        return {address: wresponse}

api.add_resource(location, '/')

if __name__ == "__main__":
    app.run(debug=True)