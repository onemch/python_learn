from fastapi import FastAPI
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    tel: str = None


app = FastAPI()


@app.post('/person')
async def getPerson(person: Person):
    print(person.dict())
    return person


@app.post('/person/{id}')
async def getMore(id: int, person: Person, q: str = None):
    result = {'id': id,  **person.dict()}
    if q:
        result.update({'q': q})
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
