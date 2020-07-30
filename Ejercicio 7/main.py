import hashlib, datetime
from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = "b'\x18\xf8@-P\x90\x1b=4t\xb7%\\\xe8w\x17'"

from models import db, Usuario, Producto, Item, Pedido

@app.route('/', methods = ['GET'])
def main():
    return render_template('inicio.html', error=request.args.get('error'))

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        usuario_actual = Usuario.query.filter_by(dni=request.form['dni']).first()
        clave_ingresada = hashlib.md5(bytes(request.form['contraseña'], encoding="utf-8")).hexdigest()

        if usuario_actual is None or usuario_actual.clave != clave_ingresada:
            return redirect(url_for('main', error=True))        
        else:
            session['dni'] = request.form['dni']
            tipo = usuario_actual.tipo.lower()
            return render_template(tipo + '.html') #Retorna mozo.html o cocinero.html
    else:
        if 'dni' in session:
            usuario_actual = Usuario.query.filter_by(dni=session['dni']).first()
            tipo = usuario_actual.tipo.lower()
            return render_template(tipo + '.html') 
                
@app.route('/nuevo_pedido', methods = ['POST', 'GET'])
def nuevo_pedido():
    if request.method == 'POST':
        session['items'] += [request.form['nombre']]
        return render_template('nuevo_pedido.html', productos=Producto.query.all(), num_mesa=request.form['mesa'], observacion=request.form['observacion'], items=session['items'])
    else:
        session['items'] = []
        return render_template('nuevo_pedido.html', productos=Producto.query.all(), num_mesa="1")

@app.route('/envio_pedido', methods = ['POST', 'GET'])
def envio_pedido():
    if request.method == 'POST':
        pedido_actual = Pedido(fecha=datetime.datetime.now(), cobrado=False, observacion=request.form['observacion'], dni_mozo=session['dni'], mesa=request.form['mesa'])
        db.session.add(pedido_actual)
        db.session.commit()
        
        t = 0
        for i in session['items']:
            prod = Producto.query.filter_by(nombre=i).first()
            item_ = Item(num_pedido=pedido_actual.num_pedido, num_producto=prod.num_producto, precio=prod.precio_unitario, estado="Pendiente")
            db.session.add(item_)
            t += item_.precio
        pedido_actual.total = t
        db.session.commit()
        return render_template('envio_pedido.html')

@app.route('/listar_pedidos')
def listar_pedidos():
    pedidos = Pedido.query.filter_by(cobrado=False)
    return render_template('listar_pedidos.html', pedidos=pedidos)

@app.route('/preparacion_items', methods = ['POST', 'GET'])
def preparacion_items():
    if request.method == 'POST':
        if request.form['item']:
            item_ = Item.query.filter_by(num_item=request.form['item']).first()
            item_.estado = "Listo"
            db.session.commit()
    pedidos = Pedido.query.all()
    pedidos_actuales = []
    for p in pedidos:
        estados = [i.estado for i in p.items]
        if "Pendiente" in estados:
            pedidos_actuales.append(p)
    return render_template('preparacion_items.html', pedidos=pedidos_actuales)
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)