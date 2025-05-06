import flask as fl
from flask_wtf import FlaskForm
import wtforms as wtf
from flask_bootstrap import Bootstrap5

app = fl.Flask(__name__)
app.secret_key = "twopancakes"
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    email = wtf.StringField('email', validators=[wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField('password', validators=[wtf.validators.DataRequired(), wtf.validators.Length(max=256)])
    submit = wtf.SubmitField('Log in')


@app.route('/')
def home():
    return fl.render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    lf = LoginForm()
    # if lf.validate_on_submit():
    if fl.request.method == 'POST':
        print(f'work\nemail: {lf.email.data}\npass: {lf.password.data}')
        if lf.email.data == 'admin@example.com' and lf.password.data == 'admin':
            return fl.render_template('success.html')
        else:
            return fl.render_template('denied.html')
    return fl.render_template('login.html', form=lf)


if __name__ == '__main__':
    app.run(debug=True)
