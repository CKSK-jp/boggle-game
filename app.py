from flask import Flask, redirect, render_template, request, session

from boggle import Boggle

# from flask_debugtoolbar import DebugToolbarExtension


# boggle_game = Boggle()
app = Flask(__name__)
app.config["SECRET_KEY"] = "asdf123"

app.debug = True
# toolbar = DebugToolbarExtension(app)


@app.route("/")
def boggle_homepage():
    session["count"] = session.get("count", 0) + 1
    return render_template("home.html")


@app.route("/submit-form", methods=["POST"])
def get_form():
    if request.method == "POST":
        print(request.form)
        return ("", 204)
    # fav_color = request.form.get("color")
    # return render_template("color.html", fav_color=fav_color)


@app.route("/redirect-me")
def redirect_me():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
