import uvicorn
from fastapi import FastAPI,Path
from typing import Union
"""
路径参数 通过{参数名}来声明
参数的校验规则通过Path 方法来实现校验
"""

app=FastAPI()


@app.get('/demo/{env_id}')
async def test(env_id:Union[int,str] ):
    return {"路径参数":env_id}

@app.get('/test/{pro_id}')
async def test(pro_id:int=Path(gt=1,lt=6)):
    return {"路径参数":pro_id}


if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)