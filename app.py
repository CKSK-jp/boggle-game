from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from boggle import Boggle


class BoggleApp(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self.config["SECRET_KEY"] = "asdf123"
        self.debug = True
        self.boggle_instance = Boggle()
        self.initial_board = self.boggle_instance.make_board()


app = BoggleApp(__name__)


@app.route("/")
def boggle_homepage():
    session.setdefault("current_board", [])
    session.setdefault("found_words", [])
    session.setdefault("current_score", 0)

    return render_template(
        "home.html",
        current_board=session["current_board"],
        found_words=session["found_words"],
        current_score=session["current_score"],
    )


@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    data = request.get_json()
    guess = data.get("guess")
    result = app.boggle_instance.check_valid_word(session["current_board"], guess)

    if result == "ok":
        if guess not in session["found_words"]:
            message = "you found a word!"
            session["found_words"].append(guess)
            session["current_score"] += len(guess)
        else:
            message = "already guessed!"

    elif result == "not-on-board":
        message = "invalid guess"
    else:
        message = "not a word"
    print(session["found_words"], session["current_score"])
    return jsonify(
        {
            "foundWords": session["found_words"],
            "feedback": message,
            "score": session["current_score"],
        }
    )


@app.route("/reset-game")
def reset_game():
    session["found_words"] = []
    session["current_board"] = app.boggle_instance.make_board()
    session["current_score"] = 0
    return redirect(url_for("boggle_homepage"))


if __name__ == "__main__":
    app.run(debug=True)
