from app import db
import sqlalchemy as sa
from typing import Optional
import sqlalchemy.orm as so

class Usuario(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped [Optional[str]] = so.mapped_column (sa.String(256))