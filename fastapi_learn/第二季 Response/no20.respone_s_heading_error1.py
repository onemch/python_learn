from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    pass
    pass
    return {'items': items[item_id]}


@app.get('/items-header/{item_id}')
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={
                            "X-Error": "There goes my error"})
    return {'items': items[item_id]}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
