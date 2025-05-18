"""
tortoise orm 框架模型
1，pip install tortoise-orm
2.pip install tortoise-orm[asyncodbc]
3.pip install aiomysql
"""
from sys import modules

import tortoise
from tortoise import fields, run_async
from tortoise.models import Model

# 继承model 类创建数据库表的模型类
class Table01(Model):
    id = fields.IntField(pk=True)
    name=fields.CharField(max_length=100)
    class Meta:
        table_name = 'table01'

# 连接MySQL数据库在初始化时加载模型类创建表格
async def create_table():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                        modules={'models': ['__main__']})
    await tortoise.Tortoise.generate_schemas()

# 初步运行方法创建对应模型的表格
run_async(create_table())