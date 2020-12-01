from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f'Role: {self.name} {self.id}'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'Role: {self.name} {self.id} {self.email} {self.password}'


@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    username = request.args.get('username')
    user = User(name=username, email='', role_id=1)
    db.session.add(user)
    db.session.commit()
    return username


@app.route('/getuser', methods=['GET', 'POST'])
def getuser():
    result = User.query.all()
    # print(result[0])
    return json.dumps(result)


if __name__ == "__main__":
    # db.drop_all()

    # db.create_all()

    app.run(debug=True)
