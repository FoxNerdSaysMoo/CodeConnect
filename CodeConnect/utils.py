import errors


def striptabs(line):
    if line.startswith('    '):
        return line[4:]
    else: 
        raise errors.InvalidIndentsError(line)

def get_author():
    return 'Fox'

def confirmation(Code):
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