from flask import Flask , request

from src import services
from src import viewModels
app = Flask(__name__)


@app.route('/health')
def health():
    return ('' , 200)

@app.route('/trees/<treeType>')
def getTree(treeType):

    s = services.ServiceFactory().getInstance(treeType)
    if s is None:
        return (viewModels.errorResult(error="tree_not_found" , result="tree type does not exist") , 404)
    else:
        filterBy = request.args.get("filterBy" , default=None)
        result =  []
        description = None
        if filterBy is not None:
            result = s.getFiltered(filterBy)
            description = "all tree leaves filtered by value {0}".format(filterBy)
        else:
            result = s.getBase()
            description="all tree leaves"

        return (viewModels.result(description=description , result=result) , 200)




if __name__ == '__main__':
    app.run()