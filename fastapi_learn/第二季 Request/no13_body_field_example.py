from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


class item(BaseModel):
    id: int = Field(description='id Param')
    name: str = Field(min_length=3, max_length=8, description='name Param')
    price: float = Field(ge=0, le=50, description='price Param')


@app.put('/item/{id}')
async def read_item(
    item: item = Body(...,
                      example={
        'id': 123,
                          'name': 'asdfsa',
                          'price': 18.6,
                          'nba': 'cba'

                          }
                      )  # 单主题 加个 embed
):
    result = dict()
    result.update({'item': item})
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
