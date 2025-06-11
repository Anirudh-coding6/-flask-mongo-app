from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# # Local MongoDB (installed version)
# MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
# client = MongoClient(MONGO_URI)
# db = client["mydatabase"]
# collection = db["users"]

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["users"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        collection.insert_one({"name": name, "email": email})
        return redirect("/")
    users = collection.find()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)