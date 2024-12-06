from flask import Blueprint, render_template, request, redirect, flash
from models import Reclamacao, Cliente
from database import db
from datetime import datetime

bp_reclamacao = Blueprint('reclamacoes', __name__, template_folder="templates")

@bp_reclamacao.route('/')
def index():
    dados = Reclamacao.query.all()
    return render_template('reclamacao.html', reclamacoes = dados)

@bp_reclamacao.route('/add')
def add():
    c = Cliente.query.all()
    return render_template('reclamacao_add.html', clientes = c)

@bp_reclamacao.route('/remove/<int:id>')
def remove(id):
    if id > 0:
        r = Reclamacao.query.get(id)
        db.session.delete(r)
        db.session.commit()
        flash('Reclamação retirada com sucesso!')
        return redirect('/reclamacoes')
    else:
        flash('Caminho Incorreto!')
        return redirect('/reclamacoes')

@bp_reclamacao.route('/save', methods=['POST'])
def save():
    id_cliente = request.form.get('id_cliente')
    descricao = request.form.get('descricao')
    data = datetime.strptime(request.form['data'], "%Y-%m-%d").strftime("%d,%m,%Y")
    if id_cliente and descricao and data:
        bd_reclamacao = Reclamacao(id_cliente, descricao, data)
        db.session.add(bd_reclamacao)
        db.session.commit()
        flash('Reclamação realizada com sucesso!')
        return redirect('/reclamacoes')
    else:
        flash('Preencha todos os campos!')
        return redirect('/reclamacoes/add')
