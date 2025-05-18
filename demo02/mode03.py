import tortoise
from tortoise import fields
from tortoise.models import Model
from mode02 import UserModel, PostModel

"""
关联数据表查询
"""


async def one_to_one():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    # 1 对1 查询 prefetch_related方法来获取关联数据
    user = await UserModel.get_or_none(id=1).prefetch_related('user_info')
    if user and getattr(user, 'user_info'):
        users = {"id": user.id,
                 "nice_name": user.nice_name,
                 "user_name": user.user_name,
                 "user_info": {"addres": user.user_info.addres, "age": user.user_info.age, "sex": user.user_info.sex}}
        print(users)

async def one_to_one2():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    user = await UserModel.get_or_none(id=1).prefetch_related('user_info')
    user_info=await user.user_info.all().values("addres","age")
    if user and getattr(user, 'user_info'):
        users = {"id": user.id,
                 "nice_name": user.nice_name,
                 "user_name": user.user_name,
                 "user_info": user_info
        }
        print(users)
async def one_to_many():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    user = await UserModel.get_or_none(id=1).prefetch_related('posts')
    if user and getattr(user, 'posts'):
        users = {"id": user.id,
                 "nice_name": user.nice_name,
                 "user_name": user.user_name,
                 "posts": []
        }
        for post in user.posts:
            users['posts'].append({"id": post.id, "title": post.title, "content": post.content})
        print(users)
async def one_to_many2():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',
                                 modules={'models': ['mode02']})
    user = await UserModel.get_or_none(id=6).prefetch_related('posts')
    # 查询多条关联数据时可以先获取关联的所有数据使用 Values 方法指定返回的字段，返回一个列表数组
    pots=await user.posts.all().values("id","title","content")
    if user and getattr(user, 'posts'):
        users = {"id": user.id,
                 "nice_name": user.nice_name,
                 "user_name": user.user_name,
                 "posts": pots
        }
        print(users)
async def many_to_many():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',modules={'models': ['mode02']})
    user = await UserModel.get_or_none(id=1).prefetch_related('communities')
    if user and getattr(user, 'communities'):
        users = {"id": user.id,
                 "nice_name": user.nice_name,
                 "user_name": user.user_name,
                 "communities": []
        }
        for community in user.communities:
            users['communities'].append({"id": community.id, "name": community.name})
        print(users)

async def many_to_one():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',modules={'models': ['mode02']})
    post=await PostModel.get_or_none(id=1).prefetch_related('user')
    if post and getattr(post, 'user'):
        users = {"id": post.id,
                 "title": post.title,
                 "content": post.content,
                 "user": {"id": post.user.id,
                          "nice_name": post.user.nice_name,
                          "user_name": post.user.user_name}
                 }
        print(users)

async def many_to_one2():
    await tortoise.Tortoise.init(db_url='mysql://root:123456@127.0.0.1:3306/demo',modules={'models': ['mode02']})
    # 从一到多方向查询关联时，select_related方法来获取关联数据
    post=await PostModel.get_or_none(id=1).select_related('user')
    if post and getattr(post, 'user'):
        users = {"id": post.id,
                 "title": post.title,
                 "content": post.content,
                 "user": {"id": post.user.id,
                          "nice_name": post.user.nice_name,
                          "user_name": post.user.user_name}
                 }
        print(users)

if __name__ == '__main__':
    tortoise.run_async(many_to_one())
    tortoise.run_async(many_to_one2())
