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
def all_contract():
    return jsonify({
        "data": Contract.query.all()
    })

@blueprint.route("/<int:contract_id>")
@jwt_required()
@auth_role(['admin'])
def get_contract_info_by_id(contract_id):
    contract = Contract.query.filter_by(id=contract_id).first()
    if contract is None:
        return jsonify({"msg": "该合约不存在"})
    return jsonify({
        "data": contract
    })


@blueprint.route("/", methods=["POST"])
@jwt_required()
@auth_role(['admin'])
def all_user():
    number = request.json.get('number', None)
    client_name = request.json.get('client_name', None)
    client_phone_1 = request.json.get('client_phone_1', None)
    client_phone_2 = request.json.get('client_phone_2', None)
    client_wechat = request.json.get('client_wechat', None)
    client_address = request.json.get('client_address', None)
    above_floor = request.json.get('above_floor', None)
    under_floor = request.json.get('under_floor', None)
    bedroom_num = request.json.get('bedroom_num', None)
    living_room_num = request.json.get('living_room_num', None)
    rest_room_num = request.json.get('rest_room_num', None)
    client_source = request.json.get('client_source', None)
    price = request.json.get('price', None)
    gift = request.json.get('gift', None)
    work_time = request.json.get('work_time', None)

    try:
        new_item = Contract(number=number, client_name=client_name, client_phone_1=client_phone_1,
                            client_phone_2=client_phone_2,
                            client_wechat=client_wechat,
                            client_address=client_address,
                            above_floor=above_floor,
                            under_floor=under_floor,
                            bedroom_num=bedroom_num,
                            living_room_num=living_room_num,
                            rest_room_num=rest_room_num,
                            client_source=client_source,
                            price=price,
                            gift=gift,
                            work_time=work_time)
        db.session.add(new_item)
        db.session.commit()

        return jsonify({
            "data": new_item.id
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)})
