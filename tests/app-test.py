from src import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_health(self):
        tester = app.app.test_client(self)
        response = tester.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_categories(self):
        tester = app.app.test_client(self)
        response = tester.get('/trees/categories')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"][0]["name"] , "Classical Music")


    def test_unknown(self):
        tester = app.app.test_client(self)
        response = tester.get('/trees/unknown')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["error"] , "tree_not_found")


    def test_filterBy(self):
        tester = app.app.test_client(self)
        response = tester.get('/trees/categories?filterBy=Products%20%26%20Services')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"][0]["name"] , "Cars")
if __name__ == '__main__':
    unittest.main()