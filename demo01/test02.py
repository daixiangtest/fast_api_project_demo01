import uvicorn
from fastapi import FastAPI,Query
from typing import Union

"""
fast api 的查询接口参数定义
"""

app = FastAPI()


@app.get("/demo01")
async def demo01(name: str, age: int):
    """
    定义查询参数声明参数名称和参数类型
    :param name:
    :param age:
    :return:
    """
    return {"name": name, "age": age}


@app.get("/demo02")
async def demo02(name: Union[str,None]=None, age: Union[int, str] = None):
    """
    当参数需要支持多个类型时或者未默认参数时通过 name: Union[str,None]=None 写法
    :param name:
    :param age:
    :return:
    """
    return {"name": name, "age": age}

@app.get("/demo03")
async def demo03(token:Union[str,None]=Query(default=None,max_length=5,min_length=3,title='tk',description="token参数描述",alias="tk")):
    """
    当参数需要一些校验时Query 方法中来进行处理
    alias 为参数的别名
    :param token:
    :return:
    """
    return {"token":token}
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
