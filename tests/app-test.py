from src import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.app.test_client(self)
        response = tester.get('/health')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()