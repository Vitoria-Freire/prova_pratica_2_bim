from app import db
from app.models.classificacao import Classificacao

class ClassificacaoController:
    def listar_classificacoes():
        classificacoes = Classificacao.query.order_by(Classificacao.pontos.desc(), Classificacao.saldo_gols.desc()).all()
        return classificacoes