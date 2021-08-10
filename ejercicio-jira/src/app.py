#Importando el módulo de flask
from os import name
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

#Instanciando el objeto.
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ejercicio-jira'
mysql = MySQL(app)

#Dependencia: "Mostrar registros".
"""
    @userData es la estructura de datos utilizada para manipular los registros.
    Contiene en su interior 3 claves (name, phone, remainder) y el valor de cada clave es una lista.
"""
userData = {
    "name": [],
    "phone": [],
    "remainder": []
}

#Ruta de muestra de usuarios.
""" 
    @show() función que realiza el proceso de muestra.
    @returns un renderizado del html con los datos que existen en el diccionario @userData
"""
@app.route('/', methods=['GET'])
def index():
    with mysql.connection.cursor() as cur:
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
    return render_template('layout/index.html', data=data)

#Ruta donde se agregan los datos a la estructura de datos.
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        remainder = request.form['remainder']
        with mysql.connection.cursor() as cur:
            try:
                cur.execute("INSERT INTO users(name, phone, remainder) VALUES(%s, %s, %s)", (name, phone, remainder))
                mysql.connection.commit()
            except:
                error = "Ocurrió un error mientras se insertaban los datos."
        return redirect('/')
    return render_template('layout/add.html')

#Ruta para actualizar los datos en la estructura de datos
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    with mysql.connection.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE id = %s", (id, ))
        user = cur.fetchone()
        if request.method == 'POST':
            newName = request.form['name']
            newPhone = request.form['phone']
            newRemainder = request.form['remainder']
            cur.execute("UPDATE users SET name = %s, phone = %s, remainder = %s WHERE id = %s", (newName, newPhone, newRemainder, id, ))
            mysql.connection.commit()
            return redirect('/')
        return render_template('layout/edit.html', user=user)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    with mysql.connection.cursor() as cur:
        cur.execute("DELETE FROM users WHERE id = %s", (id, ))
        mysql.connection.commit()
        return redirect('/')

#Ruta de busqueda.
""" 
    @search() función que se encarga de realizar la busqueda de un usuario.
    @returns un renderizado de HTML si la petición es GET.
    @returns un mensaje si el usuario no se encuentra.
    @returns un renderizado de HTML con los datos del usuario en caso de ser encontrado.
"""
@app.route('/search', methods=['POST'])
def search():
    search = request.form['search']
    with mysql.connection.cursor() as cur:
        cur.execute(f"SELECT * FROM users WHERE name LIKE '%{search}%'")
        result = cur.fetchall()
        if(result):
            return render_template('layout/index.html', data=result)
        return render_template('layout/index.html')