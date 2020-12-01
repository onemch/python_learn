from fastapi import FastAPI

app = FastAPI()


@app.get('/me/xx')
async def readMe():
    return {'me': 'me'}


@app.get('/me/{item}')
def readItem(item: str):
    return {'item': item}


# @app.get('/me/xx')
# async def readMe():
#     return {'me': 'me'}

@app.get('/')
def index():
    return {'index': 'index'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
