from flask import Blueprint, render_template, request, redirect, flash
from models import Cliente
from database import db

bp_cliente = Blueprint('clientes', __name__, template_folder="templates")

@bp_cliente.route('/')
def index():
    dados = Cliente.query.all()
    return render_template('cliente.html', clientes = dados)

@bp_cliente.route('/add')
def add():
    return render_template('cliente_add.html')

@bp_cliente.route('/save', methods=['POST'])
def save():
    nome_cliente = request.form.get('nome_cliente')
    telefone = request.form.get('telefone')
    if nome_cliente and telefone:
        bd_cliente = Cliente(nome_cliente, telefone)
        db.session.add(bd_cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!')
        return redirect('/clientes')
    else:
        flash('Preencha todos os campos!')
        return redirect('/clientes/add')
