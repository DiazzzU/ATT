class Room:
    type = ""
    room = ""
    def __init__(self, room, type):
        self.room = room
        self.type = type

    def isOK(self, session):
        if self.type == 0 and len(session.groups) >= 2:
            return True
        if self.type == 1 and len(session.groups) <= 3 and len(session.groups) >= 2:
            return True
        if self.type == 2 and len(session.groups) == 1:
            return True
        return False
