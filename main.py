from flask import Flask
from flask_restful import Api, Resource


import matplotlib
import matplotlib.pyplot as plt
from random import randint
from random import randint,shuffle
from io import BytesIO
import base64
import requests, json



app = Flask(__name__)
api = Api(app)

class Q_type():
    multichoice = "multichoice"
    singlechoice = "singlechoice"
    photo = "photo"
    shortreply = "shortreply"

def A_math_question():
        return {"photo": "44", "topic": 55, "reason":"have fun4"}

names = {"tim": {"age": 22, "gender": "male"},
         "bill": {"age": 20, "gender": "male"},
         "question": A_math_question(),
         }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
