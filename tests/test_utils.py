from src import utils

import unittest
import pytest


class UtilsTestCase(unittest.TestCase):

    def test_loadJson(self):
        json = utils.loadJson("tests/fixtures/some.json")

        assert json['prop'] == "value" , "json is not well loaded"

    def test_loadJsonwithNoPath(self):

        with pytest.raises(Exception):
            assert utils.loadJson()

    def test_filter_match(self):

        filter = utils.Filter("name" , "ciccio")

        assert filter.match(dict({"name" : "ciccio"})) is True

    def test_filter_dont_match(self):

        filter = utils.Filter("name" , "ciccio")

        assert filter.match(dict({"name" : "bello"})) is False

    def test_filter_keynotfound(self):

        filter = utils.Filter("name" , "ciccio")

        assert filter.match(dict({"foo" : "ciccio"})) is False

if __name__ == '__main__':
    unittest.main()