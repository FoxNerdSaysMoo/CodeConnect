import read

# Print out or return code to prevent malicious functions
def inspect(Name: str, Id: str, Filename: str, Return = False):
    info = read.get_info(Name, Id, Filename)
    if Return:
        return info
    else:
        for line in info:
            print(line)
        
inspect("test1", "000000", "default.codeconnect")