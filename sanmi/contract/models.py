from dataclasses import dataclass
from datetime import datetime
from sanmi.database import db
from sanmi.extensions import bcrypt


@dataclass
class Contract(db.Model):
    id: int
    number: str
    client_name: str
    client_phone_1: str
    client_phone_2: str
    above_floor: int
    under_floor: int
    bedroom_num: int
    living_room_num: int
    client_source: int
    price: float
    gift: int
    work_time: int
    create_at: datetime
    update_at: datetime
    delete_at: datetime
    # users: User

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(80), unique=True, nullable=False)
    client_name = db.Column(db.String(80), unique=False, nullable=False)
    client_phone_1 = db.Column(db.String(20), unique=False, nullable=False)
    client_phone_2 = db.Column(db.String(20), unique=False, nullable=True)
    client_wechat = db.Column(db.String(50), unique=False, nullable=True)
    client_address = db.Column(db.String, unique=False, nullable=True)
    # 地上楼层
    above_floor = db.Column(db.Numeric)
    # 地下楼侧
    under_floor = db.Column(db.Numeric)

    bedroom_num = db.Column(db.Numeric)
    living_room_num = db.Column(db.Numeric)
    client_source = db.Column(db.Numeric)
    price = db.Column(db.Float)
    gift = db.Column(db.Numeric)
    work_time = db.Column(db.Numeric)

    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_at = db.Column(db.DateTime, default=None)
    # users = db.relationship('User', backref='rol', lazy=True)
