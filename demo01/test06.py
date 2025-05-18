import os

import uvicorn
from fastapi import FastAPI, UploadFile, File,Form,HTTPException
from typing import List
"""
文件上传接口
"""
FILE_DIR="./files"
app=FastAPI()

@app.post("/upload/file")
# 上传单个文件
async def upload_file(file: UploadFile = File()):
    return {"文件类型":file.content_type,"文件名称":file.filename}

@app.post("/upload/files")
# 上传多个文件
async def upload_files(files: List[UploadFile]):
    datas=[]
    for file in files:
        datas.append({"文件类型":file.content_type,"文件名称":file.filename})
    return datas

@app.post("/upload/filename")
# 文件上传包含其他的参数 文件上送是通过表单的形式上送的，所以不支持json 的参数
async def upload_filename(file:UploadFile,name:str=Form()):
    return {
        "name":name,"文件类型":file.content_type,"文件名称":file.filename
    }
@app.post("/download/file")
# 文件的常规校验和保存
async def download_file(file: UploadFile):
    # 判断文件的大小
    print(file.size)
    if file.size>=600000000:
        raise HTTPException(status_code=400,detail={"message":"文件太大"})
    elif file.content_type not in ["image/jpeg","image/png"]:
        raise HTTPException(status_code=400,detail={"message":"文件格式不支持"})
    elif file.filename in os.listdir(FILE_DIR):
        raise HTTPException(status_code=401,detail="文件已经存在")
    with open(FILE_DIR+"/"+file.filename, "wb") as f:
        f.write(file.file.read())
        f.close()
        return {"message":"文件保存成功"}
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)