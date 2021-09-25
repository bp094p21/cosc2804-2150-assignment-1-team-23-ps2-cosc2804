class Logbook:
    logs: list = []
    owner: str = None

    def __init__(self, owner):
        self.owner = owner
