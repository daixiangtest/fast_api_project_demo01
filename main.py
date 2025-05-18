from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
if __name__ == '__main__':
    import requests
    resp=requests.post('http://127.0.0.1:8000/updte',headers={"token2":""},data={"dx":12345},cookies={"tk":"12345as"})
    print(resp.text)