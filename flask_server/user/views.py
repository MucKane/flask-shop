from flask_server.user import user_bp,user_api
from flask_server import models,db
from flask import request
from flask_restful import Resource
import re
from flask_server.utils.token import generate_token,check_token
# 创建视图
@user_bp.route('/')
def index():
  return 'Hello User!!'

# 登录功能
@user_bp.route('/login/',methods=['POST'])
def login():
  # 获取用户名
  # name = request.form.get('name')  # content-type: application/x-www-form-urlencoded
  name = request.get_json().get("name") # content-type: application/json
  # 获取密码
  password = request.get_json().get("password")
  # 判断是否传递数据完整
  if not all([name, password]):
    return {'status': 400, 'msg': '参数不完整'}
  else:
    # 通过用户名获取用户对象
    user = models.User.query.filter(name == name).first()
    # 判断用户是否存在
    if user:
      # 判断密码是否正确
      if user.check_password(password):
        # 生成token
        token = generate_token(user.id)
        return {'status': 200, 'msg': '登录成功', 'token': token}
    return {'status': 400, 'msg': '用户名或密码错误'}

# 注册功能
class Users(Resource):
  def get(self):
    pass
  def post(self):
    # 注册
    # 接受用户信息
    name = request.get_json().get('name')
    pwd = request.get_json().get('pwd')
    rel_password = request.get_json().get('rel_password')
    # 验证数据的合法性
    if not all([name, pwd, rel_password]):
      return {'status': 400, 'msg': '参数不完整'}
    # 判断两次密码是否一致
    if pwd != rel_password:
      return {'status': 400, 'msg': '两次密码不一致'}
    # 接受手机号与邮箱
    phone = request.get_json().get('phone')
    email = request.get_json().get('email')
    # 验证手机号格式
    if not re.match(r'^1[3456789]\d{9}$',phone):
      return {'status': 400, 'msg': '手机号格式不正确'}
    # 验证邮箱格式
    if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',email):
      return {'status': 400, 'msg': '邮箱格式不正确'}
  
    # 判断用户名是否存在
    try:
      user = models.User.query.filter(name == name).first()
      if user:
        return {'status': 400, 'msg': '用户名已存在'}
    except Exception as e:
      # 没有已经存在的用户 逻辑继续进行
      pass
    
    # 创建对象
    user = models.User(name=name, password=pwd, phone=phone, email=email)
    # 保存到数据库
    db.session.add(user)
    db.session.commit()
    return{'status': 200, 'msg': '注册成功'}
  

user_api.add_resource(Users,'/users/')