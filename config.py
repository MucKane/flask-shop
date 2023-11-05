# config setting

from os import urandom

class Config:
    # set premeter connect mysql
    MYSQL_DIALECT = 'mysql'
    MYSQL_DRIVER = 'pymysql'
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = 'Wangjiayi1'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'flask_shop'  # instance
    MYSQL_CHARSET = 'utf8mb4'

    # 连接数据库
    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DRIVER}://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
    debug = True
    # 数据盐
    SECRET_KEY = urandom(24)
    # json 不使用ascii编码
    JSON_AS_ASCII = False
    RESTFUL_JSON = {'ensure_ascii': False}
    
class TestConfig(Config):
    pass

class DevelopConfig(Config):
    debug = True

class ProductConfig(Config):
    debug = False

Config_map = {
    'test': TestConfig,
    'develop': DevelopConfig,
    'product': ProductConfig
}