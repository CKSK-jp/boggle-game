from datetime import datetime, timedelta

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from boggle import Boggle


class BoggleApp(Flask):
    """
    Initialize the BoggleApp.

    Parameters:
    - import_name (str): The name of the import package.
    """

    def __init__(self, import_name):
        super().__init__(import_name)
        self.config["SECRET_KEY"] = "asdf123"
        self.debug = True
        self.boggle_instance = Boggle()
        self.initial_board = self.boggle_instance.make_board()


app = BoggleApp(__name__)

# set the time limit for a timed game
time_limit_seconds = 60


@app.route("/")
def boggle_homepage():
    """Render the homepage for the Boggle game."""
    session.setdefault("current_board")
    session.setdefault("found_words", [])
    session.setdefault("current_score", 0)
    session.setdefault("highscore", 0)

    return render_template(
        "home.html",
        current_board=session["current_board"],
        found_words=session["found_words"],
        current_score=session["current_score"],
        highscore=session["highscore"],
    )


@app.route("/submit-guess", methods=["POST"])
def submit_guess():
    """
    Handles the submission of a word guess.

    Returns:
    - JSON response containing information about the guess result.
    """
    data = request.get_json()
    guess = data.get("guess")
    result = app.boggle_instance.check_valid_word(session["current_board"], guess)

    if result == "ok":
        if guess not in session["found_words"]:
            message = "you found a word!"
            session["found_words"].append(guess)
            check_score(guess)
        else:
            message = "already guessed!"

    elif result == "not-on-board":
        message = "invalid guess"
    else:
        message = "not a word"
    return jsonify(
        {
            "foundWords": session["found_words"],
            "feedback": message,
            "score": session["current_score"],
            "highscore": session["highscore"],
        }
    )


def check_score(guess):
    """
    Update the game score based on the submitted word guess.

    Parameters:
    - guess (str): The word guessed by the player.

    Returns:
    - Tuple of the current score and high score.
    """
    session["current_score"] += len(guess)
    if session["current_score"] > session["highscore"]:
        session["highscore"] = session["current_score"]
    return session["current_score"], session["highscore"]


@app.route("/reset-game")
def reset_game():
    """Handles game reset press, ensuring necessary session variables are reset."""
    session["found_words"] = []
    session["current_board"] = app.boggle_instance.make_board()
    session["current_score"] = 0
    app.config.pop("duration", None)

    return redirect(url_for("boggle_homepage"))


@app.route("/start_timer")
def start_timer():
    """
    Start the timer for the timed game.

    Returns:
    - JSON response containing the remaining time.
    """
    if "duration" not in app.config:
        app.config["duration"] = datetime.now() + timedelta(seconds=time_limit_seconds)
    remaining_time = app.config["duration"] - datetime.now()
    remaining_seconds = remaining_time.total_seconds()

    if round(remaining_seconds) == 0:
        print("end timer")
        app.config.pop("duration", None)

    return jsonify({"duration": remaining_seconds})


@app.route("/stop_timer", methods=["POST"])
def stop_timer():
    """Stop the timer for the timed game."""
    app.config.pop("duration", None)
    return {"message": "Timer stopped successfully."}


if __name__ == "__main__":
    app.run(debug=True)
