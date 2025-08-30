from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basedatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreproducto = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nombre}>"

@app.route('/')
def index():
    return render_template('index.html', name="Estudiante UDI")

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/agregar', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        nuevo = Usuario(nombre=nombre, edad=int(edad))
        db.session.add(nuevo)
        db.session.commit()
        
        return redirect(url_for('bienvenida', nombre=nombre, edad=edad))
    return render_template('form.html')

@app.route('/bienvenida')
def bienvenida():
    nombre = request.args.get('nombre')
    edad = request.args.get('edad')
    return render_template('bienvenida.html', nombre=nombre, edad=edad)

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.edad = request.form['edad']
        db.session.commit()
        return redirect(url_for('listar_usuarios'))
    
    return render_template('editar.html', usuario=usuario)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('listar_usuarios'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)