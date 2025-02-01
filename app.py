from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

# Clave secreta Flask para habilitar el uso de sesiones
app.secret_key = "your_secret_key"

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = config.Config.MYSQL_HOST
app.config['MYSQL_USER'] = config.Config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.Config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.Config.MYSQL_DB
app.config['MYSQL_PORT'] = config.Config.MYSQL_PORT

# Inicializar la base de datos
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form.get('name')
            correo = request.form.get('email')
            telefono = request.form.get('phone')
            asunto = request.form.get('subject')
            mensaje = request.form.get('message')
            
            # Insertar los datos en la base de datos
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO datos (nombre, correo, telefono, asunto, mensaje) VALUES (%s, %s, %s, %s, %s)", (nombre, correo, telefono, asunto, mensaje))
            mysql.connection.commit()
            cur.close()
            
            flash('Datos enviados correctamente', 'success')
        except Exception as e:
            flash(f'Error al enviar los datos: {str(e)}', 'danger')
                
        # Redirigir al formulario
        return redirect(url_for('formulario'))

    response = make_response(render_template('index.html'))
    response.headers['X-Server-Name'] = 'application1_pf'  # Cambia esto según el servidor
    return response

@app.route('/home')
def home():
    response = make_response(render_template('html.html'))
    response.headers['X-Server-Name'] = 'application1_pf'  # Cambia esto según el servidor
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)