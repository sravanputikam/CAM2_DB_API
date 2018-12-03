from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT
from resources.images import CameraList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost/database_name"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "cam2"
api = Api(app)

# jwt = JWT(app,authenticate,identity)

'''
    url patterns are defined here
'''
api.add_resource(CameraList, '/cameraId/<string:cameraId>')


if __name__ == '__main__':

    # Runs the API
    from db import db
    db.init_app(app)
    app.run(5000, debug=True)