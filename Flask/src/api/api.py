from flask import Blueprint
from flask import jsonify, request
import logging
from src.model import Model


model_blueprint = Blueprint("model", __name__)
logger = logging.getLogger("log.log")


@model_blueprint.route("/model", methods=["POST"])
def detect():
    postdata = request.get_json()
    model = Model(postdata)
    return model.process()
