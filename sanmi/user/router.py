from flask import Blueprint, jsonify, request
from sqlalchemy import or_
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from sanmi.database import db
from datetime import datetime

from .models import User, Role
from ..decorats import auth_role

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route("/")
@jwt_required()
@auth_role(['admin'])
def all_user():
    return jsonify({
        "data": User.query.join(Role, User.role_id == Role.id).all()
    })


@blueprint.route("/", methods=["POST"])
@jwt_required()
@auth_role(['admin'])
def add_user():
    name = request.json.get('name', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    role_id = request.json.get('roleId', None)

    if name is None:
        return jsonify({"msg": '用户名称(name)不能为空'})
    elif password is None:
        return jsonify({"msg": '用户密码(password)不能为空'})
    elif email is None:
        return jsonify({"msg": '用户邮箱(email)不能为空'})
    elif role_id is None:
        return jsonify({"msg": '用户角色(role_id)不能为空'})
    elif Role.query.filter_by(id=role_id).first() is None:
        return jsonify({"msg": '用户角色(role_id)不存在'})
    else:
        first = User.query.filter(or_(User.email == email, User.name == name)).first()
        if first is None:
            try:
                new_user = User(name=name, password=password, email=email, role_id=role_id)
                new_user.gen_pwd(password)
                db.session.add(new_user)
                db.session.commit()

                return jsonify({
                    "data": new_user.id
                })
            except Exception as e:
                db.session.rollback()
                return jsonify({"msg": str(e)})
        else:
            return jsonify({"msg": '用户已({})或({})已存在'.format(name, email)})


@blueprint.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@auth_role(['admin'])
def delete_user(user_id):
    current_user = User.query.filter_by(id=user_id).first()
    current_user.delete_at = datetime.now()
    db.session.add(current_user)
    db.session.commit()
    return jsonify({"data": 'ok'})


@blueprint.route("/role")
@jwt_required()
@auth_role(['admin'])
def all_role():
    return jsonify({
        "data": Role.query.all()
    })


@blueprint.route("/role", methods=["POST"])
@jwt_required()
@auth_role(['admin'])
def add_role():
    name = request.json.get('name', None)
    display_name = request.json.get('displayName', None)
    if name is None:
        return jsonify(msg='角色名称(name)不能为空')
    if display_name is None:
        return jsonify(msg='角色显示名称(display_name)不能为空')
    else:
        first = Role.query.filter(or_(Role.name == name, Role.display_name == display_name)).first()
        if first is None:
            new_role = Role(name=name, display_name=display_name)
            db.session.add(new_role)
            db.session.commit()

            return jsonify({
                "data": new_role.id
            })
        else:
            return jsonify(msg='角色名称({})已存在'.format(name))


@blueprint.route("/login", methods=["POST"])
def login():
    name = request.json.get('name', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(name=name).first()
    # 防止攻击，不要提示过多信息
    msg = "用户名或密码错误"
    if user is None:
        return jsonify(msg=msg)
    elif user.delete_at is not None:
        return jsonify(msg=msg)
    elif user.verify_pwd(password):
        token = create_access_token(identity=user)
        return jsonify(token=token)
    else:
        return jsonify(msg=msg)


@blueprint.route("/me")
@jwt_required()
def me():
    current_user = get_jwt_identity()
    return jsonify({
        "data": current_user
    })
