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

    # Bearer Tokens
        self.casting_assistant = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZUX2tzNVV2dmpjWlF4dEZqN2tJciJ9.eyJpc3MiOiJodHRwczovL3ptdW5pc2kuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMGQ0NDRhMzhhMzBiMDA2YWM4ODliNSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjI4MzM3OTAyLCJleHAiOjE2Mjg0MjQzMDIsImF6cCI6Ijh4dkFOOTl6d3JUUjhsNFBEQW1oeHpQdWZvM0JadUt2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.r-J7jPiAOy40kxsalN9dbVGtx8qrUpM-MhTXLqpRX_BI7PkxmAbU3QiOZQadj81a69kqrBX0w1pDXj140WyyjSJcIdP29C2X6OZM4AH_6OSby-IdtyYoAFiCCidYJHdFFMvzViuOzDBxhODxglFMFNI_iF7dS8TZonzpGiUfx84bK56P0sS33kOkSnlHOHKCfFNCLscMoAPTCn63-nyzvSMKIgWV6H8bl4pgKQFp59zmNGGroHHTE_dP5JQFCQw-T37xgYV2Td5J2nIQE0EBedPIhYoJtqkum9jqX_l0HUwfRx8eWr_zUQWlKNmzBD3looAfozn9KzsVbzm-ujzJog'
        }
        self.casting_director = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZUX2tzNVV2dmpjWlF4dEZqN2tJciJ9.eyJpc3MiOiJodHRwczovL3ptdW5pc2kuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMGU3NjMzNmFiZjNkMDA3MDE4YzUxZiIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjI4MzM4MDE0LCJleHAiOjE2Mjg0MjQ0MTQsImF6cCI6Ijh4dkFOOTl6d3JUUjhsNFBEQW1oeHpQdWZvM0JadUt2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.nHG-_VvH_sHt1V5e5-wiHkMa4q9DPoiiW0lXKcrvlKHDtaC5o2hKXqSwvhmS8AwTOQOwOoWPQYW3CEbq1oWa5mkGSBmilt5gBJVOD8sj5GXPIa0Fg4758q4umLTAjoEjPctHHvcn-gbuoHfI0tGrb0qQ05O_FOpoYS2UXev0udDUeXoOe726-iCJajFt6D-i1bsG0wiP67ytckMNYJICoS8on5r1G_BKWUrULegYjDYTadVnR_LvJYmwwhiXPJWMiZ3n9BF1En37aX1AlhP6svPIHMNKQHGEuieDi0YvhNwpE4lTmtkc44S7vbpi2jmtS29SZEVbRxm1WVK5mLCM7g'
        }
        self.executive_producer = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZUX2tzNVV2dmpjWlF4dEZqN2tJciJ9.eyJpc3MiOiJodHRwczovL3ptdW5pc2kuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMGU3NmE0MGFiMDlhMDA2ODQxYTJiOCIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjI4MzM5MDAwLCJleHAiOjE2Mjg0MjU0MDAsImF6cCI6Ijh4dkFOOTl6d3JUUjhsNFBEQW1oeHpQdWZvM0JadUt2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.l5nXvHU3vpZKWV5HOEUIQbCzIoz9va-8yShBzaTDv0s74LijGBnXK_J8XIg491fXt7jdzAJC1mb8BU5P4WUhTUugBgg1snsKmQ_NXm8eJp682r-5xdRdlez2qmRw8AQwgrPe6YhWDNCHPC5uTudP0WiDCRz6EB5sO27buy-SZeVbvkjADNEkR45P60O4yk52UWzBvnjOeX4399vaceIFX9D6H40pw0bYYdJ0Y1s7948XQ-ZGk69ZSWF0XC2zviSuxhoTjzlbUSvLkD51h9S_Ulho-1txMv-WXNZLc2NfJIho5b-PhrHAJ42YdVjtlt4RjExLYFDvP9Jm1O5zb7zULg'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Actors Tests
    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.casting_director)
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
        res = self.client().delete('/actors/10000', headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    # Movies Tests
    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.casting_director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.casting_director)
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
        res = self.client().delete('/movies/10000', headers=self.executive_producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


if __name__ == "__main__":
    unittest.main()
