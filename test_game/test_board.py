from unittest import TestCase

from flask import session

from app import app
from boggle import Boggle


class GameBoardTests(TestCase):
    # TODO -- write tests for every view function / feature!

    @classmethod
    def setUpClass(cls):
        cls.boggle_instance = Boggle()
        cls.initial_board = cls.boggle_instance.make_board()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()

    def test_display_board(self):
        with app.test_client() as client:
            res = client.get("/")
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn("<tr>", html)

    def test_board_generation(self):
        board = self.boggle_instance.make_board()
        self.assertEqual(len(board), 5)
        self.assertTrue(all(len(row) == 5 for row in board))

    def test_reset_found_words(self):
        with app.test_client() as client:
            res = client.get("/reset-game")
            self.assertEqual(res.status_code, 302)
            self.assertEqual(session["found_words"], [])

    def test_reset_board(self):
        with app.test_client() as client:
            res = client.get("/reset-game")
            self.assertEqual(res.status_code, 302)
            self.assertNotEqual(session["current_board"], self.initial_board)
