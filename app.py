from flask import Flask, flash, jsonify, redirect, render_template, request, session

from boggle import Boggle

# from flask_debugtoolbar import DebugToolbarExtension


# boggle_game = Boggle()
app = Flask(__name__)
app.config["SECRET_KEY"] = "asdf123"

app.debug = True
# toolbar = DebugToolbarExtension(app)

boggle_instance = Boggle()
board = boggle_instance.make_board()
found_words = []


@app.route("/")
def boggle_homepage():
    session["current_board"] = board
    return render_template("home.html", game_board=board)


@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    data = request.get_json()
    guess = data.get("guess")

    result = boggle_instance.check_valid_word(board, guess)
    if result == "ok":
        message = "you found a word!"
        found_words.append(guess)
    elif result == "not-on-board":
        message = "invalid guess"
    else:
        message = "not a word"

    return jsonify({"foundWords": found_words, "feedback": message})


@app.route("/redirect-me")
def redirect_me():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
