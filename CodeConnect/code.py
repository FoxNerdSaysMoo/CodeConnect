from utils import getnewid


class Code:
    
    def __init__(self, Name: str, Type: str, Inputs: list, Outputs:list, Code: list):
        # Save to self
        self.name = Name
        self.type = Type
        self.inputs = Inputs
        self.outputs = Outputs
        self.code = Code
    
    def save(self, save_file = "default.codeconnect"):
        
        # Define values to put in file
        header = "[" + self.name + "]"
        type_statement = "TYPE = " + self.type
        id_statement = "id = " + getnewid(self.name, save_file) + " " + self.name
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
                
# Testing code [delete when done]
test = Code("test2", ".py", [], [], ["print('I just got executed!')"])
test.save()

