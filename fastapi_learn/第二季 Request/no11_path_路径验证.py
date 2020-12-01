from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get('/item/{item_id}')
async def read_item(
    item_id: int = Path(..., ge=50, le=100)
):
    return item_id


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
