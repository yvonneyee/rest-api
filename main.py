from flask import Flask
from flask_restful import Api, Resource


import matplotlib
import matplotlib.pyplot as plt
from random import randint
from random import randint,shuffle
from io import BytesIO
import base64
import requests, json

from questions import algebra

app = Flask(__name__)
api = Api(app)


names = {"tim": {"age": 22, "gender": "male"},
         "bill": {"age": 20, "gender": "male"},
         "question": algebra.A_math_question(),
         "q2":algebra.find_x_angel_in_qualdrilateral()
         }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
