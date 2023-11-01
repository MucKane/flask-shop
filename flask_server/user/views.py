from flask_server.user import user_bp
from flask_server.models import User
from flask import request
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
  password = request.get_json().get("pwd")
  # 判断是否传递数据完整
  if not all([name, password]):
    return {'status': 400, 'msg': '参数不完整'}
  else:
    # 通过用户名获取用户对象
    user = User.query.filter(name == name).first()
    # 判断用户是否存在
    if user:
      # 判断密码是否正确
      if user.check_password(password):
        return {'status': 200, 'msg': '登录成功'}
    return {'status': 400, 'msg': '用户名或密码错误'}
