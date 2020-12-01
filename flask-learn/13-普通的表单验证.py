from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = '123456'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username)

        if not all([username, password, password2]):
            # print('参数不完整')
            flash(u'参数不完整')
        elif password == password2:
            # print('密码不一致')
            flash(u'密码不一致')
        else:
            return 'ok'

    return render_template('index13.html')


if __name__ == "__main__":
    app.run(debug=True)
