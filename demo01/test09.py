import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse,Response


app=FastAPI()


"""
cookie 应答
"""

@app.get("/cookie1")
async def cookie1(response:Response):
    response.set_cookie("cookie1", "test001")
    response.set_cookie("cookie2", "test002")
    return{"message":"success"}

@app.get("/cookie2")
async def cookie2():
    result={"message":"success"}
    response=JSONResponse(result)
    response.set_cookie("cookie2", "test003")
    return response

"""
响应头设置
"""
@app.get("/header1")
async def header(response:Response):
    response.headers["Content-Type"] = "application/json"
    response.headers["key"] = "test01"
    return{"message":"success"}

@app.get("/header2")
async def header2():
    result={"message":"success"}
    response=JSONResponse(result)
    response.headers["Content-Type"] = "application/json"
    response.headers["key"] = "test03"
    return response
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)