from code import Code
from errors import ItemNotFoundError


def get_code(Name, Id, read_file):
    trimmed_lines = []
    data = [Name] + Id.split()
    
    # Read file
    with open(read_file, 'r') as lines:
        curr_name = ""
        curr_id = 0
        success = False
        for line in lines:
            
            # If the line is a header, find out the name
            if line[0] == '[':
                curr_name = line[1:line.find(']')]
                if success:
                    break
                trimmed_lines.append(line)
                continue
                
            # If it is the correct header, try to get the id
            elif curr_name == Name and len(line.split()) >= 1:
                if line.split()[0] == 'id':
                    curr_id = line.split()[2]
            
            if curr_name == Name and curr_id == Id:
                if line.rstrip():
                    trimmed_lines.append(line.rstrip())
                    success = True
        if not success:
        	raise ItemNotFoundError(f'Item "{Name}" with Id "{Id}", was not found')
    
    code = Code(Name, trimmed_lines[1].split()[2], trimmed_lines[2].split()[2], [], [], [code[1:] for code in trimmed_lines[7:]])
    return code


def get_code_from_func


if __name__ == '__main__':
    code = get_code("test1", '000000', 'default.codeconnect')
