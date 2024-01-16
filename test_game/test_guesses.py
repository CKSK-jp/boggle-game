import logging
from unittest import TestCase

from flask import session

from app import app
from boggle import Boggle


class UserGuessTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boggle_instance = Boggle()
        cls.initial_board = [
            ["A", "B", "C", "R", "B"],
            ["A", "B", "C", "R", "B"],
            ["C", "A", "B", "R", "B"],
            ["A", "B", "C", "R", "B"],
            ["A", "B", "C", "R", "B"],
        ]

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_valid_word_submission(self):
        with app.test_client() as client:
            # Set 'current_board' in the session using client
            with client.session_transaction() as sess:
                sess["current_board"] = self.initial_board

            res = client.post("/submit-guess", json={"guess": "cab"})
            data = res.get_json()
            guess = data.get("guess")
            self.assertEqual(
                self.boggle_instance.check_valid_word(session["current_board"], guess),
                "ok",
            )
