from random import randint
from flask import Flask, render_template

app = Flask(__name__)

def random_css_color() -> str:
    return f"rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})"

@app.route("/", methods=["GET", "POST"])
def home():
    color = random_css_color()
    colorA = random_css_color()
    colorB = random_css_color()
    return render_template("index.html", color=color, colorA=colorA, colorB=colorB)
