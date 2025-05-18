import uvicorn
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from models_demo import UserInfoModel
from parames_model import UserModel,RegisterModel,LoginModel
app=FastAPI()
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
            "models": ["aerich.models","app_user.manage"],
            "default_connection": "default",
        }
    }
}

register_tortoise(app=app, config=TORTOISE_ORM)
@app.post("/api/register",status_code=201)
async def register(item:RegisterModel):
    #  密码一致性验证
    if item.password!=item.password_confirm:
        raise HTTPException(status_code=400,detail="密码不一致")
    #  验证用户名是否重复
    if await UserInfoModel.filter(userName=item.userName).first():
        raise HTTPException(status_code=400,detail="用户名重复")
    user= await UserInfoModel.create(**item.model_dump())
    return UserModel(**user.__dict__)

@app.post("/api/login")
async def login(item:LoginModel):
    # 验证用户名密码是否正确
    user=await UserInfoModel.get_or_none(userName=item.userName,password=item.password)
    if user:
        return UserModel(**user.__dict__)
    else:
        raise HTTPException(status_code=400, detail="用户名密码错误")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
    """
    项目运行步骤
    首次迁移数据
        初始化模型生成迁移文件
        aerich init -t main.TORTOISE_ORM
        初始化数据库连接并创建表
        aerich init-db
    后续变更模型执行
        修改模型后执行生成新的迁移文件
        aerich migrate
        更改表结构
        aerich upgrade
    运行文件启动服务
    通过fastapi 终端运行
    
    """