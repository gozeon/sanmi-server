from dataclasses import dataclass
from datetime import datetime
from sanmi.database import db
from sanmi.extensions import bcrypt


@dataclass
class Role(db.Model):
    id: int
    name: str
    display_name: str
    create_at: datetime
    update_at: datetime
    delete_at: datetime
    # users: User

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    display_name = db.Column(db.String(80), unique=True, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_at = db.Column(db.DateTime, default=None)
    # users = db.relationship('User', backref='rol', lazy=True)


@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    create_at: datetime
    update_at: datetime
    delete_at: datetime
    role_id: int
    role: Role

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_at = db.Column(db.DateTime, default=None)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', uselist=False)

    def gen_pwd(self, value):
        self.password = bcrypt.generate_password_hash(value)

    def verify_pwd(self, value):
        return bcrypt.check_password_hash(self.password, value)
