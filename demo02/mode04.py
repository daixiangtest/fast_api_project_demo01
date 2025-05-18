"""
数据排序，分页，聚合查询，原生SQL查询
"""
import tortoise
from tortoise.functions import Count, Avg, Max, Min

from mode02 import UserModel,PostModel


# 排序
async def sort():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    # 升序
    users = await UserModel.all().order_by('id')
    print(users)
    # 降序
    users = await UserModel.all().order_by('-id')
    print(users)
    # 多字段排序
    users = await UserModel.all().order_by('-id', 'user_name')
    print(users)
    # 多字段排序
    users = await UserModel.all().order_by('-id', '-user_name')
    print(users)
    # 多字段排序
    users = await UserModel.all().order_by('-id', 'user_name')
    print(users)
    # 排序后展示指定字段
    users = await UserModel.all().order_by('-id').values('id', 'user_name')
    print(users)

# 条件过滤
async def filter_values():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    users = await UserModel.filter(id__gt=1).values("id","user_name")
    print(users)
    users = await UserModel.filter(id__lt=6).values("id","user_name")
    print(users)
    #  模糊查询
    users = await UserModel.filter(user_name__contains="e").values("id","user_name")
    print(users)
    # 先获取所有数据，再进行过滤
    users = await UserModel.all().filter(user_name__icontains="e").values("id","user_name")
    print(users)

#分页查询
async def pagination(page:int,size:int):
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    # 分页查询 offset代表从第几行数据开始 limit代表取多少条数据
    users = await UserModel.all().offset((page-1)*size).limit(size).values("id","user_name")
    print(users)


# 聚合查询
async def aggregate():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    # 统计用户信息 annotate()为聚合函数的方法 Count(统计字段)为统计函数 user_info 为统计后展示的字段名称
    users=await  UserModel.annotate(user_info=Count('user_info')).all().values("id","user_name","user_info")
    print(users)
    # 平均值
    users = await UserModel.annotate(post_id=Avg('posts__id')).all().values("id", "user_name", "post_id")
    print(users)
    # 最大值
    users = await UserModel.annotate(post_id=Max('posts__id')).all().values("id", "user_name", "post_id")
    print(users)
    # 最小值
    users = await UserModel.annotate(post_id=Min('posts__id')).all().values("id", "user_name", "post_id")
    print(users)

# 原生SQL查询
async def raw_sql(sql:str):
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    db=tortoise.Tortoise.get_connection('default')
    # 执行查询sql
    users=await db.execute_query(sql)
    print(users)
    # 将查询结果转换为字典
    users=await db.execute_query_dict(sql)
    print(users)



if __name__ == '__main__':
    # tortoise.run_async(filter_values())
    # tortoise.run_async(pagination(3,3))
    # tortoise.run_async(aggregate())
    tortoise.run_async(raw_sql("select * from uesr"))
