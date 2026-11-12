import unittest
import requests
from config import base

AUTH = ("grass", "Corso_2026")  # utente creato con createsuperuser


class NewVisitorTest(unittest.TestCase):

    def test_can_add_a_film_and_retrieve_it_later_then_delete(self):
        movie = {
            "title": "Lupin III",
            "subtitle": "Il castello di Cagliostro",
            "director": "Hayao Miyazaki",
            "description": "The Castle of Cagliostro follows gentleman thief Lupin III."
        }

        post_response = requests.post(
            f"{base.api_url}/movies/", json=movie, auth=AUTH
        )
        self.assertEqual(201, post_response.status_code)
        pk = post_response.json()['id']

        get_response = requests.get(f"{base.api_url}/movies/", auth=AUTH)
        self.assertEqual(200, get_response.status_code)
        movie_list = get_response.json()

        for field in ("title", "director", "description"):
            self.assertIn(movie[field], [item[field] for item in movie_list])

        delete_response = requests.delete(
            f"{base.api_url}/movies/{pk}/", auth=AUTH
        )
        self.assertEqual(204, delete_response.status_code)

    def test_anonymous_cannot_access(self):
        response = requests.get(f"{base.api_url}/movies/")
        self.assertEqual(403, response.status_code)


if __name__ == '__main__':
    unittest.main()
