from flask import Blueprint, render_template, abort,jsonify,request
from jinja2 import TemplateNotFound
from app.models import *

from flask_security import auth_token_required,http_auth_required


bucketlistApp = Blueprint('BucketListApp', __name__,
                        template_folder='templates')


# Create a user to test with
@bucketlistApp.before_app_first_request
def create_user():
    if not User.query.first():
        User.createUser(email='test@example.com', password='test123')
        db.session.commit()


@bucketlistApp.route('/bucketlists', methods=['POST', 'GET'])
@auth_token_required
def bucketlists():
    if request.method == "POST":
        name = str(request.data.get('name', ''))
        if name:
            bucketlist = Bucketlist(name=name)
            bucketlist.save()
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 201
            return response
    else:
        # GET
        bucketlists = Bucketlist.get_all()
        results = []

        for bucketlist in bucketlists:
            obj = {
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

@bucketlistApp.route('/bucketlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bucketlist_manipulation(id, **kwargs):
    # retrieve a buckelist using it's ID
    bucketlist = Bucketlist.query.filter_by(id=id).first()
    if not bucketlist:
        # Raise an HTTPException with a 404 not found status code
        abort(404)

    if request.method == 'DELETE':
        bucketlist.delete()
        return {
        "message": "bucketlist {} deleted successfully".format(bucketlist.id) 
        }, 200

    elif request.method == 'PUT':
        name = str(request.data.get('name', ''))
        bucketlist.name = name
        bucketlist.save()
        response = jsonify({
            'id': bucketlist.id,
            'name': bucketlist.name,
            'date_created': bucketlist.date_created,
            'date_modified': bucketlist.date_modified
        })
        response.status_code = 200
        return response
    else:
        # GET
        response = jsonify({
            'id': bucketlist.id,
            'name': bucketlist.name,
            'date_created': bucketlist.date_created,
            'date_modified': bucketlist.date_modified
        })
        response.status_code = 200
        return response
    


