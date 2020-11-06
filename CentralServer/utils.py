class ItemNotFoundError(Exception):
    pass

class InvalidIndentsError(Exception):
    pass


def striptabs(line):
    if line.startswith('    '):
        return line[4:]
    else: 
        raise InvalidIndentsError(line)

def get_author():
    return 'Fox'

def confirmation(Code):
    msg = f"""Confirm you want this function:
              - Author : {Code.author}
              - Description : A function
              - Inputs : {Code.inputs}
              - Outputs : {Code.outputs}
              - Code size : {len(Code.code)} lines
              (y/n) """
    answer = input(msg)
    if answer == 'y':
        return True
    else:
        return False

def filter(item):
    return ''.join([letter for letter in item if letter in 'abcdefghijklmnopqrstuvwxyz-_ABCDEFGHIJKLMNOPQRSTUVWXYZ'])