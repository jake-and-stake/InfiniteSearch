import certifi
import datetime
import os

from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()
MONGO_CLIENT_URL = os.getenv('MONGO_CLIENT_URI')

def create_app():
    app = Flask(__name__)
    client = MongoClient(MONGO_CLIENT_URL,
                        tlsCAFile=certifi.where())
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
            # Reloads page and removes previously passed arguments
            return redirect('/')

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

        return render_template("home.html", entries=entries_with_date)
    
    @app.route("/write", methods=["GET", "POST"])
    def write():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
            # Reloads page and removes previously passed arguments
            return redirect('/')
        return render_template("write.html")

    @app.route('/posts/<post_id>')
    def post_page(post_id):
        entries = app.db.entries.find({'_id': ObjectId(post_id)})
        post = [entry["content"] for entry in entries] 
        return render_template('post.html', post=post)

    return app

