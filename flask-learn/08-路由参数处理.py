from flask import Flask

app = Flask(__name__)


@app.route('/order/<int:order>')
def getOrder(order):
    return 'order : %s' % order


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="2222", debug=True)
