from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    username = StringField("username", [validators.Length(min=5)])
    password = PasswordField("password", [
        validators.Length(min=8),
        validators.EqualTo("password_repeat")
    ])
    password_repeat = PasswordField("repeat password: ")


class LoginForm(Form):
    username = StringField("username", [validators.Length(min=5)])
    password = PasswordField("password", [
        validators.Length(min=8)
    ])
