import click
from sanmi.app import create_app
from sanmi.user.models import Role, User
from sanmi.database import db

app = create_app()


@app.cli.command("create-admin")
def create_admin():
    # 插入角色 admin
    admin_role = Role(name="admin", display_name="管理员")
    db.session.add(admin_role)
    db.session.commit()

    # 插入用户 admin:admin
    admin_user = User(name="admin", email="admin@admin.com", role_id=admin_role.id)
    admin_user.gen_pwd("admin")
    db.session.add(admin_user)
    db.session.commit()

    print("enjoy!")
