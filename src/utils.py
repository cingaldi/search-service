import json


def loadJson(path):

    ret = None

    with open(path) as file:
        ret = json.load(file)
        file.close()

    return ret
    