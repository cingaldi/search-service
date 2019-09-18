from flask import Flask , request , jsonify

from src import services

app = Flask(__name__)


@app.route('/health')
def health():
    return ('' , 200)

@app.route('/trees/<treeType>')
def getTree(treeType):
    s = services.ServiceFactory().getInstance(treeType)
    if s is None:
        return ({"error" : "tree type does not exist"} , 404)
    else:
        return (jsonify(s.getBase()) , 200)




if __name__ == '__main__':
    app.run()