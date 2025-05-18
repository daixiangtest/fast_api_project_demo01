from dotenv.cli import unset
from pydantic import BaseModel

class loginform(BaseModel):
    username: str
    password: str
    phone: int
    sex:str ="男"
    age:int=18

def login(loginform: loginform):
    print(loginform)
    # .dict已经弃用
    # data=loginform.dict()
    data=loginform.model_dump()
    print(data,type(data))
    # .json()已经弃用
    # data1=loginform.json()
    data1=loginform.model_dump_json()
    print(data1,type(data1))
    # 排除字段展示
    data2=loginform.model_dump(exclude=['password'])
    print(data2,type(data2))
    # 排除默认字段展示
    data3=loginform.model_dump(exclude_unset=True)
    print(data3,type(data3))
if __name__ == '__main__':
    login(loginform=loginform(username="admin", password="123",phone=123456))
