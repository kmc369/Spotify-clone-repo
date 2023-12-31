from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    image = db.Column(db.String(1000))
    hashed_password = db.Column(db.String(255), nullable=False)

    #relationships 
    songs = db.relationship("Song", back_populates="user", cascade="all, delete-orphan")
    albums = db.relationship("Album", back_populates="user", cascade="all, delete-orphan")
    playlists = db.relationship("Playlist", back_populates="user", cascade="all, delete-orphan")
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "image":self.image,
            'email': self.email
            
        }
