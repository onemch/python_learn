from fastapi import FastAPI, Cookie


app = FastAPI()


@app.get('/testCookie')
def testCookie(info: str = Cookie(None)):
    return {"info": info}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8077)
