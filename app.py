import flask
import flask_restful
import urllib.parse
import urllib.request
import jsons
import os

app = flask.Flask(__name__)
api = flask_restful.Api(app)
address = 'Washington DC'

class test(flask_restful.Resource):
    def get(self):
        return {"test": "location of test"}

class init(flask_restful.Resource):
    def get(self):
        return {"init": "location of " + address}

class location(flask_restful.Resource):
    def get(self):
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

api.add_resource(init, '/init')
api.add_resource(test, '/test')
api.add_resource(location, '/location')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')

