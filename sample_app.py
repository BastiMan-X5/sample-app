from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "This is a sample app" # O el retorno que pida tu lab

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)