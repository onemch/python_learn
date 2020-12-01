from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List


class Person(BaseModel):
    name: str
    age: int
    tel: str = None


app = FastAPI()


@app.get('/item1')
async def getitem1(item: str = Query(None, min_length=3, max_length=5, regex='^nice')):
    print(item)
    return item


@app.get('/item2')
async def getitem2(item: List[str] = Query(['qqq', 'wwww'])):
    print(item)
    return item


@app.get('/item3')
async def getitem3(item: str = Query(None, alias='item_alias')):
    result = [123]
    if(item):
        result.append(item)
    print(result)
    return result


@app.get('/item4')
async def getitem4(item: str = Query(None, deprecated=True)):
    result = [123]
    if(item):
        result.append(item)
    print(result)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
