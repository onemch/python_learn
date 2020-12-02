from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.post('/user')
async def files(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    print(f'username : {username}')
    print(f'password : {password}')
    return templates.TemplateResponse('no5_static.html', {'request': request, 'username': username, 'password': password})


@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse('no5_static.html', {'request': request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
