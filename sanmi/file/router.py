import os
import time

from flask import Blueprint, jsonify, request, current_app, url_for
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from ..decorats import auth_role
from sanmi.config import config

blueprint = Blueprint("file", __name__, url_prefix="/file")


@blueprint.route("/upload", methods=["POST"])
@jwt_required()
@auth_role(['admin'])
def upload_file():
    file = request.files['file']
    filename =  str(time.time()) + '@' + file.filename
    file_path = os.path.abspath(os.path.join(current_app.root_path, 'static', filename))
    file.save(file_path)
    
    return jsonify({
        "data": {
            "baseUrl": config.get("server", 'host_name') or request.host_url,
            "filePath": url_for('static', filename=filename),
            "filename": file.filename,
        }
    })

