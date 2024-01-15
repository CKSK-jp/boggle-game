from flask import Flask, render_template, request

from boggle import Boggle

boggle_game = Boggle()
app = Flask(__name__)


@app.route("/")
def story_selection():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
