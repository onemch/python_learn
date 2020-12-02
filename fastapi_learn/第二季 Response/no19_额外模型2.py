from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserOut(UserBase):
    pass


class UserIn(UserBase):
    password: str


@app.post('/user0/', response_model=UserOut)
async def create_user0(*, user: UserIn):
    return user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
