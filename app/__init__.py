from flask_api import FlaskAPI
from flask import request,jsonify,abort
from app.models import db,User,Role,user_datastore
from app.controllers import bucketlistApp


# local import 
from instance.config import app_config
from flask_security import Security



def create_app(config_name):
    app=FlaskAPI(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(bucketlistApp) # add 
    db.init_app(app)

    security = Security(app, user_datastore)

    return app


