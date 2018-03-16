from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin,SQLAlchemyUserDatastore


# initialize sql-alchemy
db=SQLAlchemy()

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model,RoleMixin):
    """Model for the role Table"""
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True)
    description = db.Column(db.String(255))

class User(db.Model,UserMixin):
    """Model for the user Table"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    
    @staticmethod
    def createUser(email,password):
        user_datastore.create_user(email=email, password=password)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

class CRUDMixin(object):
    """This class is used for save and delete in child classes"""

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

# Define your Models here
class Bucketlist(db.Model,CRUDMixin):
    """This class represents the bucketlist table"""

    __tablename__ ='bucketlists'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def __repr__(self):
        return f"<Bucketlist: {self.name}>"

