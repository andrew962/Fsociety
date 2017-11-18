import sqlite3
from random import randint

db = sqlite3.connect('estudiantes')
cursor = db.cursor()
try:
   cursor.execute('''CREATE TABLE docentes(id INTEGER PRIMARY KEY, id_docente TEXT, nombre TEXT)''')
except Exception as e:
    print(e)
    pass

id_docente =("1000"+str(randint(1000,3000)))
docentes = input("nombre: ")
cursor.execute('''INSERT INTO docentes (id_docente, nombre) VALUES(?,?) ''',(id_docente, docentes))
db.commit()
#try:
 # cursor.execute('''CREATE TABLE  estudiantes(id INTEGER PRIMARY KEY, id_estudiante TEXT, nombre TEXT)''')
#except Exception as e:
 # print(e)
  #pass
#id_estudiantes = ("1000"+str(randint(1000,3000)))
#nombre = input("nombre: ")
#cursor.execute('''INSERT INTO estudiantes (id_estudiante, nombre) VALUES (?,?)''',(id_estudiantes, nombre))
#db.commit()

#db.close()
