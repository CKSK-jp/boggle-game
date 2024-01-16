from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdf123"
app.debug = True

boggle_instance = Boggle()
initial_board = boggle_instance.make_board()
found_words = []
score = 0


@app.route("/")
def boggle_homepage():
    session.setdefault("current_board", initial_board)
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
    result = boggle_instance.check_valid_word(session["current_board"], guess)

    if result == "ok":
        if guess not in found_words:
            message = "you found a word!"
            found_words.append(guess)
            session["found_words"] = found_words

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
    session["current_board"] = boggle_instance.make_board()
    session["current_score"] = 0
    return redirect(url_for("boggle_homepage"))


if __name__ == "__main__":
    app.run(debug=True)
