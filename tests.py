import os
import unittest
from app import create_app
from models import setup_db
import json


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['SQLALCHEMY_DATABASE_URI']
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'testia',
            'director': 'testia',
            'release_date': '1999',
            'desc': 'When a beautiful stranger leads computer \
                            hacker Neo to a forbidding underworld, \
                            he discovers the shocking truth--the life \
                            he knows is the elaborate deception \
                            of an evil cyber-intelligence.'
        }

        self.new_actor = {
            'name': 'Keanu Charles',
            'surname': 'Reeves',
            'age': 56,
            'gender': 'male'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Actors Tests
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(data['created'], 0)

    # def test_delete_actor(self):
    #     res = self.client().delete('/actors/23')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 23)

    def test_422_if_delete_actor_does_not_exist(self):
        res = self.client().delete('/actors/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Movies Tests
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(data['created'], 0)

    # def test_delete_movie(self):
    #     res = self.client().delete('/movies/13')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 13)

    def test_422_if_delete_movie_does_not_exist(self):
        res = self.client().delete('/movies/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


if __name__ == "__main__":
    unittest.main()
