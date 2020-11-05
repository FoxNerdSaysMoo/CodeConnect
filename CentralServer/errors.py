class ItemNotFoundError(Exception):
    def __init__(item, instances):
        super().__init__(f"Item '{item}' had {instances} instances found")