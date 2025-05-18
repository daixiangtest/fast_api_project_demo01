"""
关联表直接的创建
"""
import tortoise
from tortoise import fields
from tortoise.models import Model


class UserModel(Model):
    id = fields.IntField(pk=True, description="用户id")
    nice_name = fields.CharField(max_length=255, description="名称")
    user_name = fields.CharField(max_length=255, description="用户名")
    password = fields.CharField(max_length=20, description="密码")

    def __str__(self):
        return self.nice_name

    class Meta:
        table = 'uesr'


class PostModel(Model):
    id = fields.IntField(pk=True, description="id")
    title = fields.CharField(max_length=255, description="标题")
    content = fields.CharField(max_length=255, description="内容")
    # 一对多的关系该字段声明关联的是UserModel模型,关键反查询字段为posts
    user = fields.ForeignKeyField('models.UserModel', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        table = 'post'


class UserInfoModel(Model):
    id = fields.IntField(pk=True, description="id")
    addres = fields.TextField(description="地址")
    age = fields.IntField(description="年龄")
    sex = fields.BooleanField(default="男", description="性别")
    # 1对1 字段声明
    user = fields.OneToOneField("models.UserModel", related_name='user_info')

    def __str__(self):
        return self.user.nice_name

    class Meta:
        table = 'user_info'


class CommunityModel(Model):
    id = fields.IntField(pk=True, description="id")
    name = fields.CharField(max_length=255, description="name")
    # 声明多对多的表格
    user = fields.ManyToManyField('models.UserModel', related_name='communities')

    def __str__(self):
        return self.name

    class Meta:
        table = 'community'


# 连接MySQL数据库在初始化时加载模型类创建表格
async def create_table():
    # 初始化数据库
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['__main__']})
    # 根据模型生成表格
    await tortoise.Tortoise.generate_schemas()


async def create_data():
    # 初始化数据库
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['__main__']})
    # 添加表格数据
    user = await UserModel.create(nice_name="李四", user_name="李四", password="Dx23828")
    await PostModel.create(title="标题2", content="内容2", user=user)
    await UserInfoModel.create(addres="北京", age=19, sex=True, user=user)
    await CommunityModel.create(name="社区1")


async def query_data():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['__main__']})
    # 查询所有数据
    item = await UserModel.all()
    for i in item:
        print(i)
    # 查询指定数据(过滤条件)
    name = await UserModel.filter(nice_name="李四")
    print(name)
    # 查询指定数据(获取单个)多个会报错
    item2 = await UserModel.get(nice_name="张三")
    print(item2.__dict__)
    # 查询单个或空数据
    item2 = await UserModel.get_or_none(nice_name="张三")
    print(item2)


async def update_data():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['__main__']})
    # 修改数据
    # user = await UserModel.get(id=2)
    # 方式1修改整个结构数据
    # await user.update_from_dict({"nice_name": "王二", "user_name": "王2", "password": "Dx23828"})
    # await user.save()
    # 方式2修改部分字段数据
    # user.nice_name="牛二"
    # await user.save()
    # 更改多条数据根据查询集修改
    await UserModel.filter(nice_name="李四").update(nice_name="王二2", user_name="王2")

async def delete_data():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['__main__']})
    # 删除数据1通过查询集可以删除多条数据
    await UserModel.filter(nice_name="王二2").delete()
    # 删除数据2通过获取数据对象删除单条数据
    # user=await UserModel.get(id=2)
    # await user.delete()
# 初步运行方法创建对应模型的表格
if __name__ == '__main__':
    # tortoise.run_async(create_data())
    # tortoise.run_async(query_data())
    # tortoise.run_async(update_data())
    tortoise.run_async(delete_data())
