import sqlite3 
import json

#Conexion sqlite 

conexion = sqlite3.connect('desafioTareaUc.sqlite')
cursor = conexion.cursor()

#Verifica si la tabla de base de datos existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Project_UC (
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,   
        Gender TEXT,
        PlanDeSalud TEXT,
        Phone INTEGER
    )
''')

