from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

num_row = 0
num_cols = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tool")
def tool():
    return render_template("tool.html")
    
if __name__ == "__main__":
    app.run(port=2010, debug=True)