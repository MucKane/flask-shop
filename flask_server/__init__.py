# Author: wjy
# Time: 2023/10/25 21:00 
# todo : 项目启动文件

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config_map


# 创建sqlalchemy对象
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # 加载配置信息
    Config = Config_map.get(config_name)
    # 通过类加载配置信息
    app.config.from_object(Config)
    # 初始化db
    db.init_app(app)
    # 获取user蓝图对象
    from flask_server.user import user_bp
    # 注册蓝图
    app.register_blueprint(user_bp)
    # 返回实例
    return app
