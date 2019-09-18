from  src import utils

class TreeModel:

    def __init__(self):
        self.__tree = {}
        self.__selector = "children"
        self.__filter = None

    def navigateBy(self , selector):
        self.__selector = selector
        return self

    def filterBy(self , key , value):
        self.__filter = {"key" : key , "value" : value}
        return self

    def getLeaves(self):

        leaves = []
        for root in self.__tree:
            for node in self._visit(root):
                if self.__selector not in node:
                    if self.__filter is None or node["mark"] is True:
                        del node["mark"]
                        leaves.append(node)
        return leaves

    def _setTree(self , tree):
        self.__tree = tree

    def _visit(self , node , mark=False ):

        markSubtree = mark
        if self.__filter is not None:
            if self.__filter["key"] in node and node[self.__filter["key"]] == self.__filter["value"]:         
              markSubtree = True
        
        node["mark"] = markSubtree
        yield node
        
        #recursive step
        if self.__selector in node:
            for i in node[self.__selector]:

                for child in self._visit(i , markSubtree):
                    yield child

class TreeModelFactory:

    def __init__(self , name):
        self.__name = name

    def getInstance(self):
        ret = TreeModel()
        ret._setTree(utils.loadJson("{0}.json".format(self.__name)))

        return ret
