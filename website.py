from flask import Flask, redirect, render_template

#Configure application
app = Flask(__name__,template_folder="templates",static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/experience")
def experience():
    return render_template("Experience.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")