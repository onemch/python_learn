from fastapi import FastAPI

from starlette.requests import Request
from starlette.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            'message': f"Oops! {exc.name} did something. There goes a rainbow..."}
    )


@app.get('/unicorn/{name}')
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {"unicorn_name": name}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8077)
