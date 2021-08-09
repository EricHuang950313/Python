from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"
@app.route("/test")
def test():
    return "TestTest"

if __name__ == "__main__":
    app.run()