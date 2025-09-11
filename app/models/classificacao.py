import sqlalchemy.orm as so
from app import db
from datetime import datetime

class Classificacao(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # posicao: so.Mapped[int] = so.mapped_column(nullable=False)
    pontos: so.Mapped[int] = so.mapped_column(nullable=False)
    jogos_disputados: so.Mapped[int] = so.mapped_column(nullable=False)
    vitorias: so.Mapped[int] = so.mapped_column(nullable=False)
    empates: so.Mapped[int] = so.mapped_column(nullable=False)
    derrotas: so.Mapped[int] = so.mapped_column(nullable=False)
    gols_pro: so.Mapped[int] = so.mapped_column(nullable=False)
    gols_contra: so.Mapped[int] = so.mapped_column(nullable=False)
    saldo_gols: so.Mapped[int] = so.mapped_column(nullable=False)
    updated_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)