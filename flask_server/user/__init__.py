from flask import Blueprint


# 创建蓝图对象
user_bp = Blueprint('user', __name__,url_prefix='/user')


# 导入视图
from . import views
