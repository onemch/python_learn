from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():

    msg = 'www.safsafdsaf.com'
    mylist = [1, 2, 3, 4, 5]
    mydict = {'name': 'jyui', 'age': 12}
    return render_template('index10.html', mylist=mylist, mydict=mydict)


if __name__ == "__main__":
    app.run(debug=True)
