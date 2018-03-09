import unittest
from server import app
import json

class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        ...

    def test_sucsess_user1(self):
        response = self.client.get('/user?id=1')
        self.assertEqual(200, response.status_code)
        response_data = response.data.decode('utf-8')
        response_data = json.loads(response_data)
        self.assertEqual('Dmitriy', response_data.get('name'))
        self.assertEqual('Sergeevich', response_data.get('second_name'))
        self.assertEqual('Kozlov', response_data.get('surname'))

    def test_sucsess_user3(self):
        response = self.client.get('/user?id=3')
        self.assertEqual(200, response.status_code)
        response_data = response.data.decode('utf-8')
        response_data = json.loads(response_data)
        self.assertEqual('Volfgan', response_data.get('name'))
        self.assertEqual('Amadei', response_data.get('second_name'))
        self.assertEqual('Mozart', response_data.get('surname'))

    def test_sucsess_user5(self):
        response = self.client.get('/user?id=5')
        self.assertEqual(200, response.status_code)
        response_data = response.data.decode('utf-8')
        response_data = json.loads(response_data)
        self.assertEqual('Edvard', response_data.get('name'))
        self.assertEqual('Greeg', response_data.get('surname'))

    def test_failed_user(self):
        response = self.client.get('/user?id=')
        self.assertEqual(400, response.status_code)

    def test_not_found(self):
        response = self.client.get('/user?id=6')
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
