from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy as sa

########## CONFIG ##########
DB_FILENAME = 'data.db'



########## CODE ##########
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILENAME}'
# class Base(DeclarativeBase): pass
# db = SQLAlchemy(model_class=Base)
# db.init_app(app)
db = SQLAlchemy(app)


#####
# DATA FORMAT

# Define what constitutes a book
class Book(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True, autoincrement="auto", unique=True)
    title: Mapped[str] = mapped_column(sa.String(250), nullable=False)
    author: Mapped[str] = mapped_column(sa.String(250), nullable=False)
    rating: Mapped[float] = mapped_column(sa.Float(), nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

# Define what constitutes the database (copy from the Book class)
all_books = db.Table(
    "books",
    sa.Column("id", db.Integer, primary_key=True),
    sa.Column("title", sa.ForeignKey(Book.title)),
    sa.Column("author", sa.ForeignKey(Book.author)),
    sa.Column("rating", sa.ForeignKey(Book.rating))
)

# SQLAlchemy make a database
with app.app_context():
    db.create_all()



##### Flask #####
@app.route('/')
def root():
    # return render_template('index.html', items=all_books)
    query = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template('index.html', rows=query)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_item = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('root'))
    return render_template('add.html')


# when route to /edit?id=1
@app.route("/edit", methods=['GET', 'POST'])
def edit():
    id = int(request.args.get('id'))
    if request.method == 'POST':
        row = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        row.title = request.form['title']
        row.author = request.form['author']
        row.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('root'))
    if id:
        row = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        return render_template('edit.html', id=id, title=row.title, author=row.author, rating=row.rating)
    return render_template('edit.html', id=id)

# when route to /delete?id=1
@app.route("/delete")
def delete():
    id = int(request.args.get('id'))
    if id:
        row = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.delete(row)
        db.session.commit()
    return redirect(url_for('root'))

if __name__ == '__main__':
    app.run(debug=True)

