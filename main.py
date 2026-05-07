from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

num_row = 0
num_cols = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/path-builder")
def path():
    return render_template("path-builder.html")

@app.route("/map-builder")
def map():
    return render_template("map-builder.html")
    
if __name__ == "__main__":
    app.run(port=2010, debug=True)