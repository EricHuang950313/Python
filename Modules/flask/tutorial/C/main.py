from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "e937d6d16f4ccd6ef8ca0b61fde04e76b0318e69"

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
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"{form.username.data} created!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Rigistration", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "abc@abc.com" and form.password.data == "123":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)