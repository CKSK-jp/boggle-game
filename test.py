from unittest import TestCase

from flask import session

from app import app
from boggle import Boggle


class FlaskTests(TestCase):
    # TODO -- write tests for every view function / feature!

    def display_board(self):
        with app.test_client() as client:
            # import pdb
            # pdb.set_trace
            res = client.get("/")
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>Test Title</h1>", html)
