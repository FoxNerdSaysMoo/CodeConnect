from sanic import Sanic, response
from config import *
import os
from errors import *
from code import Code
from threading import Thread
import time
import json


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
        print(e)
        return response.text(e)
    return response.json(function)

@app.route('/addfunc')
async def upload_func(request):
    try:
        addfunc(json.loads(str(request.args).replace('\'', '"'))['code'])
        return response.text('Success')
    except Exception as e:
        print(e)
        return response.text(str(e))


def cli(host):
    time.sleep(1)
    send = Code.load_from_func(cli)
    send.save_to_server(host)
    recv = Code.load_from_server('cli', 'Fox', host)
    print(recv.repr())


if __name__ == '__main__':
    Thread(target=cli, args=['https://CodeConnect.foxnerdsaysmoo.repl.co']).start()
    app.run(host='0.0.0.0', port=8000)
    