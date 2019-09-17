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


if __name__ == '__main__':
    unittest.main()