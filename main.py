#main.py

from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")

def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/", methods=["POST", "GET "])

def greet():
    flash("Hi there, " + request.form["name"])
    return render_template("index.html")
    
    request.form['']
    if request.method == "POST":
        name = request.form["name"]
        return render_template("greet.html", name=name)
    else:
        return render_template("error.html")
if __name__ == "__main__":
    app.secret_key = '51505150'
    app.run(host="127.0.0.1", port=8080, debug=True)

    