#!/usr/bin/python3
""" Module for api """
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS

from api.v1.views import app_views

from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def teardown_flask(exception):
    """close storage"""
    storage.close()


@app.errorhandler(400)
def handle_400(error):
    """handle HTTP 400 error code."""
    if error.description:
        return jsonify(error=error.description), 400
    return jsonify(error="Bad Request"), 400


@app.errorhandler(404)
def handle_404(error):
    """handle HTTP 404 error code."""
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    env_host = getenv("HBNB_API_HOST", "0.0.0.0")
    env_port = getenv("HBNB_API_PORT", "5000")
    app.run(host=env_host, port=env_port, threaded=True)
