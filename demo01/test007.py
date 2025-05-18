import uvicorn
from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
from typing import Union
"""
增删查改常规接口的默认应答码定义
"""

app = FastAPI()

# 模拟数据库数据
cases = [
    {"id": 1, "name": "张三", "age": 10},
    {"id": 2, "name": "李四", "age": 13},
    {"id": 3, "name": "王五", "age": 18}
]
# 定义json对象
class caseModel(BaseModel):
    id: int
    name: str
    age: int

@app.get("/item",status_code=200)
# 查询接口
async def read_item():
    return cases

@app.get("/item/{id}",status_code=200)
# 查询接口
async def read_item(id: Union[int,None]=None):
    if id ==0:
        return cases
    else:
        for case in cases:
            if case["id"] == id:
                return case
        else:
            raise HTTPException(status_code=404,detail="数据不存在")

@app.post("/item",status_code=201)
# 查询所有数据
async def read_item(case: caseModel):
    cases.append(case.model_dump())
    return cases

@app.put("/item",status_code=200)
# 更新数据
async def read_item(id:int,case: caseModel):
    for index,cas in enumerate(cases):
        if cas["id"] == id:
            cases[index]=case.model_dump()
            return cases
@app.delete("/item/{id}",status_code=204)
# 删除接口 204 只返回状态码，不返回应答数据
async def read_item(id:Union[int,None]):
    for i in cases:
        if i["id"] == id:
            cases.remove(i)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)