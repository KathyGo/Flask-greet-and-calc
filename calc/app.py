# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask('__name__')

@app.route('/add')
def do_add():
    res = add(int(request.args["a"]), int(request.args["b"]))
    return f'<h1>{res}</h1>'

@app.route('/sub')
def do_sub():
    res = sub(int(request.args["a"]), int(request.args["b"]))
    return f'<h1>{res}</h1>'

@app.route('/mult')
def do_mult():
    res = mult(int(request.args["a"]), int(request.args["b"]))
    return f'<h1>{res}</h1>'

@app.route('/div')
def do_div():
    res = div(int(request.args["a"]), int(request.args["b"]))
    return f'<h1>{res}</h1>'

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<operation>')
def do_math(operation):
    # if operation == 'add':
    #     res = operations.add(int(request.args["a"]), int(request.args["b"]))
    # elif operation == 'sub':
    #     res = operations.sub(int(request.args["a"]), int(request.args["b"]))
    # elif operation == 'mult':
    #     res = operations.mult(int(request.args["a"]), int(request.args["b"]))
    # elif operation == 'div':
    #     res = operations.div(int(request.args["a"]), int(request.args["b"]))

    a = int(request.args["a"])
    b = int(request.args["b"])
    res = operators[operation](a,b)
    
    return f'<h1>{res}</h1>'