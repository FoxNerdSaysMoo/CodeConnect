import read
import code


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

if __name__ == '__main__':
    test = read.get_code("test1", '000000', 'default.codeconnect')
    func_save(test, "tests/CCfuncs.py")