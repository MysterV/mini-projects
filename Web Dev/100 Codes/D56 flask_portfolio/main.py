import flask as fl

app = fl.Flask(__name__)


@app.route('/')
def root():
    return fl.render_template('index.html')


@app.route('/about')
def about():
    return fl.render_template('index.html')


@app.route('/projects')
def projects():
    return fl.render_template('index.html')


@app.route('/sheets')
def sheets():
    return fl.render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
