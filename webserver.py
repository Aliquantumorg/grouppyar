from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "GroupYar is running!"

def start_webserver():
    thread = threading.Thread(
        target=lambda: app.run(
            host="0.0.0.0",
            port=10000,
            use_reloader=False
        ),
        daemon=True
    )
    thread.start()
