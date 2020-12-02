from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


@app.get('/items/{item_id}', response_model=Dict[str, float])
async def read_item():
    return {'foo': 2.3, 'bar': 3.6}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
