from flask_server.user import user_bp
from flask_server.models import User
# 创建视图
@user_bp.route('/')
def index():
  return 'Hello User!!'
