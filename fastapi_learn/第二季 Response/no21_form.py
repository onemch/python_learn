from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.post('/user/')
async def getUser(request: Request, username: str = Form(...), password: str = Form(...)):
    print('username : ', username)
    print('password : ', password)

    return templates.TemplateResponse('no3_show.html', {'request': request, 'username': username, 'password': password})


@app.get('/')
async def showUserForm(request: Request):
    return templates.TemplateResponse('no3_form.html', {'request': request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
