from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "GroupYar is running!"

def start_webserver():
    app.run(host="0.0.0.0", port=10000)
