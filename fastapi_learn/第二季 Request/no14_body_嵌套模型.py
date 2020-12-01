from typing import List, Set
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class item(BaseModel):
    id: int
    name: str = None
    price: float = None
    tag0: list = []
    tag1: List[str] = []
    tag2: Set[str] = set()


@app.put('/item/{id}')
async def read_item(
    item: item
):
    result = dict()
    result.update({'item': item})
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
