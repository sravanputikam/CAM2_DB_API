from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import JWT,jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

jwt = JWT()
items = []


if __name__ == '__main__':
    app.run(5000, debug=True)