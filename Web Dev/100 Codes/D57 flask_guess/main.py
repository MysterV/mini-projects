import flask as fl
import requests

app = fl.Flask(__name__)


@app.route('/')
def root():
    return fl.render_template('index.html')


@app.route('/guess/<string:name>')
def guess(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    return fl.render_template('guess.html', name=name.title(), gender=gender, age=age)


if __name__ == '__main__':
    app.run(debug=True)
