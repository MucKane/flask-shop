# token生成
# TODO:生成token 加密算法 pyjwt 密钥:SECRET_KEY
# time: 2023/11/5
# author: wangjiayi
import jwt
from flask import current_app

# 生成token
def generate_token(user_id):
    # 生成token
    # 参数:用户id
    # 返回值:token
    # 导入密钥
    secret_key = current_app.config['SECRET_KEY']
    # 生成token
    # 传递的参数一定要以字典的形式传递 否则报错
    token = jwt.encode({'user_id':user_id},secret_key,algorithm='HS256')
    # 返回token
    return token

# 校验token 
def check_token(token):
    # 校验token
    # 参数:token
    # 返回值:用户id
    # 导入密钥
    secret_key = current_app.config['SECRET_KEY']
    # 校验token
    try:
        # 解码token
        data = jwt.decode(token,secret_key,algorithms=['HS256'])
        # 返回用户id
        return data['user_id']
    except:
        # 校验失败
        return None