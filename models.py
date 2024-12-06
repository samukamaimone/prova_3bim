from database import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key = True)
    nome_cliente = db.Column(db.String(100))
    telefone = db.Column(db.String(15))

    def __init__(self, nome_cliente, telefone):
        self.nome_cliente = nome_cliente
        self.telefone = telefone

    def __repr__(self):
        return "<Cliente {self.nome_cliente}>".f
    

class Reclamacao(db.Model):
    __tablename__ = 'reclamacao'
    id = db.Column(db.Integer, primary_key = True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    descricao = db.Column(db.String(255))
    data = db.Column(db.Date)

    cliente = db.relationship('Cliente', foreign_keys=id_cliente)

    def __init__(self, id_cliente, descricao, data):
        self.id_cliente = id_cliente
        self.descricao = descricao
        self.data = data

    def __repr__(self):
        return "<Reclamação {self.cliente.nome_cliente} - {self.reclamacao.descricao} - {self.reclamacao.data}>".f