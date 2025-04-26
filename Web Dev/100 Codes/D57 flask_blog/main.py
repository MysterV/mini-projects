import flask as fl
import requests

app = fl.Flask(__name__)
data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
posts = [i for i in data]


@app.route('/')
def home():
    return fl.render_template('index.html', posts=posts)


@app.route('/blog/<int:id>')
def blog(id):
    post = posts[id-1]
    return fl.render_template('post.html', title=post['title'], subtitle=post['subtitle'], post=post['body'])


if __name__ == '__main__':
    app.run(debug=True)
