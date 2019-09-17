from  src import utils

class TreeModel:

    def __init__(self):
        self.__tree = {}
        self.__selector = ""

    def navigateBy(self , selector):
        self.__selector = selector
        return self

    def getLeaves(self):

        if self.__selector == "":
            return self.__tree
        else:
            return self._visit(self.__tree , [])

    def _setTree(self , tree):
        self.__tree = tree

    def _visit(self , node , visited):
        print (node)
        if self.__selector in node and isinstance(node[self.__selector] , list):
            for i = 1 to len(node[self.__selector]:
                visited.append(self._visit(node[self.__selector][i] , visited))
        else:
            visited.append(node)
        
        return visited

class TreeModelFactory:

    def __init__(self , name):
        self.__name = name

    def getInstance(self):
        ret = TreeModel()
        ret._setTree(utils.loadJson("{0}.json".format(self.__name)))

        return ret
