from flask import Flask

app = Flask(__name__)

num_row = 0
num_cols = 0

@app.route("/")
def home():
    with open("frontend/index.html") as f:
        return f.read()

@app.route("/tool")
def tool():
    with open("frontend/tool.html") as f:
        return f.read().replace("tobereplaced1", "500").replace("tobereplaced2", "500")
if __name__ == "__main__":
    app.run(port=2000, debug=True)