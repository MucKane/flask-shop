from flask_server.menu import menu_api
from flask_restful import Resource
from flask_server import models
from flask import request

class Menu(Resource):
    def get(self):
        # 根据前端页面的要求设计来决定什么机构
        type_ = request.args.get('type_')
        if(type_ == 'tree'):
            # 树形结构获取
            # 获取树形结构第一层
            menu_list = models.Menu.query.filter(models.Menu.level == 1).all()
            menu_data = []
            # 把获取的结构遍历输入到data中
            for m in menu_list:
                menu_data.append(m.to_dict_tree())
            return {'status':200,'msg':'获取成功','data':menu_data}
        
        # 如果是列表结构
        else:
            menu_list = models.Menu.query.filter(models.Menu.level != -1).all()
            menu_data = []
            # 把获取的结构遍历输入到data中
            for m in menu_list:
                menu_data.append(m.to_dict_list())
            return {'status':200,'msg':'获取成功','data':menu_data}
# 映射
menu_api.add_resource(Menu,'/menus/')