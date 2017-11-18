from random import randint
from flask import Flask,render_template,redirect,request,session,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///YEAH.sqlite3'
app.config['SECRET_KEY']='aRFQWE34hjYUfrgtertA'
db = SQLAlchemy(app)
"""En esta base de dato se van a ir guardando los codigos generados para despues ser validados"""
class Codigo(db.Model):
    id = db.Column('ID', db.Integer, primary_key=True)
    codigo = db.Column(db.String(5))
    def __init__(self,codigo):
        self.codigo = codigo

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estudiante = db.Column(db.String(100),unique = True)
    cedulae = db.Column(db.String(10), unique=True)
    passwd= db.Column(db.String(20))
    def __init__(self, estudiante,cedulae,passwd):
        self.estudiante = estudiante
        self.cedulae = cedulae
        self.passwd = passwd

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    asistencia = db.Column(db.String(20))
    nom_estudiante = db.Column(db.String(20),unique = True)
    def __init__(self,asistencia,nom_estudiante):
        self.asistencia = asistencia
        self.nom_estudiante = nom_estudiante

class Profesor(db.Model):
    id = db.Column('ID', db.Integer, primary_key = True)
    profesor = db.Column(db.String(100), unique = True)
    cedulap = db.Column(db.String(10),unique = True)
    passwdp = db.Column(db.String(20))

    def __init__(self, profesor, cedulap, passwdp):
        self.profesor = profesor
        self.passwdp = passwdp
        self.cedulap = cedulap

# nombreE = input('nombre: ')
# cedulap = input('cedula: ')
# passwd = input('pass: ')
#
# id_docente = (str(randint(1000, 3000)))
# nuevo_codigo = Codigo(id_docente)
# nuevo_estudiante= Estudiante(nombreE,cedulap,passwd)
# #nuevo_profesor = Profesor(nombreE, cedulap, passwd)
# db.session.add(nuevo_codigo)
# #db.session.add(nuevo_profesor)
# db.session.add(nuevo_estudiante)
# db.session.commit()


@app.route('/',methods = ['GET','POST'])
def init():
    if not session.get('logged_in'):
        render_template('init.html')
    # else:
    #     if request.method == 'POST':
    #         print('esta logeado')
    #         return render_template('init.html')
    return render_template('init.html')

@app.route('/estudiante',methods = ['GET','POST'])
def estudiante():
    if not session.get('logged_in'):
        render_template('login.html')
    else:
        if request.method == 'POST':
            print('entre aqui')
            return render_template('init.html')
        nombre = session.get('estudiante')
        return render_template('estudiante.html',nombre=nombre)
    return render_template('estudiante.html')

@app.route('/ruta',methods = ['GET','POST'])
def ruta():
    if request.method == 'POST':
        codigo = request.form['codigo']
        data = Codigo.query.filter(Codigo.codigo==codigo).first()
        if data is not None:
            nombre = session.get('estudiante')
            print(nombre)
            session['logged_in'] = True
            asistio = 'asistio'
            nueva_asistencia = Asistencia(asistencia=asistio, nom_estudiante=nombre)
            db.session.add(nueva_asistencia)
            db.session.commit()
            print('si existe')
            mensaje = 'registro completo'
            return render_template('estudiante.html', mensaje=mensaje,nombre = nombre)
    else:
        return render_template('estudiante.html')
    return render_template('login.html')

@app.route('/profesor',methods = ['GET','POST'])
def profesor():
    if not session.get('logged_in'):
        render_template('init.html')
    else:
        if request.method == 'POST':
            print('esta logeado')
            return render_template('init.html')
        nombre = session.get('profesor')
        return render_template('profesor.html',nombre=nombre,estudiante = Asistencia.query.all())
    return render_template('profesor.html')

@app.route('/login/estudiante',methods = ['GET','POST'])
def login():
    """validacion de login"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        cedula = request.form['cedula']
        pwd = request.form['pwd']
        try:
            data = Estudiante.query.filter(Estudiante.cedulae==cedula,Estudiante.passwd==pwd).first()
            if data is not None:
                session['logged_in'] = True
                session['estudiante'] = data.estudiante
                return redirect(url_for('estudiante'))
            else:
                return render_template('login.html')
        except Exception as e:
            print(e)
            return render_template('login.html')

@app.route('/login/profesor',methods = ['GET','POST'])
def loginp():
    """validacion de login"""
    if request.method == 'GET':
        return render_template('loginp.html')
    else:
        cedula = request.form['cedula']
        pwd = request.form['pwd']
        try:
            data = Profesor.query.filter(Profesor.cedulap==cedula,Profesor.passwdp==pwd).first()
            if data is not None:
                session['logged_in'] = True
                session['profesor'] = data.profesor
                return redirect(url_for('profesor'))
            else:
                return render_template('loginp.html')
        except Exception as e:
            print(e)
            return render_template('loginp.html')

@app.route('/logout',methods = ['GET','POST'])
def logout():
    """cerrar sesion"""
    session['logged_in'] = False
    return redirect(url_for('init'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,port=5000)
