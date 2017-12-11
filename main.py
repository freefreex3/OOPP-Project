from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, PasswordField, validators
app = Flask(__name__)

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = PasswordField('Password')

@app.route('/', methods=['GET', 'POST'])
def log_in():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if(form.username.data == "admin" and form.password.data == "password"):
            return render_template('home.html', form=form)

    return render_template('test.html', form=form)

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/Repair/')
def Repair():
    return render_template('Repair.html')

@app.route('/Storage/')
def Storage():
    return render_template('Storage.html')

@app.route('/Profile/')
def Profile():
    return render_template('Profile.html')

if __name__ == "__main__":
    app.run(debug=True)

