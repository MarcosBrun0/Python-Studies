from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
pip3 install -r requirements.txt
This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///TopMovies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(300))
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String)


new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(Movie , movie_id)
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]

        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected)


@app.route("/delete", )
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(home)

@app.route('/add')
def add():
    return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)
