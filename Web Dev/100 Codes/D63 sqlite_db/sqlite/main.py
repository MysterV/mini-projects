from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# ===== CONFIG =====
db_filename = 'data.db'


# ===== CODE =====
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_filename}'


# SQLite
db = sqlite3.connect(db_filename, check_same_thread=False)
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(250) NOT NULL UNIQUE,
    author varchar(250) NOT NULL,
    rating FLOAT NOT NULL
)''')
db.commit()


# ===== Flask =====
@app.route('/')
def root():
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    print(rows)
    return render_template('index.html', rows=rows)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cursor.execute('INSERT INTO books (title, author, rating) VALUES(?, ?, ?)', (request.form['title'], request.form['author'], request.form['rating']))
        db.commit()
        return redirect(url_for('root'))
    return render_template('add.html')

# when route to /edit?id=1
@app.route("/edit", methods=['GET', 'POST'])
def edit():
    id = int(request.args.get('id'))
    if request.method == 'POST':
        cursor.execute('UPDATE books SET title=?, author=?, rating=? where id=?', (request.form['title'], request.form['author'], request.form['rating'], id))
        db.commit()
        return redirect(url_for('root'))
    if id:
        cursor.execute(f'SELECT * FROM books WHERE id={id}')
        row = cursor.fetchall()[0]
        return render_template('edit.html', id=id, title=row[1], author=row[2], rating=row[3])
    return render_template('edit.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)

