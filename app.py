from flask import session
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import get_db_connection
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.utils import secure_filename
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from mysql.connector import IntegrityError
from db import get_db_connection




app = Flask(__name__)
app.secret_key = '1234'
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'img', 'productos')
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        username = request.form.get('username')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO usuarios (nombre, apellido, username, email, telefono, password) VALUES (%s, %s, %s, %s, %s, %s)''',
                (nombre, apellido, username, email, telefono, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            return f"Error en el registro: {err}"
    return render_template('registro.html')

@app.route('/')
def index():
    # Datos del mapa de energías renovables del Caribe
    departamentos_caribe = [
        {
            'nombre': 'La Guajira',
            'capacidad_solar': 486.8,  # MW
            'capacidad_eolica': 498.9,  # MW
            'proyectos_activos': 12,
            'porcentaje_renovable': 78,
            'lat': 11.5444,
            'lng': -72.9072,
            'proyectos': [
                {'nombre': 'Parque Eólico Jepírachi', 'tipo': 'eolico', 'capacidad': 19.5},
                {'nombre': 'Granja Solar La Guajira', 'tipo': 'solar', 'capacidad': 86.2},
                {'nombre': 'Parque Eólico Windpeshi', 'tipo': 'eolico', 'capacidad': 205},
            ]
        },
        {
            'nombre': 'Cesar',
            'capacidad_solar': 245.6,
            'capacidad_eolica': 0,
            'proyectos_activos': 8,
            'porcentaje_renovable': 35,
            'lat': 10.4631,
            'lng': -73.2532,
            'proyectos': [
                {'nombre': 'Parque Solar El Paso', 'tipo': 'solar', 'capacidad': 86.2},
                {'nombre': 'Planta Solar Valledupar', 'tipo': 'solar', 'capacidad': 62.5},
                {'nombre': 'Granja Solar Cesar I', 'tipo': 'solar', 'capacidad': 96.9},
            ]
        },
        {
            'nombre': 'Magdalena',
            'capacidad_solar': 123.4,
            'capacidad_eolica': 0,
            'proyectos_activos': 5,
            'porcentaje_renovable': 22,
            'lat': 10.4139,
            'lng': -74.4059,
            'proyectos': [
                {'nombre': 'Parque Solar Santa Marta', 'tipo': 'solar', 'capacidad': 45.8},
                {'nombre': 'Planta Solar Ciénaga', 'tipo': 'solar', 'capacidad': 32.1},
                {'nombre': 'Granja Solar Aracataca', 'tipo': 'solar', 'capacidad': 45.5},
            ]
        },
        {
            'nombre': 'Atlántico',
            'capacidad_solar': 89.7,
            'capacidad_eolica': 147.5,
            'proyectos_activos': 6,
            'porcentaje_renovable': 28,
            'lat': 10.7964,
            'lng': -74.8810,
            'proyectos': [
                {'nombre': 'Parque Solar Barranquilla', 'tipo': 'solar', 'capacidad': 42.3},
                {'nombre': 'Parque Eólico Atlántico', 'tipo': 'eolico', 'capacidad': 147.5},
                {'nombre': 'Granja Solar Soledad', 'tipo': 'solar', 'capacidad': 47.4},
            ]
        },
        {
            'nombre': 'Bolívar',
            'capacidad_solar': 67.2,
            'capacidad_eolica': 0,
            'proyectos_activos': 4,
            'porcentaje_renovable': 18,
            'lat': 10.3910,
            'lng': -75.4794,
            'proyectos': [
                {'nombre': 'Parque Solar Cartagena', 'tipo': 'solar', 'capacidad': 35.1},
                {'nombre': 'Planta Solar Turbaco', 'tipo': 'solar', 'capacidad': 32.1},
            ]
        },
        {
            'nombre': 'Córdoba',
            'capacidad_solar': 45.8,
            'capacidad_eolica': 0,
            'proyectos_activos': 3,
            'porcentaje_renovable': 15,
            'lat': 8.7569,
            'lng': -75.8664,
            'proyectos': [
                {'nombre': 'Granja Solar Montería', 'tipo': 'solar', 'capacidad': 28.4},
                {'nombre': 'Parque Solar Cereté', 'tipo': 'solar', 'capacidad': 17.4},
            ]
        },
        {
            'nombre': 'Sucre',
            'capacidad_solar': 34.2,
            'capacidad_eolica': 0,
            'proyectos_activos': 2,
            'porcentaje_renovable': 12,
            'lat': 9.1469,
            'lng': -75.3947,
            'proyectos': [
                {'nombre': 'Parque Solar Sincelejo', 'tipo': 'solar', 'capacidad': 24.8},
                {'nombre': 'Granja Solar Corozal', 'tipo': 'solar', 'capacidad': 9.4},
            ]
        },
        {
            'nombre': 'San Andrés',
            'capacidad_solar': 12.5,
            'capacidad_eolica': 8.2,
            'proyectos_activos': 3,
            'porcentaje_renovable': 45,
            'lat': 12.5847,
            'lng': -81.7006,
            'proyectos': [
                {'nombre': 'Proyecto Solar Islas', 'tipo': 'solar', 'capacidad': 12.5},
                {'nombre': 'Turbina Eólica Marina', 'tipo': 'eolico', 'capacidad': 8.2},
            ]
        }
    ]
    
    return render_template('index.html', departamentos_caribe=departamentos_caribe)

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT * FROM usuarios WHERE username = %s OR email = %s', (username, username))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['rol'] = user.get('rol', 'usuario')
                return redirect(url_for('index'))
            else:
                error = 'Usuario o contraseña incorrectos.'
        except mysql.connector.Error as err:
            error = f"Error de conexión: {err}"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

@app.route('/productos_solares')
def productos_solares():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos WHERE seccion = 'solar' AND disponible = 'si'")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('productos_solares.html', productos=productos)

@app.route('/productos_eolicos')
def productos_eolicos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos WHERE seccion = 'eolico' AND disponible = 'si'")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('productos_eolicos.html', productos=productos)

@app.route('/ingenieria')
def ingenieria():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos WHERE seccion = 'ingenieria' AND disponible = 'si'")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('ingenieria.html', productos=productos)

# Decorador para requerir usuario admin
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('rol') or session.get('rol') != 'admin':
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
@admin_required
def admin():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # Total usuarios
    cursor.execute('SELECT COUNT(*) as total FROM usuarios')
    usuarios = cursor.fetchone()['total']
    # Total productos
    cursor.execute('SELECT SUM(cantidad) as total FROM productos')
    productos = cursor.fetchone()['total'] or 0
    # Total ventas
    cursor.execute('SELECT COUNT(*) as total FROM ventas')
    ventas = cursor.fetchone()['total']
    # Total mensajes
    cursor.execute('SELECT COUNT(*) as total FROM mensajes_contacto')
    mensajes = cursor.fetchone()['total']
    # Último acceso (última venta registrada)
    cursor.execute('SELECT MAX(fecha) as ultimo FROM ventas')
    ultimo_acceso = cursor.fetchone()['ultimo']
    # Admins registrados
    cursor.execute('SELECT COUNT(*) as total FROM usuarios WHERE rol = "admin"')
    admins = cursor.fetchone()['total']
    # Productos bajo stock
    cursor.execute('SELECT nombre, cantidad FROM productos WHERE cantidad <= 5')
    productos_bajo_stock_lista = cursor.fetchall()
    productos_bajo_stock = len(productos_bajo_stock_lista)
    cursor.close()
    conn.close()
    resumen = {
        'usuarios': usuarios,
        'productos': productos,
        'ventas': ventas,
        'mensajes': mensajes,
        'ultimo_acceso': ultimo_acceso,
        'admins': admins,
        'productos_bajo_stock': productos_bajo_stock,
        'productos_bajo_stock_lista': productos_bajo_stock_lista
    }
    return render_template('admin.html', resumen=resumen)

# Ruta de perfil de usuario (ambos roles)
@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    mensaje = error = None
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
    usuario = cursor.fetchone()
    # Obtener compras del usuario
    cursor.execute('SELECT * FROM ventas WHERE usuario_id = %s ORDER BY fecha DESC', (user_id,))
    compras = cursor.fetchall()
    compras_con_detalles = []
    for v in compras:
        cursor.execute('SELECT * FROM venta_detalles WHERE venta_id = %s', (v['id'],))
        detalles = cursor.fetchall()
        compras_con_detalles.append({'venta': v, 'detalles': detalles})
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        if not check_password_hash(usuario['password'], old_password):
            error = 'La contraseña actual es incorrecta.'
        else:
            hashed_new = generate_password_hash(new_password)
            cursor.execute('UPDATE usuarios SET password = %s WHERE id = %s', (hashed_new, user_id))
            conn.commit()
            mensaje = 'Contraseña actualizada correctamente.'
            # Refrescar datos
            cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
            usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('perfil.html', usuario=usuario, mensaje=mensaje, error=error, compras=compras_con_detalles)

# Ruta para la página de contacto
@app.route('/contactanos', methods=['GET', 'POST'])
def contactanos():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        texto = request.form.get('mensaje')
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO mensajes_contacto (nombre, email, mensaje) VALUES (%s, %s, %s)', (nombre, email, texto))
            conn.commit()
            cursor.close()
            conn.close()
            mensaje = '¡Mensaje enviado correctamente! Pronto nos pondremos en contacto.'
        except Exception as err:
            mensaje = f'Error al enviar el mensaje: {err}'
    return render_template('contactanos.html', mensaje=mensaje)

# --- RUTAS ADMIN ---
from flask import render_template

@app.route('/admin/usuarios')
@admin_required
def admin_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # Ordenar primero los admin, luego los usuarios normales
    cursor.execute('SELECT id, nombre, apellido, username, email, telefono, rol FROM usuarios ORDER BY (rol = "admin") DESC, id ASC')
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    # Identificar el admin original (id=1)
    admin_original_id = 1
    return render_template('admin_usuarios.html', usuarios=usuarios, active='usuarios', admin_original_id=admin_original_id)

# Cambiar rol a admin
@app.route('/admin/usuarios/<int:user_id>/hacer_admin', methods=['POST'])
@admin_required
def hacer_admin(user_id):
    if user_id == 1:
        return redirect(url_for('admin_usuarios'))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET rol = %s WHERE id = %s', ('admin', user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('admin_usuarios'))

# Quitar rol admin
@app.route('/admin/usuarios/<int:user_id>/quitar_admin', methods=['POST'])
@admin_required
def quitar_admin(user_id):
    if user_id == 1:
        return redirect(url_for('admin_usuarios'))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET rol = %s WHERE id = %s', ('usuario', user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('admin_usuarios'))

# Eliminar usuario
@app.route('/admin/usuarios/<int:user_id>/eliminar', methods=['POST'])
@admin_required
def eliminar_usuario(user_id):
    if user_id == 1:
        return redirect(url_for('admin_usuarios'))
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('admin_usuarios'))

# Editar usuario (GET muestra formulario, POST guarda cambios)
@app.route('/admin/usuarios/<int:user_id>/editar', methods=['GET', 'POST'])
@admin_required
def editar_usuario(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        username = request.form.get('username')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        try:
            cursor.execute('''UPDATE usuarios SET nombre=%s, apellido=%s, username=%s, email=%s, telefono=%s WHERE id=%s''',
                (nombre, apellido, username, email, telefono, user_id))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('admin_usuarios'))
        except IntegrityError as e:
            error = "El correo ya está registrado por otro usuario."
            conn.rollback()
    if request.method == 'GET' or error:
        cursor.execute('SELECT id, nombre, apellido, username, email, telefono, rol FROM usuarios WHERE id = %s', (user_id,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('editar_usuario.html', usuario=usuario, error=error)

@app.route('/admin/inventario')
@admin_required
def admin_inventario():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # Obtener productos por sección
    cursor.execute("SELECT * FROM productos WHERE seccion = 'solar'")
    productos_solar = cursor.fetchall()
    cursor.execute("SELECT * FROM productos WHERE seccion = 'eolico'")
    productos_eolico = cursor.fetchall()
    cursor.execute("SELECT * FROM productos WHERE seccion = 'ingenieria'")
    productos_ingenieria = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template(
        'admin_inventario.html',
        productos_solar=productos_solar,
        productos_eolico=productos_eolico,
        productos_ingenieria=productos_ingenieria,
        active='inventario'
    )

# Agregar producto
@app.route('/admin/inventario/agregar', methods=['GET', 'POST'])
@admin_required
def agregar_producto():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion') or None
        precio = request.form.get('precio')
        cantidad = request.form.get('cantidad')
        disponible = request.form.get('disponible') or 'si'
        seccion = request.form.get('seccion') or 'solar'
        foto = request.files.get('foto')
        foto_filename = None
        if foto and foto.filename:
            foto_filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_filename))
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO productos (nombre, descripcion, precio, cantidad, disponible, seccion, foto) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                (nombre, descripcion, precio, cantidad, disponible, seccion, foto_filename))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('admin_inventario'))
        except Exception as err:
            mensaje = f"Error al agregar producto: {err}"
    return render_template('agregar_producto.html', mensaje=mensaje, active='inventario')

# Editar producto
@app.route('/admin/inventario/<int:producto_id>/editar', methods=['GET', 'POST'])
@admin_required
def editar_producto(producto_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion') or None
        try:
            precio = float(request.form.get('precio'))
        except (TypeError, ValueError):
            precio = 0.0
        try:
            cantidad = int(request.form.get('cantidad'))
        except (TypeError, ValueError):
            cantidad = 0
        disponible = request.form.get('disponible') or 'si'
        seccion = request.form.get('seccion') or 'ingenieria'
        foto = request.files.get('foto')
        cursor.execute('SELECT foto FROM productos WHERE id = %s', (producto_id,))
        foto_row = cursor.fetchone()
        old_foto = foto_row['foto'] if foto_row and 'foto' in foto_row else None
        foto_filename = old_foto
        if foto and foto.filename:
            foto_filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_filename))
        cursor.execute(
            'UPDATE productos SET nombre=%s, descripcion=%s, precio=%s, cantidad=%s, disponible=%s, seccion=%s, foto=%s WHERE id=%s',
            (nombre, descripcion, precio, cantidad, disponible, seccion, foto_filename, producto_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('admin_inventario'))
    else:
        cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
    return render_template('editar_producto.html', producto=producto, active='inventario')

# Eliminar producto
@app.route('/admin/inventario/<int:producto_id>/eliminar', methods=['POST'])
@admin_required
def eliminar_producto(producto_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = %s', (producto_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('admin_inventario'))


@app.route('/admin/ventas')
@admin_required
def admin_ventas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ventas ORDER BY fecha DESC')
    ventas = cursor.fetchall()
    # Para cada venta, obtener detalles
    ventas_con_detalles = []
    for v in ventas:
        cursor.execute('SELECT * FROM venta_detalles WHERE venta_id = %s', (v['id'],))
        detalles = cursor.fetchall()
        ventas_con_detalles.append({'venta': v, 'detalles': detalles})
    cursor.close()
    conn.close()
    return render_template('admin_ventas.html', ventas=ventas_con_detalles, active='ventas')


@app.route('/admin/mensajes')
@admin_required
def admin_mensajes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM mensajes_contacto ORDER BY fecha DESC')
    mensajes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('admin_mensajes.html', mensajes=mensajes, active='mensajes')

# --- Carrito de compras ---

@app.route('/carrito')
def carrito():
    carrito = obtener_carrito()
    compra_bloqueada = False
    # Cargar stock actual por producto y marcar bloqueo si alguna cantidad excede
    if carrito:
        ids = tuple({item['id'] for item in carrito})
        placeholders = ','.join(['%s'] * len(ids))
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT id, cantidad FROM productos WHERE id IN ({placeholders})", ids)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        stock_map = {r['id']: int(r['cantidad'] or 0) for r in rows}
        for it in carrito:
            it['stock'] = stock_map.get(it['id'], 0)
            if it['cantidad'] > it['stock']:
                compra_bloqueada = True
    total = sum(item['precio'] * item['cantidad'] for item in carrito) if carrito else 0
    return render_template('carrito.html', carrito=carrito, total=total, active='carrito', compra_bloqueada=compra_bloqueada)

# --- Carrito de compras ---
def obtener_carrito():
    return session.get('carrito', [])

def guardar_carrito(carrito):
    session['carrito'] = carrito

# Añadir producto al carrito
@app.route('/agregar_al_carrito/<int:producto_id>', methods=['POST'])
def agregar_al_carrito(producto_id):
    cantidad = int(request.form.get('cantidad', 1))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    if not producto:
        flash('Producto no encontrado', 'danger')
        return redirect(request.referrer or url_for('tienda'))
    disponible = int(producto.get('cantidad', 0) or 0)
    if producto.get('disponible') == 'no' or disponible <= 0:
        flash('Producto sin stock. No se puede agregar al carrito.', 'warning')
        return redirect(request.referrer or url_for('tienda'))
    carrito = obtener_carrito()
    for item in carrito:
        if item['id'] == producto_id:
            nueva = item['cantidad'] + cantidad
            if nueva > disponible:
                nueva = disponible
                flash('Se ajustó la cantidad al máximo disponible en stock.', 'info')
            item['cantidad'] = max(1, nueva)
            break
    else:
        carrito.append({
            'id': producto['id'],
            'nombre': producto['nombre'],
            'precio': float(producto['precio']),
            'cantidad': min(cantidad, disponible)
        })
    guardar_carrito(carrito)
    flash('Producto agregado al carrito', 'success')
    from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

    ref = request.referrer or url_for('tienda')
    parsed = urlparse(ref)
    query = parse_qs(parsed.query)
    query['cart'] = 'added'
    new_query = urlencode(query, doseq=True)
    new_url = urlunparse(parsed._replace(query=new_query))
    return redirect(new_url)

# Actualizar cantidad en carrito
@app.route('/actualizar_carrito', methods=['POST'])
def actualizar_carrito():
    cantidades = request.form.getlist('cantidad')
    ids = request.form.getlist('producto_id')
    carrito = obtener_carrito()
    # Pre-cargar stock para los productos a actualizar
    stock_map = {}
    try:
        ids_unique = tuple({int(x) for x in ids}) if ids else tuple()
        if ids_unique:
            placeholders = ','.join(['%s'] * len(ids_unique))
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT id, cantidad FROM productos WHERE id IN ({placeholders})", ids_unique)
            for r in cursor.fetchall():
                stock_map[r['id']] = int(r['cantidad'] or 0)
            cursor.close()
            conn.close()
    except Exception:
        stock_map = {}
    nuevos = []
    for it in carrito:
        sid = str(it['id'])
        if sid in ids:
            idx = ids.index(sid)
            try:
                solicitada = int(cantidades[idx])
            except Exception:
                solicitada = it['cantidad']
            disponible = stock_map.get(it['id'], 0)
            if disponible <= 0:
                # quitar del carrito si no hay stock
                continue
            nueva = max(1, min(solicitada, disponible))
            if nueva != solicitada:
                flash(f"La cantidad de '{it['nombre']}' fue ajustada a {nueva} por límite de stock.", 'info')
            it['cantidad'] = nueva
        nuevos.append(it)
    carrito = nuevos
    guardar_carrito(carrito)
    return redirect(url_for('carrito'))

# Eliminar producto individual del carrito
@app.route('/eliminar_del_carrito/<int:producto_id>', methods=['POST'])
def eliminar_del_carrito(producto_id):
    carrito = obtener_carrito()
    carrito = [item for item in carrito if item['id'] != producto_id]
    guardar_carrito(carrito)
    flash('Producto eliminado del carrito.', 'info')
    return redirect(url_for('carrito'))


# --- Finalizar compra ---
@app.route('/finalizar_compra')
def finalizar_compra():
    usuario = None
    if session.get('user_id'):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT nombre, email, telefono FROM usuarios WHERE id = %s', (session['user_id'],))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        if not usuario:
            # Intentar buscar por username si no se encuentra por id
            username = session.get('username')
            if username:
                conn = get_db_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute('SELECT nombre, email, telefono FROM usuarios WHERE username = %s', (username,))
                usuario = cursor.fetchone()
                cursor.close()
                conn.close()
    return render_template('finalizar_compra.html', active='carrito', usuario=usuario)


# Procesar compra real
@app.route('/procesar_compra', methods=['POST'])
def procesar_compra():
    if not session.get('user_id'):
        flash('Debes iniciar sesión para comprar.', 'warning')
        return redirect(url_for('login'))
    carrito = obtener_carrito()
    if not carrito:
        flash('El carrito está vacío.', 'warning')
        return redirect(url_for('carrito'))
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    direccion_envio = request.form.get('direccion_envio')
    metodo_pago = request.form.get('metodo_pago')
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    usuario_id = session['user_id']

    # Verificación de stock vigente antes de comprar
    ids = tuple({it['id'] for it in carrito})
    placeholders = ','.join(['%s'] * len(ids)) if ids else ''
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if not ids:
        flash('El carrito está vacío.', 'warning')
        cursor.close()
        conn.close()
        return redirect(url_for('carrito'))
    cursor.execute(f"SELECT id, nombre, cantidad FROM productos WHERE id IN ({placeholders})", ids)
    rows = cursor.fetchall()
    stock_map = {r['id']: int(r['cantidad'] or 0) for r in rows}
    insuf = []
    for it in carrito:
        disp = stock_map.get(it['id'], 0)
        if it['cantidad'] > disp:
            insuf.append({'nombre': it['nombre'], 'sol': it['cantidad'], 'disp': disp})
    if insuf:
        # Ajustar carrito y bloquear compra
        nuevos = []
        for it in carrito:
            disp = stock_map.get(it['id'], 0)
            if disp <= 0:
                continue
            it['cantidad'] = min(it['cantidad'], disp)
            nuevos.append(it)
        guardar_carrito(nuevos)
        msg = '; '.join([f"{x['nombre']}: solicitada {x['sol']}, disponible {x['disp']}" for x in insuf])
        flash(f'No hay stock suficiente para completar la compra. Ajusta el carrito. Detalles: {msg}', 'danger')
        cursor.close()
        conn.close()
        return redirect(url_for('carrito'))

    # Transacción: actualizar dirección, descontar stock atómicamente, crear venta y detalles
    cursor.close()
    conn.close()
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Actualizar dirección en usuario
        cursor.execute('UPDATE usuarios SET direccion=%s WHERE id=%s', (direccion_envio, usuario_id))
        # Descontar inventario with verification (evita negativos)
        for it in carrito:
            cursor.execute('UPDATE productos SET cantidad = cantidad - %s WHERE id = %s AND cantidad >= %s', (it['cantidad'], it['id'], it['cantidad']))
            if cursor.rowcount == 0:
                raise Exception('Stock insuficiente durante el procesamiento de la compra')
        # Insertar venta
        cursor.execute(
            'INSERT INTO ventas (usuario_id, nombre_cliente, email_cliente, telefono_cliente, direccion_envio, metodo_pago, total) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (usuario_id, nombre, email, telefono, direccion_envio, metodo_pago, total)
        )
        venta_id = cursor.lastrowid
        # Insertar detalles de la venta
        for it in carrito:
            cursor.execute(
                'INSERT INTO venta_detalles (venta_id, producto_id, nombre_producto, cantidad, precio_unitario, subtotal) VALUES (%s, %s, %s, %s, %s, %s)',
                (venta_id, it['id'], it['nombre'], it['cantidad'], it['precio'], it['precio']*it['cantidad'])
            )
        # Marcar como no disponible los que quedaron en 0
        ids_compra = tuple({it['id'] for it in carrito})
        if ids_compra:
            placeholders = ','.join(['%s'] * len(ids_compra))
            cursor.execute(f"UPDATE productos SET disponible='no' WHERE id IN ({placeholders}) AND cantidad <= 0", ids_compra)
        conn.commit()
        # Obtener venta y detalles para mostrar en el recibo
        # Cerrar el cursor y reabrirlo como dictionary para ambos
        cursor.close()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM ventas WHERE id = %s', (venta_id,))
        venta = cursor.fetchone()
        cursor.execute('SELECT * FROM venta_detalles WHERE venta_id = %s', (venta_id,))
        detalles = cursor.fetchall()
    except Exception as e:
        print('ERROR en procesar_compra:', e)
        conn.rollback()
        flash(f'No se pudo completar la compra: {e}', 'danger')
        cursor.close()
        conn.close()
        return redirect(url_for('carrito'))
    cursor.close()
    conn.close()
    session['carrito'] = []
    return render_template('recibo.html', venta=venta, detalles=detalles)  # O la página que corresponda

@app.route('/perfil/compras')
def compras_perfil():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM ventas WHERE usuario_id = %s ORDER BY fecha DESC', (user_id,))
    compras = cursor.fetchall()
    compras_con_detalles = []
    for v in compras:
        cursor.execute('SELECT * FROM venta_detalles WHERE venta_id = %s', (v['id'],))
        detalles = cursor.fetchall()
        compras_con_detalles.append({'venta': v, 'detalles': detalles})
    cursor.close()
    conn.close()
    return render_template('compras_perfil.html', compras=compras_con_detalles)

@app.route('/perfil/seguridad', methods=['GET', 'POST'])
def seguridad_perfil():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    mensaje = error = None
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
    usuario = cursor.fetchone()
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        if not check_password_hash(usuario['password'], old_password):
            error = 'La contraseña actual es incorrecta.'
        else:
            hashed_new = generate_password_hash(new_password)
            cursor.execute('UPDATE usuarios SET password = %s WHERE id = %s', (hashed_new, user_id))
            conn.commit()
            mensaje = 'Contraseña actualizada correctamente.'
            # Refrescar datos
            cursor.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
            usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('seguridad_perfil.html', usuario=usuario, mensaje=mensaje, error=error)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))  # toma el puerto de Render o usa 5050 por defecto
    app.run(host='0.0.0.0', port=port, debug=True)











    
# ---
# Credenciales de admin para pruebas:
# Usuario: admin
# Email: admin@solaris.com
# Contraseña: (admin1234)
