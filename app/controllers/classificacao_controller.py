from app import db
from app.models.classificacao import Classificacao

class ClassificacaoController:
    def listar_classificacoes():
        times = Time.query.all()
        classicacao = []
        for time in times:
            pontos = ClassificacaoController.calcular_pontos(time)
            vitorias, empates, derrotas = ClassificacaoController.jogos_vencidos, time.jogos_empates, time.jogos_perdidos
        classificacoes = Classificacao.query.order_by(Classificacao.pontos.desc(), Classificacao.saldo_gols.desc()).all()
        return classificacoes
    
    def calcular_pontos(time):
        vitorias = time.jogos_vencidos * 3
        empates = time.jogos_empates * 1
        pontos = vitorias + empates
        return pontos