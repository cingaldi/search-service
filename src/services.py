from src import models

class CategoriesService:

    def __init__ (self):
        self.__treeModel = models.TreeModelFactory("data/categories").getInstance()
    def getBase(self):
        return self.__treeModel.getLeaves()

    def getFiltered(self , value):
        return self.__treeModel.filterBy("name" , value).getLeaves()
