import certifi
import datetime
import os

from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId

from flask_session import Session

# Google sign in packages
from google.oauth2 import credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow

load_dotenv()
MONGO_CLIENT_URL = os.getenv('MONGO_CLIENT_URI')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
SECRET_SESSION_KEY = os.getenv('SECRET_SESSION_KEY')

SESSION_FILE_DIR = "./session_data"

def create_app():
    app = Flask(__name__)

    if not os.path.exists(SESSION_FILE_DIR):
        os.makedirs(SESSION_FILE_DIR)

    # Configure Flask-Session to use in-memory storage
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = SECRET_SESSION_KEY
    app.config['SESSION_FILE_DIR'] = SESSION_FILE_DIR

    # Initialize Flask-Session
    Session(app)

    client = MongoClient(MONGO_CLIENT_URL,
                        tlsCAFile=certifi.where())
    app.db = client.microblog

    @app.route("/", methods=["GET"])
    def home():
        entries = app.db.entries.find( {} ).limit(10)
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"),
                entry["_id"]
            )
            for entry in entries
        ]
        session.clear()

        return render_template("home.html", entries=entries_with_date)
    
    @app.route("/write", methods=["GET", "POST"])
    def write():
        if session.get('user') and session['user'] == "Jake":
            if request.method == "POST":
                entry_content = request.form.get("content")
                formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
                app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
                # Reloads page and removes previously passed arguments
                return redirect('/')
            return render_template("write.html")
        return redirect('/')


    @app.route('/posts/<post_id>')
    def post_page(post_id):
        entries = app.db.entries.find({'_id': ObjectId(post_id)})
        post = [entry["content"] for entry in entries] 
        return render_template('post.html', post=post)

    @app.route("/login", methods=["GET"])
    def login():
        session['user'] = "Jake"
        return render_template('login.html')

    return app

