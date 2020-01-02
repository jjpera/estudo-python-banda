
# Import the framework
from flask import Flask
from flask_restful import Api
from controller import Banda, BandaId

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

@app.route("/")
def index():
    return 'Hello World'

api.add_resource(Banda, '/bandas/banda')
api.add_resource(BandaId, '/bandas/banda/<string:identifier>')

app.run(host='0.0.0.0', port=8086, debug=True)