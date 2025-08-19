import flask as fl
import requests as rq
import random as r
import datetime as dt

app = fl.Flask(__name__)

response = rq.get('https://api.npoint.io/de18561c3767e6dc49db')
response.raise_for_status()
blog_data = response.json()

# add dates to posts
for i in blog_data:
    i['date'] = f'{r.randint(2000, 2025)}-{str(r.randint(1, 12)).zfill(2)}-{str(r.randint(1, 28)).zfill(2)}'


@app.route('/')
def root():
    return fl.render_template('index.html',
        img='home-bg.jpg',
        title='Clean Blog',
        subtitle='A Blog Theme by Start Bootstrap',
        posts=blog_data)


@app.route('/about/')
def about():
    return fl.render_template('about.html',
        img='about-bg.jpg',
        title='About Me',
        subtitle='This is what I do.')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if fl.request.method == 'GET':
        return fl.render_template('contact.html',
            img='contact-bg.jpg',
            title='Contact Me',
            subtitle='Have questions? I have answers.')
    elif fl.request.method == 'POST':
        name = fl.request.form['name']
        email = fl.request.form['email']
        phone = fl.request.form['phone']
        message = fl.request.form['message']
        message_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
        with open('output.txt', 'at') as f:
            f.write(f'===== {message_time} =====\n{name}\n{email}\n{phone}\n\n{message}\n\n')
        return fl.render_template('contact-sent.html',
            img='contact-bg.jpg',
            title='Contact Me',
            subtitle='Have questions? I have answers.')


@app.route('/post/<int:nr>')
def post(nr):
    return fl.render_template('post.html',
        img='post-bg.jpg',
        title=blog_data[nr-1]['title'],
        subtitle=blog_data[nr-1]['subtitle'],
        post=blog_data[nr-1]['body'])


if __name__ == '__main__':
    app.run(debug=True)
