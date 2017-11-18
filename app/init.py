from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///YEAH.sqlite3'
app.config['SECRET_KEY']='aRFQWE34hjYUfrgtertA'
db = SQLAlchemy(app)

class estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estudiante = db.Column(db.String(100))
    codigoe = db.Column(db.String(10))

    def __init__(self, estudiante,codigoe):
        self.estudiante = estudiante
        self.codigoe = codigoe

# class profesor(db.Model):
#     id = db.Column('ID', db.Integer, primary_key = True)
#     profesor = db.Column(db.String(100), unique = True)
#     passwdp = db.Column(db.String(20), unique = True)
#
#     def __init__(self, profesor, passwdp):
#         self.profesor = profesor
#         self.passwdp = passwdp
#
# class administrativos(db.Model):
#     id = db.Column('ID', db.Integer, primary_key = True)
#     admin = db.Column(db.String(100), unique = True)
#     passwda = db.Column(db.String(20), unique = True)
#
#     def __init__(self,admin,passwda):
#         self.admin = admin
#         self.passwda = passwda

# @app.route('/',methods = ['GET','POST'])
# def init():
#     if not session.get('logget_in'):
#         render_template('init.html')
#     else:
#         if request.method == 'POST':
#             return render_template('init.html')
#     return render_template('init.html')
#
# @app.route('/login',methods = ['POST'])
# def login():
#     return render_template('login.html')

nombreE = input('nombre: ')
codigo = input('codigo: ')
try:
    nuevo_estudiante = estudiante(estudiante=nombreE,codigoe=codigo)
    db.session.add(nuevo_estudiante)
    db.session.commit()
except Exception as e:
    print(e)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
    db.create_all()