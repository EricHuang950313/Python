from flask import Flask

# The first argument is the name of the application’s module or package. It helps flask to find templates and static files.
app = Flask(__name__)

# @app.route("") --> String inside "" stands for the path for the website.
@app.route("/")
def home():
    # return HTML
    return "<h1>Home Page</h1>"

# @app.route("") --> String inside "" stands for the path for the website. 
@app.route("/about")
def about():
    # return HTML
    return "<h1>About Page</h1>"


# How to run the file:
# A. Environment Variable
# B. Code in Python file 
# Solution A:
# $env:FLASK_APP="main.py"
# $env:FLASK_DEBUG=0 -->close(default); $env:FLASK_DEBUG=1 -->open
# flask run
# Solution B:
if __name__ == "__main__":
    # app.run()
    app.run(debug=True)