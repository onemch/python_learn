from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(json_compatible_item_data)
    print(type(json_compatible_item_data))
    print(fake_db)
    print(type(fake_db))


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
