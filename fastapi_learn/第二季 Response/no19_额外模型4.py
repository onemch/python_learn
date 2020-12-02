from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": 'fox', "description": "this is fox"},
    {"name": 'red', "description": "this is red"}
]


@app.get('/items/{item_id}', response_model=List[Item])
async def read_item():
    return items


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
