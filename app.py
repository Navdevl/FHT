import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host="0.0.0.0", port=port)