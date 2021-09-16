from flask import Flask, render_template, jsonify
from random import randint
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder = "../frontend/public/index.html")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/random")
def random_number():
    response = {"r_num": randint(1, 100)}
    return jsonify(response)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run()