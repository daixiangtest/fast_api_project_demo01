import uvicorn
from fastapi import FastAPI,Form

"""
表单参数通过 From() 方法来声明并对参数进行校验
"""
app=FastAPI()

@app.post("/login")
async def login(a:int,user:str=Form(),pwd:str=Form()):
    return {"user":user,"pwd":pwd,"a":a}

@app.post("/register")
async def student(name:str=Form(min_length=2,max_length=5),age:int=Form(gt=0,lt=20),phone:str=Form(min_length=10,max_length=13)):
    return {"name":name,"age":age,"phone":phone}

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)