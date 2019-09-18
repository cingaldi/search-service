from src import models

class IService:
    def getBase(self):
        pass

    def getFiltered(self , value):
        pass

class CoreService(IService):

    def __init__ (self , dataSource , navigateKey , filterKey):
        self.__treeModel = models.TreeModelFactory(dataSource).getInstance()
        self.__navigateKey = navigateKey
        self.__filterKey = filterKey

    def getBase(self):
        return self.__treeModel.navigateBy(self.__navigateKey).getLeaves()

    def getFiltered(self , value):
        return self.__treeModel.navigateBy(self.__navigateKey).filterBy(self.__filterKey , value).getLeaves()       

class CategoriesService(IService):

    def __init__ (self):
        self.__s = CoreService("data/categories" , "children" , "name")
    def getBase(self):
        return self.__s.getBase()

    def getFiltered(self , value):
        return self.__s.getFiltered(value)

class PsychographicsService(IService):

    def __init__ (self):
        self.__s = CoreService("data/psychographics" , "values" , "label")
    def getBase(self):
        return self.__s.getBase()

    def getFiltered(self , value):
        print(value)
        return self.__s.getFiltered(value)

class ServiceFactory:

    def getInstance(self , serviceType):

        if serviceType == "categories":
            return CategoriesService()
        elif serviceType == "psychographics":
            return PsychographicsService()
        else:
            return None

