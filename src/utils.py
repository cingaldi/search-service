import json


def loadJson(path):

    ret = None

    with open(path) as file:
        ret = json.load(file)
        file.close()

    return ret
    
class Filter:

    def __init__ (self , key = "" , value = ""):
        self.__key = key
        self.__value = value

    def match (self , myDict):
        return self.__key in myDict and  myDict[self.__key] == self.__value

    def disabled (self):
        return False

class DefaultFilter(Filter):
    def match (self , myDict):
        return False

    def disabled(self):
        return True