import flask as fl

app = fl.Flask(__name__)

@app.route('/')
def root():
    return fl.render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return fl.render_template('login.html', login=fl.request.form['email'], password=fl.request.form['password'])

if __name__ == '__main__':
    app.run(debug=True)