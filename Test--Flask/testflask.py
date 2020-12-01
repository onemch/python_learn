from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/helloget')
def helloget():
    recArg = request.args.get('name', 'leijun')
    print(recArg)
    return recArg


if __name__ == '__main__':
    app.run(host='127.3.3.3', debug=True)
