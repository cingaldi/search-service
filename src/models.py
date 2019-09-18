from  src import utils

class TreeModel:

    def __init__(self):
        self.__tree = {}
        self.__selector = ""

    def navigateBy(self , selector):
        self.__selector = selector
        return self

    def getLeaves(self):

        leaves = []
        for node in self._visit(self.__tree[0]):
            if "children" not in node:
                leaves.append(node)
        return leaves

    def _setTree(self , tree):
        self.__tree = tree

    def _visit(self , node ):

        yield node
        
        #recursive step
        if "children" in node:
            for i in node["children"]:

                for child in self._visit(i):
                    yield child

class TreeModelFactory:

    def __init__(self , name):
        self.__name = name

    def getInstance(self):
        ret = TreeModel()
        ret._setTree(utils.loadJson("{0}.json".format(self.__name)))

        return ret
