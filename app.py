from random import randint
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class ColorTripplet(db.Model):
    key = db.Column(db.Integer, primary_key=True)
    primary_color = db.Column(db.String(20), nullable=False)
    close_color = db.Column(db.String(20), nullable=False)
    far_color = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"ColorTriplet(primary: {self.primary_color}, close: {self.close_color}, far: {self.far_color})"

def random_css_color() -> str:
    return f"rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})"

@app.route("/", methods=["GET", "POST"])
def home():
    color = random_css_color()
    colorA = random_css_color()
    colorB = random_css_color()
    return render_template("index.html", color=color, colorA=colorA, colorB=colorB)

@app.route("/submit", methods=["POST"])
def submit():
    if "closest" in request.form:
        primary_color = request.form["color"]
        closest = request.form["closest"]
        close_color = request.form[closest]
        far_color = request.form[f"color{'A' if 'B' in closest else 'B'}"]
        color_triplet = ColorTripplet(
            primary_color=primary_color,
            close_color=close_color,
            far_color=far_color
        )
        db.session.add(color_triplet)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/list")
def list_triplets():
    return render_template("list.html", color_triplets=ColorTripplet.query.all())
