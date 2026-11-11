import unittest
import requests
from config import base

class NewVisitorTest(unittest.TestCase):

    def test_can_add_a_film_and_retrieve_it_later_then_delete(self):

        movie = {
            "title": "Lupin III",
            "subtitle": "Il castello di Cagliostro",
            "director": "Hayao Miyazaki",
            "description": "The Castle of Cagliostro follows gentleman thief Lupin III."
        }

        # Create a movie
        post_response = requests.post(
            f"{base.api_url}/movies/",
            json=movie
        )

        self.assertEqual(201, post_response.status_code)

        pk = post_response.json()['id']

        # Retrieve the movie list
        get_response = requests.get(
            f"{base.api_url}/movies/"
        )

        self.assertEqual(200, get_response.status_code)

        movie_list = get_response.json()

        self.assertIn(
            movie['title'],
            [item['title'] for item in movie_list]
        )

        self.assertIn(
            movie['director'],
            [item['director'] for item in movie_list]
        )

        self.assertIn(
            movie['description'],
            [item['description'] for item in movie_list]
        )

        # Delete the movie
        delete_response = requests.delete(
            f"{base.api_url}/movies/{pk}/"
        )

        self.assertEqual(204, delete_response.status_code)


if __name__ == '__main__':
    unittest.main()
