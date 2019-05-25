from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

'''
Большинство расширений Flask используют соглашение об именах flask_ для импорта
верхнего уровня. В этом случае Flask-WTF меняет все свои символы под flask_wtf.
Здесь базовый класс FlaskForm импортируется из верхней части app/forms.py.
Четыре класса, которые представляют типы полей, которые я использую для этой формы,
импортируются непосредственно из пакета WTForms, поскольку расширение Flask-WTF
не предоставляет настраиваемые версии. Для каждого поля объект создается как
переменная класса в классе LoginForm. Каждому полю присваивается описание или
метка в качестве первого аргумента.


Дополнительный аргумент validators, который вы видите в некоторых полях,
используется для привязки поведения проверки к полям. Валидатор DataRequired
просто проверяет, что поле не отправлено пустым. Существует еще много доступных
валидаторов, некоторые из которых будут использоваться в других формах.
'''
