from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL
import csv
import re

# config
csv_file = 'cafe-data.csv'
ratings_scale = [i for i in range(0, 11)]

app = Flask(__name__)
app.config['SECRET_KEY'] = '64bit'
Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()], render_kw={'placeholder': 'The Café down the road'})
    location = StringField('Location URL', validators=[DataRequired(), URL()], render_kw={'placeholder': 'https://goo.gl/maps/2EvhB4oq4gyUXKXx9'})
    open = TimeField('Opens at', validators=[DataRequired()])
    close = TimeField('Closes at', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', validators=[DataRequired()], choices=ratings_scale)
    wifi = SelectField('Wi-Fi rating', validators=[DataRequired()], choices=ratings_scale)
    power = SelectField('Power outlet rating', validators=[DataRequired()], choices=ratings_scale)
    submit = SubmitField('Submit')

@app.template_filter('regex_match')
def regex_match(string, pattern):
    return re.match(pattern, string) is not None

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(csv_file, newline='', mode='at') as file:
            entry = [value for key, value in form.data.items()][:-2]
            print(entry)
            csv.writer(file).writerow(entry)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(csv_file, newline='') as file:
        data = csv.reader(file)
        list_of_rows = [row for row in data]
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
