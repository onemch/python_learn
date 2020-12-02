from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


@app.post('/user/')
async def create_user(*, user: UserIn):
    user = UserOut(**user.dict())
    return user


@app.post('/user0/', response_model=UserOut)
async def create_user0(*, user: UserIn):
    return user


@app.post('/user1/')
async def create_user1(*, user: UserIn):
    result1 = UserOut(username='123', email='123@qwe.com', full_name='789')
    result2 = UserOut(**user.dict())
    return result1, result2


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
