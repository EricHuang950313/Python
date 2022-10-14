from flask import Flask, render_template, url_for
# url_for: href="{{ url_for('folder_name', filename='file_name') }}" --> Find the file in a specific folder in html file.

# template_folder="folder_name" --> Getting templates from a specific folder to use function render_template().
app = Flask(__name__, template_folder="templates")

posts = [
    {
        "author": "Eric Huang",
        "title": "Blog Posted 1",
        "contents": "First post content",
        "date_posted": "8/8/2021"
    },
    {
        "author": "Eric Huang",
        "title": "Blog Posted 2",
        "contents": "Second post content",
        "date_posted": "8/8/2021"
    }
]

@app.route("/")
def home():
    # Render a template from the given template source string.
    # flask uses "jinja" as a templating engine, which allows people to write programs in HTML.
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    # Render a template from the given template source string.
    # flask uses "jinja" as a templating engine, which allows people to write programs in HTML.
    return render_template("about.html", title="About")


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)