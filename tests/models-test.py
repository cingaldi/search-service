from src import models

import unittest
import pytest


class TreeModelFactoryTestCase(unittest.TestCase):

    def test_creates_a_treeModel(self):

        tmf = models.TreeModelFactory('tests/fixtures/some')
        treeModel = tmf.getInstance()

        assert treeModel is not None

class TreeModelTestCase(unittest.TestCase):

    def test_gets_leaf_on_zerolevel(self):

        tmf = models.TreeModelFactory('tests/fixtures/zerolevelthree')
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

    def test_gets_leaves_on_multiroot(self):
        tmf = models.TreeModelFactory('tests/fixtures/multiroot')
        tree = tmf.getInstance()

        result = tree.getLeaves()
        assert result  == [{"prop" : "value1"} , {"prop" : "value2"}]

    def txest_gets_leaves_on_threeleveletc(self):
        tmf = models.TreeModelFactory('tests/fixtures/threelevelbalancedfigli')
        tree = tmf.getInstance()

        result = tree.navigateBy("figli").getLeaves()
        assert result  == [{"prop" : "value4"} , {"prop" : "value5"} , {"prop" : "value6"}]

    def test_gets_leaves_and_filterbyname(self):
        tmf = models.TreeModelFactory('tests/fixtures/filterbyname')
        tree = tmf.getInstance()

        result = tree.filterBy("name" , "ciccio").getLeaves()
        print(result)
        assert result  == [{"prop" : "value4"} , {"prop" : "value5"}]


if __name__ == '__main__':
    unittest.main()