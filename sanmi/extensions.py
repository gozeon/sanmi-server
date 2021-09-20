from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
jwtManager = JWTManager()
cors = CORS
