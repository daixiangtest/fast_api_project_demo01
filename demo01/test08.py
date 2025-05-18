import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

"""
响应模型的基本定义
"""
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    phone: int


# 响应模型的基本定义（主要用于展示接口文档的应答类型）
@app.get("/index", response_model=Item)
async def index():
    return {"name": "index", "price": 10.1, "phone": 100}


"""
嵌套类型的模型定义
"""


class shangping(BaseModel):
    id: int
    name: str
    price: float


class dingdan(BaseModel):
    dingdan_id: int
    shangping: List[shangping]
    status: bool


@app.get("/dingdan", response_model=dingdan)
async def get_dingdan():
    return {"dingdan_id": 1,
            "shangping": [{"id": 1, "name": "apple", "price": 10.1},
                          {"id": 1, "name": "blanla", "price": 12.1}],
            "status": True}


"""
复杂模型的继承类
"""


class userInfo(BaseModel):
    username: str


class login(userInfo):
    passwd: str


class register(login):
    phone: int
    email: str
    address: str


@app.post("/register", response_model=userInfo)
async def register(user_info: register):
    return {"username": user_info.username}


"""
定义响应数据的类型（默认为json）
"""


@app.get("/login", response_class=HTMLResponse)
async def login():
    data = """
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
    <h1>登录成功</h1>
</body>
</html>
    """
    return HTMLResponse(data)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
