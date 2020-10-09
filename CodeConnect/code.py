from utils import getnewid, striptabs, get_author
from errors import *
import inspect


class Code:
    def __init__(self, Name: str, Author: str, Type: str, Inputs: list, Outputs, Code: list):
        # Save to self
        self.name = Name
        self.author = Author
        self.type = Type
        self.inputs = Inputs
        self.outputs = Outputs
        self.code = Code
    
    def save(self, save_file = "default.codeconnect"):
        
        # Define values to put in file
        header = "[" + self.name + "]"
        type_statement = "TYPE = " + self.type
        id_statement = "id = " + self.author + " " + self.name
        input_top = "INPUTS:"
        code_top = "CODE:"
        code = ["~" + item for item in self.code]
        inputs = ["~" + item for item in self.inputs]
        outputs = ["~" + item for item in self.outputs]
        
        # Combine them all
        lines = [header, "", type_statement, "", id_statement, "", input_top] + inputs + ["", "RETURNS:"] + outputs + ["", code_top] + code
        
        #Write them
        with open(save_file, "a") as file:
            file.write("\n")
            for line in lines:
                file.write("\n")
                file.write(line)

    def func_save(Code, save_file):
        define = f"def {Code.name}({' ,'.join(Code.inputs)}):"
        lines = [define] + ["    " + line for line in Code.code]

        with open(save_file, 'a') as file:
            file.writelines([line + "\n" for line in lines])
    
    @staticmethod
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

    @staticmethod
    def func_load(func):
        lines = inspect.getsource(func)
        lines = [line for line in lines.split(sep="\n")[1:] if line]
        lines = [striptabs(line) for line in lines]
        lines = [line for line in lines if line]
        inputs = list(func.__code__.co_varnames)

        name = func.__name__

        func_type = '.py'

        author = get_author()

        Code = Code(
                    name,
                    author,
                    func_type,
                    inputs,
                    'No declared outputs',
                    lines
                    )
    
        return Code

    @staticmethod
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

        code = Code(Name, trimmed_lines[1].split()[2], trimmed_lines[1].split()[2], [], [], [code[1:] for code in trimmed_lines[5:]])
        return code

if __name__ == '__main__':
    code = Code.get_code("test2", 'Fox', 'default.codeconnect')
