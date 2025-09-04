from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestion_ventas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)

# Modelo Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    direccion = db.Column(db.Text, nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con ventas
    ventas = db.relationship('Venta', backref='cliente', lazy=True)

    def __repr__(self):
        return f"<Cliente {self.nombre} {self.apellido}>"

# Modelo Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    categoria = db.Column(db.String(50), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con detalles de venta
    detalles_venta = db.relationship('DetalleVenta', backref='producto', lazy=True)

    def __repr__(self):
        return f"<Producto {self.nombre}>"

# Modelo Venta
class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    fecha_venta = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False, default=0.0)
    estado = db.Column(db.String(20), default='Pendiente')  # Pendiente, Completada, Cancelada
    
    # Relación con detalles de venta
    detalles = db.relationship('DetalleVenta', backref='venta', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Venta {self.id} - Cliente: {self.cliente.nombre}>"

# Modelo DetalleVenta
class DetalleVenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<DetalleVenta {self.id} - Producto: {self.producto.nombre}>"

# ===== RUTA PRINCIPAL - DASHBOARD =====
@app.route('/')
def dashboard():
    # Estadísticas básicas para el dashboard
    total_clientes = Cliente.query.count()
    total_productos = Producto.query.count()
    total_ventas = Venta.query.count()
    ventas_pendientes = Venta.query.filter_by(estado='Pendiente').count()
    
    # Ventas recientes (últimas 5)
    ventas_recientes = Venta.query.order_by(Venta.fecha_venta.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                         total_clientes=total_clientes,
                         total_productos=total_productos,
                         total_ventas=total_ventas,
                         ventas_pendientes=ventas_pendientes,
                         ventas_recientes=ventas_recientes)

# ===== RUTAS CRUD PARA CLIENTES =====
@app.route('/clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/lista.html', clientes=clientes)

@app.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        try:
            cliente = Cliente(
                nombre=request.form['nombre'],
                apellido=request.form['apellido'],
                email=request.form['email'],
                telefono=request.form.get('telefono', ''),
                direccion=request.form.get('direccion', '')
            )
            db.session.add(cliente)
            db.session.commit()
            flash('Cliente agregado exitosamente', 'success')
            return redirect(url_for('listar_clientes'))
        except Exception as e:
            flash(f'Error al agregar cliente: {str(e)}', 'error')
    
    return render_template('clientes/nuevo.html')

@app.route('/clientes/<int:id>')
def ver_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('clientes/detalle.html', cliente=cliente)

@app.route('/clientes/<int:id>/editar', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        try:
            cliente.nombre = request.form['nombre']
            cliente.apellido = request.form['apellido']
            cliente.email = request.form['email']
            cliente.telefono = request.form.get('telefono', '')
            cliente.direccion = request.form.get('direccion', '')
            db.session.commit()
            flash('Cliente actualizado exitosamente', 'success')
            return redirect(url_for('listar_clientes'))
        except Exception as e:
            flash(f'Error al actualizar cliente: {str(e)}', 'error')
    
    return render_template('clientes/editar.html', cliente=cliente)

@app.route('/clientes/<int:id>/eliminar', methods=['POST'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    try:
        db.session.delete(cliente)
        db.session.commit()
        flash('Cliente eliminado exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar cliente: {str(e)}', 'error')
    return redirect(url_for('listar_clientes'))

# ===== RUTAS CRUD PARA PRODUCTOS =====
@app.route('/productos')
def listar_productos():
    productos = Producto.query.all()
    return render_template('productos/lista.html', productos=productos)

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        try:
            producto = Producto(
                nombre=request.form['nombre'],
                descripcion=request.form.get('descripcion', ''),
                precio=float(request.form['precio']),
                stock=int(request.form.get('stock', 0)),
                categoria=request.form.get('categoria', '')
            )
            db.session.add(producto)
            db.session.commit()
            flash('Producto agregado exitosamente', 'success')
            return redirect(url_for('listar_productos'))
        except Exception as e:
            flash(f'Error al agregar producto: {str(e)}', 'error')
    
    return render_template('productos/nuevo.html')

@app.route('/productos/<int:id>')
def ver_producto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('productos/detalle.html', producto=producto)

@app.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        try:
            producto.nombre = request.form['nombre']
            producto.descripcion = request.form.get('descripcion', '')
            producto.precio = float(request.form['precio'])
            producto.stock = int(request.form.get('stock', 0))
            producto.categoria = request.form.get('categoria', '')
            db.session.commit()
            flash('Producto actualizado exitosamente', 'success')
            return redirect(url_for('listar_productos'))
        except Exception as e:
            flash(f'Error al actualizar producto: {str(e)}', 'error')
    
    return render_template('productos/editar.html', producto=producto)

@app.route('/productos/<int:id>/eliminar', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    try:
        db.session.delete(producto)
        db.session.commit()
        flash('Producto eliminado exitosamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar producto: {str(e)}', 'error')
    return redirect(url_for('listar_productos'))

# ===== RUTAS PARA GESTIÓN DE VENTAS =====
@app.route('/ventas')
def listar_ventas():
    ventas = Venta.query.order_by(Venta.fecha_venta.desc()).all()
    return render_template('ventas/lista.html', ventas=ventas)

@app.route('/ventas/nueva', methods=['GET', 'POST'])
def nueva_venta():
    if request.method == 'POST':
        try:
            # Crear nueva venta
            venta = Venta(
                cliente_id=int(request.form['cliente_id']),
                estado='Pendiente'
            )
            db.session.add(venta)
            db.session.flush()  # Para obtener el ID de la venta
            
            # Procesar productos y cantidades
            productos_ids = request.form.getlist('producto_id')
            cantidades = request.form.getlist('cantidad')
            
            total_venta = 0
            
            for i, producto_id in enumerate(productos_ids):
                if producto_id and cantidades[i]:
                    producto = Producto.query.get(int(producto_id))
                    cantidad = int(cantidades[i])
                    
                    if producto and cantidad > 0:
                        # Verificar stock disponible
                        if producto.stock >= cantidad:
                            subtotal = producto.precio * cantidad
                            
                            # Crear detalle de venta
                            detalle = DetalleVenta(
                                venta_id=venta.id,
                                producto_id=producto.id,
                                cantidad=cantidad,
                                precio_unitario=producto.precio,
                                subtotal=subtotal
                            )
                            db.session.add(detalle)
                            
                            # Actualizar stock
                            producto.stock -= cantidad
                            total_venta += subtotal
                        else:
                            flash(f'Stock insuficiente para {producto.nombre}', 'error')
                            db.session.rollback()
                            return redirect(url_for('nueva_venta'))
            
            # Actualizar total de la venta
            venta.total = total_venta
            db.session.commit()
            
            flash('Venta creada exitosamente', 'success')
            return redirect(url_for('ver_venta', id=venta.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear venta: {str(e)}', 'error')
    
    # Obtener clientes y productos para el formulario
    clientes = Cliente.query.all()
    productos = Producto.query.filter(Producto.stock > 0).all()
    return render_template('ventas/nueva.html', clientes=clientes, productos=productos)

@app.route('/ventas/<int:id>')
def ver_venta(id):
    venta = Venta.query.get_or_404(id)
    return render_template('ventas/detalle.html', venta=venta)

@app.route('/ventas/<int:id>/estado', methods=['POST'])
def actualizar_estado_venta(id):
    venta = Venta.query.get_or_404(id)
    nuevo_estado = request.form['estado']
    
    try:
        # Si se cancela la venta, devolver stock
        if nuevo_estado == 'Cancelada' and venta.estado != 'Cancelada':
            for detalle in venta.detalles:
                detalle.producto.stock += detalle.cantidad
        
        # Si se reactiva una venta cancelada, verificar stock
        elif venta.estado == 'Cancelada' and nuevo_estado != 'Cancelada':
            for detalle in venta.detalles:
                if detalle.producto.stock < detalle.cantidad:
                    flash(f'Stock insuficiente para reactivar la venta', 'error')
                    return redirect(url_for('ver_venta', id=id))
                detalle.producto.stock -= detalle.cantidad
        
        venta.estado = nuevo_estado
        db.session.commit()
        flash(f'Estado de venta actualizado a {nuevo_estado}', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Error al actualizar estado: {str(e)}', 'error')
    
    return redirect(url_for('ver_venta', id=id))

# ===== RUTAS DE REPORTES BÁSICOS =====
@app.route('/reportes')
def reportes():
    # Ventas por estado
    ventas_por_estado = db.session.query(
        Venta.estado, 
        db.func.count(Venta.id).label('cantidad'),
        db.func.sum(Venta.total).label('total')
    ).group_by(Venta.estado).all()
    
    # Top productos más vendidos
    productos_mas_vendidos = db.session.query(
        Producto.nombre,
        db.func.sum(DetalleVenta.cantidad).label('cantidad_vendida'),
        db.func.sum(DetalleVenta.subtotal).label('ingresos')
    ).join(DetalleVenta).group_by(Producto.id).order_by(
        db.func.sum(DetalleVenta.cantidad).desc()
    ).limit(10).all()
    
    # Clientes con más compras
    mejores_clientes = db.session.query(
        Cliente.nombre,
        Cliente.apellido,
        db.func.count(Venta.id).label('total_compras'),
        db.func.sum(Venta.total).label('total_gastado')
    ).join(Venta).group_by(Cliente.id).order_by(
        db.func.sum(Venta.total).desc()
    ).limit(10).all()
    
    return render_template('reportes/dashboard.html',
                         ventas_por_estado=ventas_por_estado,
                         productos_mas_vendidos=productos_mas_vendidos,
                         mejores_clientes=mejores_clientes)

# ===== API ENDPOINTS PARA AJAX =====
@app.route('/api/productos/<int:id>')
def api_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify({
        'id': producto.id,
        'nombre': producto.nombre,
        'precio': producto.precio,
        'stock': producto.stock
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)