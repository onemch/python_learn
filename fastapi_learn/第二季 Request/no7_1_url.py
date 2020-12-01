from fastapi import FastAPI
from enum import Enum


class Name(str, Enum):
    ZhangSan = '张三'
    LiSi = '李四'
    WangWu = '王五'


app = FastAPI()


@app.get('/{who}')
async def Who(who: Name):
    if(who == Name.ZhangSan):
        return {'who': who, 'Name': '张三'}
    if(who.value == 'LiSi'):
        return {'who': who, 'Name': '李四'}
    else:
        return {'who': who, 'Name': '王五'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
