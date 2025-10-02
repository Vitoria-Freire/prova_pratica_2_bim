from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo
from app.controllers.usuarioController import UsuarioController

class UsuarioForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Por favor, preencha o seu nome de usuário.")])
    email = EmailField('Email', validators=[DataRequired(message="Por favor, preencha o email."), Email(message='Email inválido.')])
    password = PasswordField('Senha', validators=[DataRequired(message="Por favor, preencha a senha."), Length(min=6)])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Salvar')

    def validate_username(self, username):
        if not UsuarioController.checar_unicidade(username.data.strip(), 'username'):
            raise ValidationError('Nome de usuário já cadastrado.')
        
    def validate_email(self, email):
        if not UsuarioController.checar_unicidade(email.data.strip().lower(), 'email'):
            raise ValidationError('Email já cadastrado.')