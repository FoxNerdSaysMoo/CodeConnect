from utils import *
from errors import *
import inspect
import importlib
import requests


class Code:
    def __init__(self, Name: str, Author: str, Type: str, Inputs: list, Outputs, Code: list):
        # Save to self
        self.name = filter(Name)
        self.author = filter(Author)
        self.type = '.py'
        self.inputs = filter(Inputs)
        self.outputs = filter(Outputs)
        self.code = Code

        assert self.name, 'Arguments should all have values'
        assert self.author, 'Arguments should all have values'
        assert self.type, 'Arguments should all have values'
        assert self.code, 'Arguments should all have values'
    
    def repr(self):
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

        return lines

    def save_as_code(self, save_file = "default.codeconnect"):
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
        with open(save_file, 'a') as openfile:
            openfile.write('\n' + '\n'.join(lines))

    def save_as_func(Code, save_file):
        define = f"def {Code.name}({' ,'.join(Code.inputs)}):"
        lines = [define] + ["    " + line for line in Code.code]

        with open(save_file, 'a') as file:
            file.writelines([line + "\n" for line in lines])
    
    def get_as_func(Code):
        define = f"def {Code.name}({' ,'.join(Code.inputs)}):"
        lines = [define + "\n"] + ["    " + line + "\n" for line in Code.code]

        open('func_dump.py', 'w').writelines(lines)
        
        func = getattr(importlib.import_module('func_dump'), Code.name)
        return func

    @staticmethod
    def load_from_func(func):
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
    def load_from_file(Name, Author, read_file):
        trimmed_lines = []
        data = [Name] + Author.split()
    
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
            
                if curr_name == Name and curr_id == Author:
                    if line.rstrip():
                        trimmed_lines.append(line.rstrip())
                        success = True
            if not success:
        	    raise ItemNotFoundError(f'Item "{Name}" with Author "{Author}", was not found')

        curr_line = ''
        inputs = []
        outputs = []
        code_lines = []
        for line in trimmed_lines:
            if line == 'INPUTS:':
                curr_line = 'inputs'
                continue
            elif line == 'RETURNS:':
                curr_line = 'outputs'
                continue
            elif line == 'CODE:':
                curr_line = 'code'
                continue
            
            if curr_line == 'inputs':
                inputs.append(line)
                continue
            elif curr_line == 'outputs':
                outputs.append(line)
                continue
            elif curr_line == 'code':
                code_lines.append(line[1:])
                continue

        author = Author
        print(author)
        code = Code(Name, author, '.py', inputs, outputs, code_lines)
        return code

    @staticmethod
    def load_from_lines(lines):
        trimmed_lines = []
        Name = ""
        author = ''
        for line in lines:
            if line.rstrip():
                if line[0] == '[':
                    Name = line[1:line.find(']')]
                    continue
                trimmed_lines.append(line.rstrip())
                if line.startswith('id'):
                    author = line.split('=')[-1].split()[0]

        curr_line = ''
        inputs = []
        outputs = []
        code_lines = []
        for line in trimmed_lines:
            if line == 'INPUTS:':
                curr_line = 'inputs'
                continue
            elif line == 'RETURNS:':
                curr_line = 'outputs'
                continue
            elif line == 'CODE:':
                curr_line = 'code'
                continue
            
            if curr_line == 'inputs':
                inputs.append(line)
                continue
            elif curr_line == 'outputs':
                outputs.append(line)
                continue
            elif curr_line == 'code':
                code_lines.append(line[1:])
                continue
        
        code = Code(Name, author, '.py', inputs, outputs, code_lines)
        return code

    @staticmethod
    def load_from_server(name, author, serverip):
        response = request.get(serverip + f'/func/{name}/{author}')
        response.raise_for_status()
        try:
            code = load_from_lines(list(responce.json()))
        except Exception as e:
            print("Invalid Response From Server:", response)
            return False
        return code


if __name__ == '__main__':
    pass
