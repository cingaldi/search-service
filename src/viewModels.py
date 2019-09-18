from flask import jsonify

def result(description="success" , result = ""):
    return jsonify({
        "description" : description,
        "result" : result
    })

def errorResult(description="error" , error="generic_error" , result=""):
    return jsonify({
        "description" : description,
        "error" : error,
        "result" : result
    })