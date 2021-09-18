from flask import Flask, render_template, jsonify, request
from random import randint
from flask_cors import CORS
import requests as re
import json

app = Flask(__name__, template_folder = "../frontend/public/index.html")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/handler", methods=["GET", "POST"])
def random_number():
  if request.method == "GET":
    response = {"r_num": randint(1, 100)}
    return jsonify(response)
  elif request.method == "POST":
    UDATA_URL = "https://getpantry.cloud/apiv1/pantry/21ceb567-2886-4091-b255-efa0913b311b/basket/Flask-Vue-test"
    Fdata = request.get_json()
    Fdata = Fdata.get("fromVue")
    Udata = {}
    Udata["fromVue"] = int(Fdata)
    update = re.post(UDATA_URL, json=Udata)
    return jsonify({"status": "success"})
  else:
    pass

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run()