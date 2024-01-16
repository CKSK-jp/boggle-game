from unittest import TestCase

from flask import session

from app import app
from boggle import Boggle

app.config["TESTING"] = True
app.config["DEBUG_TP_HOSTS"] = ["dont-show-debug-toolbug"]


class FlaskTests(TestCase):
    # TODO -- write tests for every view function / feature!

    # @classmethod
    # def setUpClass(cls) -> None:
    #     return super().setUpClass()

    # @classmethod
    # def tearDownClas(cls) -> None:
    #     return super().setUpClass()

    # def setUp(self):
    #     with app.test_client() as client:
    #         res = client.get("/")

    # def tearDown(self):
    #     print("inside tear down")

    def test_display_board(self):
        with app.test_client() as client:
            res = client.get("/")
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn("<h1>Test Title</h1>", html)

    def test_form_post(self):
        with app.test_client() as client:
            res = client.post("/fav-color", data={"color": "orange"})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("<h3>Whoa! I like orange, too</h3>", html)

    def test_redirection(self):
        with app.test_client() as client:
            res = client.get("/redirect-me")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.location, "https://localhost/")

    def test_redirection_followed(self):
        with app.test_client() as client:
            res = client.get("/redirect-me", follow_redirects=True)
            self.assertEqual(res.status_code, 200)

    def test_session_count(self):
        with app.test_client() as client:
            res = client.get("/")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(session["count"], 1)

    def test_set_session(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["count"] = 999

            res = client.get("/")
            self.assertEqual(res.status_code, 200)
            self.assertEqual(session["count"], 1000)
