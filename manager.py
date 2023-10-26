from flask_server import create_app,db  
from flask_migrate import Migrate
app = create_app('develop')

# # 创建迁移对象
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()