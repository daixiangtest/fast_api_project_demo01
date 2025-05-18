"""
数据迁移
tortoise 数据库模型实现项目迁移可以使用 aerich 第三方库来实现迁移（生成迁移记录方便数据库的变更）
"""
import uvicorn
from fastapi import FastAPI
from tortoise import Model
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise


app=FastAPI()

class UserInfoModel(Model):
    id = fields.IntField(pk=True, description="id")
    userName = fields.CharField(max_length=255, description="用户名")
    addres = fields.TextField(description="地址")
    age = fields.IntField(description="年龄")
    sex = fields.BooleanField(default="男", description="性别")
    email=fields.CharField(max_length=255, description="邮箱")
    def __str__(self):
        return self.userName

    class Meta:
        table = 'users'
# 迁移配置信息
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "123456",
                "database": "demo02",
            }
        }
    },
    "apps": {
        "models": {
            "models": ["aerich.models","main"],
            "default_connection": "default",
        }
    }
}

# 注册ORM 模型
register_tortoise(app=app, config=TORTOISE_ORM)

if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000, reload=True)

    """
    cd demo03
    迁移数据命令
    首次执行终端命令
        初始化模型生成迁移文件
        aerich init -t main.TORTOISE_ORM
        初始化数据库连接并创建表
        aerich init-db
    后续执行
        修改模型后执行生成新的迁移文件
        aerich migrate
        更改表结构
        aerich upgrade
    每次迁移的记录都会记录在默认的aerich 表中
    
    """