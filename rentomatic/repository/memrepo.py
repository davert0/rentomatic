from rentomatic.domain.room import Room

class MemRepo:
    def __init__(self, rooms) -> None:
        self.rooms = rooms

    def list(self):
        return [Room.from_dict(room_dict) for room_dict in self.rooms]