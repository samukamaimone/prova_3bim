from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'StRiNgQNgMSaBe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/prova_flask3bim"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Cliente, Reclamacao
db.init_app(app)
migrate = Migrate(app, db)

from modulos.clientes.clientes import bp_cliente
app.register_blueprint(bp_cliente, url_prefix='/clientes')

from modulos.reclamacoes.reclamacoes import bp_reclamacao
app.register_blueprint(bp_reclamacao, url_prefix='/reclamacoes')

@app.route("/")
def index():
    return render_template('index.html')



