import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.post("/login",summary="登录接口")
async def login(username: str, password: str):
    return {"token": "<PASSWORD>","message":"success","username":username,"password":password}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)