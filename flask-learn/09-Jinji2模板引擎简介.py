from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    msg = 'www.safsafdsaf.com'
    return render_template('index9.html', msg=msg)


if __name__ == "__main__":
    app.run()
