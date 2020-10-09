import read
import code
import inspect
import utils


def confirmation(Code: code.Code):
    msg = f"""Confirm you want this function:
              - Author : {Code.author}
              - Description : A function
              - Inputs : {Code.anputs}
              - Outputs : {Code.autputs}
              - Code size : {len(Code.code)} lines
              (y/n) """
    answer = input(msg)
    if answer == 'y':
        return True
    else:
        return False

def func_save(Code: code.Code, save_file):
    define = f"def {Code.name}({' ,'.join(Code.inputs)}):"
    lines = [define] + ["    " + line for line in Code.code]

    with open(save_file, 'a') as file:
        file.writelines([line + "\n" for line in lines])

def func_load(func):
    lines = inspect.getsource(func)
    lines = [line for line in lines.split(sep="\n")[1:] if line]
    lines = [utils.striptabs(line) for line in lines]
    lines = [line for line in lines if line]
    inputs = list(func.__code__.co_varnames)

    name = func.__name__

    func_type = '.py'

    author = utils.get_author()

    Code = code.Code(
                     name,
                     author,
                     func_type,
                     inputs,
                     'No declared outputs',
                     lines
                     )
    
    return Code

if __name__ == '__main__':
    #test = read.get_code("test1", '000000', 'default.codeconnect')
    #func_save(test, "tests/CCfuncs.py")
    Code = func_load(func_load)
    