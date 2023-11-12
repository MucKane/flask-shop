from flask_server import create_app,db  
from flask_migrate import Migrate
from flask_cors import CORS

app = create_app('develop')
# CORS(app, supports_credentials=True) # 解决前后端跨域问题
# 创建迁移对象
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()