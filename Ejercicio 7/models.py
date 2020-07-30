from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuario(db.Model):
    dni = db.Column(db.String(8), primary_key=True)
    clave = db.Column(db.String(32), nullable=False)
    tipo = db.Column(db.String(8), nullable=False)
    pedidos = db.relationship("Pedido", backref="usuario", cascade="all, delete-orphan", lazy="dynamic")

class Producto(db.Model):
    num_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    items = db.relationship("Item", backref="producto", cascade="all, delete-orphan", lazy="dynamic")
    
class Pedido(db.Model):
    num_pedido = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    total = db.Column(db.Float)
    cobrado = db.Column(db.Boolean)
    observacion = db.Column(db.String(60))
    dni_mozo = db.Column(db.String(8), db.ForeignKey("usuario.dni"))
    mesa = db.Column(db.Integer)
    items = db.relationship("Item", backref="pedido", cascade="all, delete-orphan", lazy="dynamic")
    
class Item(db.Model):
    num_item = db.Column(db.Integer, primary_key=True)
    num_pedido = db.Column(db.Integer, db.ForeignKey("pedido.num_pedido"))
    num_producto = db.Column(db.Integer, db.ForeignKey("producto.num_producto"))
    precio = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(9), nullable=False)
    