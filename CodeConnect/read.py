from code import Code
from errors import ItemNotFoundError


def get_code(Name, Id, read_file):
    info = []
    
    # Read file
    with open(read_file, 'r') as lines:
        curr_name = ""
        curr_id = 0
        success = False
        for line in lines:
            
            # If the line is a header, find out the name
            if line[0] == '[':
                curr_name = line[1:line.find(']')]
                continue
                
            # If it is the correct header, try to get the id
            elif curr_name == Name and len(line.split()) >= 1:
                if line.split()[0] == 'id':
                    curr_id = line.split()[2]
            
            if curr_name == Name and curr_id == Id:
                if line.rstrip():
                    info.append(line.rstrip())
                    success = True
        if not success:
        	raise ItemNotFoundError(f'Item {Name} with Id {Id}, was not found')
    
    code = Code(Name, info[2].split()[2], [], [], [code[1:] for code in info[7:]])
    return code