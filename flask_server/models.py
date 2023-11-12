# Desc: 数据库模型
# Date: 2023/10/26
# todo: 修改密码存储方式 防止直接被盗取

from werkzeug.security import generate_password_hash,check_password_hash
from flask_server import db
from datetime import datetime

class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class User(db.Model,BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    pwd = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)

    @property
    def password(self):
        return self.pwd
    
    @password.setter
    def password(self,pwd):
        self.pwd = generate_password_hash(pwd)

    def check_password(self,pwd):
        return check_password_hash(self.pwd,pwd)
    
# TODO:菜单模型
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    level = db.Column(db.Integer, default=1)
    path = db.Column(db.String(50))
    pid = db.Column(db.Integer, default=-1)
    children = db.relationship('Menu')

    # 传递回前端要以json的形式
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'level':self.level,
            'path':self.path,
            'pid':self.pid,
            'children':[child.to_dict() for child in self.children]
        }