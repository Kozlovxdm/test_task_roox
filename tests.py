import unittest
from server import app
import json
import psycopg2

class SimpleTest(unittest.TestCase):

    def seed_test_data(self):
        try:
            conn = psycopg2.connect(dbname="dimon", user="dimon", password="dimon", host="localhost")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (id, name, second_name, surname) VALUES (1, 'Dmitriy', 'Sergeevich', 'Kozlov')")
            cur.execute("INSERT INTO users (id, name, second_name, surname) VALUES (2, 'Johann', 'Sebastian', 'Bach')")  
            cur.execute("INSERT INTO users (id, name, second_name, surname) VALUES (3, 'Wolfgang', 'Amadeus', 'Mozart')")
            cur.execute("INSERT INTO users (id, name, second_name, surname) VALUES (4, 'Ludwig', 'van', 'Beethoven')")  
            cur.execute("INSERT INTO users (id, name, surname) VALUES (5, 'Edvard', 'Grieg')")
            conn.commit()
        except Exception as e:
            print(str(e))
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def delete_seed_data(self):
        try:
            conn = psycopg2.connect(dbname="dimon", user="dimon", password="dimon", host="localhost")
            cur = conn.cursor()
            cur.execute("TRUNCATE users;")
            conn.commit()
        except Exception as e:
            print(str(e))
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def setUp(self):
        self.client = app.test_client()
        self.seed_test_data()

    def tearDown(self):
        self.delete_seed_data()

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
        self.assertEqual('Wolfgang', response_data.get('name'))
        self.assertEqual('Amadeus', response_data.get('second_name'))
        self.assertEqual('Mozart', response_data.get('surname'))

    def test_sucsess_user5(self):
        response = self.client.get('/user?id=5')
        self.assertEqual(200, response.status_code)
        response_data = response.data.decode('utf-8')
        response_data = json.loads(response_data)
        self.assertEqual('Edvard', response_data.get('name'))
        self.assertEqual('Grieg', response_data.get('surname'))

    def test_failed_user(self):
        response = self.client.get('/user?id=')
        self.assertEqual(400, response.status_code)

    def test_not_found(self):
        response = self.client.get('/user?id=6')
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
