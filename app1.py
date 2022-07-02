import flask
import flask_restful
import urllib.parse
import urllib.request
import jsons

app = flask.Flask(__name__)
api = flask_restful.Api(app)

class HelloWorld(flask_restful.Resource):
    def get(self):
        address = 'Washington DC'
        returnurl = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
        response = urllib.request.urlopen(returnurl)
        data = jsons.loads(response.read().decode(response.info().get_param('charset') ))
        wresponse = "Lattitude = " + data[0]["lat"]
        wresponse += "\nlongitude = " + data[0]["lon"]

        return {address: wresponse}

    def post(self):
        json_data = request.get_json(force=True)
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        return jsonify(firstname=firstname, lastname=lastname)

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)