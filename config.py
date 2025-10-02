import secrets


class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gerenciamento_futebol.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:labinfo@localhost:3306/futebol'