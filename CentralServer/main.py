from sanic import Sanic, response
from config import *
import os
from errors import *
from code import Code


app = Sanic(__name__)

def getfunc(func, author):
    if MODE == 'folder':
        files = os.listdir(os.getcwd() + FOLDER)
        file = [file for file in files if file.startswith(func)]
        if len(file) != 1:
            raise ItemNotFoundError(func, len(file))
        return Code.load_from_file(func, author, os.getcwd() + FOLDER + file[0])

def addfunc(func):
    if ACCEPT_UPLOAD:
        code = Code.load_from_lines(func)
        code.save_as_code(os.getcwd() + FOLDER + code.name + '.codeconnect')
    return ACCEPT_UPLOAD

@app.route('/')
async def main(request):
    return response.text('This is the CodeConnect Official Server Website')

@app.route('/func/<funcname>/<author>')
async def func(request, funcname, author):
    try:
        function = getfunc(funcname, author).repr()
    except Exception as e:
        return response.text(e)
    return response.json(function)

@app.route('/addfunc')
async def upload_func(request):
    print(request.args)
    try:
        addfunc(request.args.get('code'))
        return response.text('Success')
    except Exception as e:
        return response.text(str(e))


app.run(host="0.0.0.0", port=8000)