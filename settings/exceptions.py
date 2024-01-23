from fastapi.responses import JSONResponse

class NotFound(Exception):
    def __init__(self, name_not_found:str):
        self.name = f"Exception! {name_not_found} not found"

class DBEmpty(Exception):
    def __init__(self):
        self.name = f"Exception! Data Base is Empty"