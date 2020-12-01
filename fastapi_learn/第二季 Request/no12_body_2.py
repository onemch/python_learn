from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI()


class item(BaseModel):
    id: int
    name: str
    price: float


@app.put('/item/{id}')
async def read_item(
    id: int = Path(..., ge=50, le=100),
    item: item = None,
    q: str = Body(...)
):
    result = {'id': id}
    if item:
        result.update({'item': item})
    if q:
        result.update({'q': q})
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
