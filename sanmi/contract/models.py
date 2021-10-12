from decimal import Decimal
from dataclasses import dataclass
from datetime import datetime
from sanmi.database import db
from sanmi.extensions import bcrypt


@dataclass
class Contract(db.Model):
    id: int
    # 合约编号
    number: str
    # 客户姓名
    client_name: str
    # 客户电话
    client_phone_1: str
    # 客户备用电话
    client_phone_2: str
    # 客户微信号
    client_wechat: str
    # 客户地址
    client_address: str
    # 地上楼层
    above_floor: int
    # 地下楼层
    under_floor: int
    # 居室数量
    bedroom_num: int
    # 客厅数量
    living_room_num: int
    # 卫生间数量
    rest_room_num: int
    # 客户来源
    client_source: int
    # 成交金额
    price: float
    # 礼品
    gift: int
    # 工期
    work_time: int
    create_at: datetime
    update_at: datetime
    delete_at: datetime

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(80), unique=True, nullable=False)
    client_name = db.Column(db.String(80), unique=False, nullable=False)
    client_phone_1 = db.Column(db.String(20), unique=False, nullable=False)
    client_phone_2 = db.Column(db.String(20), unique=False, nullable=True)
    client_wechat = db.Column(db.String(50), unique=False, nullable=True)
    client_address = db.Column(db.String, unique=False, nullable=True)
    # 地上楼层
    above_floor = db.Column(db.Integer)
    # 地下楼侧
    under_floor = db.Column(db.Integer)
    bedroom_num = db.Column(db.Integer)
    living_room_num = db.Column(db.Integer)
    rest_room_num = db.Column(db.Integer)
    client_source = db.Column(db.Integer)
    price = db.Column(db.Float)
    gift = db.Column(db.Integer)
    work_time = db.Column(db.Integer)

    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_at = db.Column(db.DateTime, default=None)
    # users = db.relationship('User', backref='rol', lazy=True)
