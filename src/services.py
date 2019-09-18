from src import models

class CategoriesService:

    def __init__ (self):
        self.__treeModel = models.TreeModelFactory("data/categories").getInstance()
    def getBase(self):
        return self.__treeModel.navigateBy("children").getLeaves()

    def getFiltered(self , value):
        return self.__treeModel.navigateBy("children").filterBy("name" , value).getLeaves()
