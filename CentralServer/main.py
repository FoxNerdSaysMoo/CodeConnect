from sanic import Sanic, responce
from config import *


app = Sanic(__name__)

def getfunc(func, file):
    if MODE == 'file':
        with open(file, 'r') as readfile:
            pass

@app.route('/'):
    return responce.text('under development')