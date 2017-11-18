from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///YEAH.sqlite3'
app.config['SECRET_KEY']='aRFQWE34hjYUfrgtAfertA'
db = SQLAlchemy(app)

class Estudiante(db.Model):
    id = db.Column('ID', db.Interger, primary_key=True)
    estudiante = db.Column(db.String(100), unique = True)
    passwdwe= db.Column(db.String(20), unique = True)
    codigoe = db.Column(db.String(10),unique = True)

    def __init__(self, estudiante,passwde,codigoe):
        self.estudiante = estudiante
        self.passwde = passwde
        self.codigoe = codigoe

class Profesor(db.Model):
    id = db.Column('ID', db.Interger, primary_key = True)
    profesor = db.Column(db.String(100), unique = True)
    passwdp = db.Column(db.String(20), unique = True)
    codigop = db.Column(db.String(10), unique = True)

    def __init__(self, profesor, passwdp,codigop):
        self.profesor = profesor
        self.passwdp = passwdp
        self.codigop = codigop


@app.route('/')
def init():

    return render_template('init.html')

if __name__ == '__main__':
    app.run(debug=True,port=0000)