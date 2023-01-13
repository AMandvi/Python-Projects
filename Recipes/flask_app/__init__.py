from flask import Flask
app = Flask(__name__)
app.secret_key = "No secret on github"
DATABASE = "recipes"