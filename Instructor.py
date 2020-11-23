class Instructor:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.sessions = []

    def addSession(self, A):
        self.sessions.append(A)