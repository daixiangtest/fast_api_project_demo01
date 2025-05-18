import json

import uvicorn
from fastapi import FastAPI,Cookie,Header,Request
from pydantic import BaseModel,Field
from typing import Annotated,Union
"""
json参数的定义
"""
class address(BaseModel):
    # 嵌套结构体时定义子级结构体在
    city: str
    state: str
    country: list[str]  #声明该字段是个列表且列表里面的值是个字符串
# 定义json结构体的模型类
class zhuce(BaseModel):
    """
    参数的结构体必须继承pydantic的模型类来进行参数校验
    """
    name: str
    passwd:str=Field(default=None,max_length=10,min_length=3)  # 参数校验规则可以通过Field 方法来进行校验
    phone:int
    address:address


app=FastAPI()

@app.post("/zhuce")
async def zhuce(item:zhuce):
    return item

# cookie 参数的传递
@app.get("/varify")
async def varify(token:Annotated[str,None,Cookie()]=None):
    return token

# 请求头参数传递
@app.get("/header")
async def header(token1:Union[str,None]=Header(min_length=5,default=None)):
    return token1

# fast api 也可以不进行参数校验获取整个请求参数的对象
@app.post("/updte")
async def updte(request:Request):
    # 获取请求体信息，为byts 字段类型
    # body = await request.body()
    # print(body)
    # 获取的表单参数 返回dict 类型
    # body=await request.form()
    # 获取的json数据 返回dict
    json_data=await request.json()
    # print(body,type(body))
    return {"header":request.headers,"cookie":request.cookies,"body":json_data}
if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)