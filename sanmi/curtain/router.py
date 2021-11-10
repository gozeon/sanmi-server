from flask import Blueprint, jsonify, request
from sqlalchemy import or_
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from sanmi.database import db
from datetime import datetime

from .models import Curtain
from ..decorats import auth_role

blueprint = Blueprint("curtain", __name__, url_prefix="/curtain")


@blueprint.route("/")
@jwt_required()
@auth_role(['admin'])
def all_curtain():
    return jsonify({
        "data": Curtain.query.all()
    })


@blueprint.route("/", methods=["POST"])
@jwt_required()
@auth_role(['admin'])
def add_curtain():
    from sanmi.contract.models import Contract
    room_name = request.json.get('room_name', None)
    material = request.json.get('material', None)
    dangling = request.json.get('dangling', None)
    fabric_kind = request.json.get('fabric_kind', None)
    open_way = request.json.get('open_way', None)
    width = request.json.get('width', None)
    height = request.json.get('height', None)
    join_way = request.json.get('join_way', None)
    cloth_main_no = request.json.get('cloth_main_no', None)
    cloth_sub1_no = request.json.get('cloth_sub1_no', None)
    cloth_sub2_no = request.json.get('cloth_sub2_no', None)
    cloth_lining_no = request.json.get('cloth_lining_no', None)
    cloth_yarn_no = request.json.get('cloth_yarn_no', None)

    drape_multiple = request.json.get('drape_multiple', None)
    lace_no = request.json.get('lace_no', None)
    lace_way = request.json.get('lace_way', None)
    craft_desc = request.json.get('craft_desc', None)
    curtain_scarf = request.json.get('curtain_scarf', None)
    curtain_scarf_deep = request.json.get('curtain_scarf_deep', None)
    curtain_scarf_no = request.json.get('curtain_scarf_no', None)

    rail_cloth_type = request.json.get('rail_cloth_type', None)
    rail_cloth_no = request.json.get('rail_cloth_no', None)
    rail_yarn_type = request.json.get('rail_yarn_type', None)
    rail_yarn_no = request.json.get('rail_yarn_no', None)
    rail_set_way = request.json.get('rail_set_way', None)
    rail_set_posi = request.json.get('rail_set_posi', None)

    rail_battery_type = request.json.get('rail_battery_type', None)
    rail_electric_lift = request.json.get('rail_electric_lift', None)
    rail_left_size = request.json.get('rail_left_size', None)
    rail_right_size = request.json.get('rail_right_size', None)
    rail_remark = request.json.get('rail_remark', None)
    image_url = request.json.get('image_url', None)

    contract_id = request.json.get('contract_id', None)

    contract = Contract.query.filter_by(id=contract_id).first()
    if contract is None:
        return jsonify({
            "msg": '合约(contract_id)不存在'
        })

    try:
        new_item = Curtain(room_name=room_name, material=material, dangling=dangling, fabric_kind=fabric_kind,
                           open_way=open_way, width=width, height=height, join_way=join_way,
                           cloth_main_no=cloth_main_no,
                           cloth_sub1_no=cloth_sub1_no, cloth_sub2_no=cloth_sub2_no, cloth_lining_no=cloth_lining_no,
                           cloth_yarn_no=cloth_yarn_no, drape_multiple=drape_multiple, lace_no=lace_no,
                           lace_way=lace_way,
                           craft_desc=craft_desc, curtain_scarf=curtain_scarf, curtain_scarf_deep=curtain_scarf_deep,
                           curtain_scarf_no=curtain_scarf_no, rail_cloth_type=rail_cloth_type,
                           rail_cloth_no=rail_cloth_no, rail_yarn_type=rail_yarn_type, rail_yarn_no=rail_yarn_no,
                           rail_set_way=rail_set_way, rail_set_posi=rail_set_posi, rail_battery_type=rail_battery_type,
                           rail_electric_lift=rail_electric_lift, rail_left_size=rail_left_size,
                           rail_right_size=rail_right_size,
                           rail_remark=rail_remark, image_url=image_url, contract_id=contract_id)
        db.session.add(new_item)
        db.session.commit()

        return jsonify({
            "data": new_item.id
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)})
