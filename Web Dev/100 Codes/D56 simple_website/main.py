import flask as fl

app = fl.Flask(__name__)
@app.route('/')
def hi():
    return fl.render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
