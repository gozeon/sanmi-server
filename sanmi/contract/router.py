from flask import Blueprint, jsonify, request
from sqlalchemy import or_
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from sanmi.database import db
from datetime import datetime

from .models import Contract
from ..decorats import auth_role

blueprint = Blueprint("contract", __name__, url_prefix="/contract")


@blueprint.route("/")
@jwt_required()
@auth_role(['admin'])
def all_user():
    return jsonify({
        "data": 1
    })
