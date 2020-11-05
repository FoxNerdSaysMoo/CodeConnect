from sanic import Sanic, response
from config import *
import os
from errors import *
import code


app = Sanic(__name__)

def getfunc(func, author):
    if MODE == 'folder':
        files = os.listdir(os.getcwd() + FOLDER)
        file = [file for file in files if file.startswith(func)]
        if len(file) != 1:
            raise ItemNotFoundError(func, len(file))
        return code.Code.load_from_file(func, author, os.getcwd() + FOLDER + file[0])

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


app.run(host="0.0.0.0", port=8000)