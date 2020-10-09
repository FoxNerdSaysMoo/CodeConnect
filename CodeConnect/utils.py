import errors


def getnewid(name: str, read_file: str):
    
    # Define a few variables
    new_id = 0
    used_ids = []
    
    # Read file
    with open(read_file, 'r') as lines:
        curr_name = ""
        for line in lines:
            
            # If the line is a header, find out the name
            if line[0] == '[':
                curr_name = line[1:line.find(']')]
            
            # If it is the correct header, try to get the id
            elif curr_name == name and len(line.split()) >= 1:
                if line.split()[0] == 'id':
                    used_ids.append(int(line.split()[2]))
    # Find the next unused id
    for i in range(10000000):
        if i not in used_ids:
            new_id = str(i)
            break
    
    # Finalize the id
    while len(new_id) < 6:
        new_id = "0" + new_id
    return new_id

def striptabs(line):
    if line.startswith('    '):
        return line[4:]
    else: raise errors.InvalidIndentsError(line)

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