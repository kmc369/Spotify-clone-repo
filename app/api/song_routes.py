from flask import Blueprint, jsonify, request 
from flask_login import login_required
from app.models import Song,Album,db,Playlist


songs_bp = Blueprint('songs',__name__)


@songs_bp.route("/playlist/<int:userid>", methods=["GET"])
def get_songs_of_playlist(userid):
    """GET ALL THE SONGS ON Playlist function"""

    playlists = Playlist.query.filter_by(user_id =userid).all()
  
   
    if not playlists:
        return jsonify({"message":"No playlist found"},400)
    return [playlist.to_dict() for playlist in playlists]


@songs_bp.route("/user/<int:userid>", methods=["GET"])
def get_user_songs(userid):
    """GET ALL THE SONGS OF THE USER """ 

    songs = Song.query.filter_by(user_id=userid).all()

    if not songs:
        return jsonify({"message":"No song found"},400)
    return [song.to_dict() for song in songs]


@songs_bp.route("/<int:albumid>", methods=["GET"])
def get_songs_of_album(albumid):
    """GET ALL THE SONGS ON AN ALBUM"""

    songs = Song.query.filter_by(album_id=albumid).all()
  
   
    if not songs:
        return jsonify({"message":"No songs found"},400)
    return [song.to_dict() for song in songs]





 