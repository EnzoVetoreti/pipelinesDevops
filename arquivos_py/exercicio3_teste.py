import unittest
from arquivos_py.exercicio3 import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_devops(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Germinare', response.data)

if __name__ == '__main__':
    unittest.main()
