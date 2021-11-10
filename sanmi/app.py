from sanmi import user, contract, curtain, file
from sanmi.user.models import User
from flask import Flask
from sanmi.extensions import db, migrate, bcrypt, jwtManager, cors
from datetime import timedelta
from sanmi.config import config


@jwtManager.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    current_user = User.query.filter_by(id=jwt_payload['sub']['id']).first()
    return current_user.delete_at is not None


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('database', 'url')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('database', 'TRACK_MODIFICATIONS')
    app.config["JWT_SECRET_KEY"] = config.get('common', 'secret')
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    cors(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwtManager.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(user.router.blueprint)
    app.register_blueprint(contract.router.blueprint)
    app.register_blueprint(curtain.router.blueprint)
    app.register_blueprint(file.router.blueprint)
    return None
