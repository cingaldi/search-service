from src import models

import unittest
import pytest


class TreeModelFactoryTestCase(unittest.TestCase):

    def test_creates_a_treeModel(self):

        tmf = models.TreeModelFactory('tests/fixtures/some')
        treeModel = tmf.getInstance()

        assert treeModel is not None

class TreeModelTestCase(unittest.TestCase):

    def test_gets_leaf_on_single_node(self):

        tmf = models.TreeModelFactory('tests/fixtures/some')
        tree = tmf.getInstance()

        result = tree.getLeaves()

        assert result  == [{'prop' : "value"}]
    
    def test_gets_leaves_on_oneleveltree(self):
        tmf = models.TreeModelFactory('tests/fixtures/oneleveltree')
        tree = tmf.getInstance()

        result = tree.getLeaves()

        assert result  == [{"prop" : "value1"} , {"prop" : "value2"}]

    def test_gets_leaves_on_twolevelunbalanced(self):
        tmf = models.TreeModelFactory('tests/fixtures/twolevelunbalanced')
        tree = tmf.getInstance()

        result = tree.getLeaves()
        assert result  == [{"prop" : "value1"} , {"prop" : "value3"}]


if __name__ == '__main__':
    unittest.main()