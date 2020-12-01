from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List, Dict

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple")
async def createImages(*, images: List[Image]):
    return images


@app.post("/random_dict")
async def create_random_dict(info: Dict[int, float]):
    return info


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
