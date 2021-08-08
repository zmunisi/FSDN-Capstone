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

        self.edit_movie = {
            'title': 'Point Break',
            'director': 'Testia Directoria',
            'release_date': '2000',
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

        self.edit_actor = {
            'name': 'Edit Charles',
            'surname': 'Edit Reeves',
            'age': 57,
            'gender': 'female'
        }

    # Bearer Tokens
        self.casting_assistant = {
            'Authorization': 'Bearer ' + os.environ['CASTING_ASSISTANT']
        }
        self.casting_director = {
            'Authorization': 'Bearer ' + os.environ['CASTING_DIRECTOR']
            }
        self.executive_producer = {
            'Authorization': 'Bearer ' + os.environ['EXECUTIVE_PRODUCER']
            }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Actors Tests
    def test_get_actors(self):
        res = self.client().get('/actors',
                                headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(data['created'], 0)

    def test_edit_actor(self):
        res = self.client().post('/actors/1', json=self.edit_actor,
                                 headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(data['created'], 0)

    def test_delete_actor(self):
        res = self.client().delete('/actors/1',
                                   headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)

    def test_422_if_delete_actor_does_not_exist(self):
        res = self.client().delete('/actors/10000',
                                   headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Movies Tests
    def test_get_movies(self):
        res = self.client().get('/movies',
                                headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(data['created'], 0)

    def test_edit_movie(self):
        res = self.client().post('/movies/1', json=self.edit_movie,
                                 headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertNotEqual(data['created'], 0)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1',
                                   headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)

    def test_422_if_delete_movie_does_not_exist(self):
        res = self.client().delete('/movies/10000',
                                   headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


if __name__ == "__main__":
    unittest.main()
