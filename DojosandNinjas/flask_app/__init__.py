from flask import Flask
app = Flask(__name__)
app.secret_key = "No secret on github"
DATABASE = "dojos_and_ninjas_schema"  