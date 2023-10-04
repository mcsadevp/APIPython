# pip install Flask Flask-SQLAlchemy

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Función para buscar registros por correo electrónico
def buscar_por_email(email):
    conexion = sqlite3.connect('desafioTareaUc.sqlite')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM Project_UC WHERE Email = ?', (email,))
    resultado = cursor.fetchall()

    conexion.close()
    return resultado

# Ruta de la API para buscar por correo electrónico
@app.route('/buscar_por_email', methods=['GET'])
def buscar_por_email_api():
    email = request.args.get('email')
    if email:
        resultados = buscar_por_email(email)
        if resultados:
            return jsonify(resultados)
        else:
            return jsonify({'mensaje': 'No se encontraron registros para el correo electrónico proporcionado.'}), 404
    else:
        return jsonify({'mensaje': 'Por favor, proporcione un correo electrónico válido en el parámetro "email".'}), 400

if __name__ == '__main__':
    app.run(debug=True)











