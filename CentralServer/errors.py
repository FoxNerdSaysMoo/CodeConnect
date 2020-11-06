class ItemNotFoundError(Exception):
    def __init__(item, instances):
        super().__init__(f"Item '{item}' had {instances} instances found")

class InvalidIndentsError(Exception):
    def __init__():
        super.__init__('Invalid Indents')
