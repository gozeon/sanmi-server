from dataclasses import dataclass
from datetime import datetime
from sanmi.database import db


@dataclass
class Curtain(db.Model):
    id: int
    # 房间名称
    room_name: str
    # 材料
    material: int
    # 悬挂方式
    dangling: int
    # 布料种类
    fabric_kind: int
    # 打开方式
    open_way: int
    # 宽(单位: 米)
    width: int
    # 高(单位: 米)
    height: int
    # 拼接方式
    join_way: int

    # 主布编号
    cloth_main_no: str
    # 配布1编号
    cloth_sub1_no: str
    # 配布2编号
    cloth_sub2_no: str
    # 衬布编号
    cloth_lining_no: str
    # 纱布编号
    cloth_yarn_no: str

    # 褶皱倍数
    drape_multiple: float
    # 花边编号
    lace_no: str
    # 花边车缝方式
    lace_way: int
    # 工艺特殊要求
    craft_desc: str

    # 窗幔
    curtain_scarf: int
    # 窗帘盒深(单位: 米)
    curtain_scarf_deep: float
    # 窗幔编号
    curtain_scarf_no: int

    # 杆轨布帘
    rail_cloth_type: int
    # 布帘编号
    rail_cloth_no: str
    # 杆轨纱帘
    rail_yarn_type: int
    # 纱帘编号
    rail_yarn_no: str
    # 安装方式
    rail_set_way: int
    # 安装位置
    rail_set_posi: int
    # 电池类型
    rail_battery_type: int
    # 电动升降（和高度相关）
    rail_electric_lift: int
    # L型左尺寸
    rail_left_size: float
    # L型右尺寸
    rail_right_size: float
    # 备注
    rail_remark: str
    # 安装位置照片
    image_url: str
    contract_id: int

    create_at: datetime
    update_at: datetime
    delete_at: datetime

    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(80), unique=False, nullable=False)
    material = db.Column(db.Integer)
    dangling = db.Column(db.Integer)
    fabric_kind = db.Column(db.Integer)
    open_way = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    join_way = db.Column(db.Integer)

    cloth_main_no = db.Column(db.String(100), unique=False, nullable=True)
    cloth_sub1_no = db.Column(db.String(100), unique=False, nullable=True)
    cloth_sub2_no = db.Column(db.String(100), unique=False, nullable=True)
    cloth_lining_no = db.Column(db.String(100), unique=False, nullable=True)
    client_wechat = db.Column(db.String(100), unique=False, nullable=True)
    cloth_yarn_no = db.Column(db.String(100), unique=False, nullable=True)

    drape_multiple = db.Column(db.Float)
    lace_no = db.Column(db.String(100), unique=False, nullable=True)
    lace_way = db.Column(db.Integer)
    craft_desc = db.Column(db.String(500), unique=False, nullable=True)

    curtain_scarf = db.Column(db.Integer)
    curtain_scarf_deep = db.Column(db.Float)
    curtain_scarf_no = db.Column(db.String(100), unique=False, nullable=True)

    rail_cloth_type = db.Column(db.Integer)
    rail_cloth_no = db.Column(db.String(100), unique=False, nullable=True)
    rail_yarn_type = db.Column(db.Integer)
    rail_yarn_no = db.Column(db.String(100), unique=False, nullable=True)
    rail_set_way = db.Column(db.Integer)
    rail_set_posi = db.Column(db.Integer)
    rail_battery_type = db.Column(db.Integer)
    rail_electric_lift = db.Column(db.Integer)
    rail_left_size = db.Column(db.Float)
    rail_right_size = db.Column(db.Float)
    rail_remark = db.Column(db.String(500), unique=False, nullable=True)
    image_url = db.Column(db.String(300), unique=False, nullable=True)

    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_at = db.Column(db.DateTime, default=None)

    # 关联
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'), nullable=False)
