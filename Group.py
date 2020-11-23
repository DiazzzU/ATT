class Group:
    gNumber = ""
    id = 0

    def __init__(self, id, gNumber):
        self.id = id
        self.gNumber = gNumber
        self.courses = []
        self.sessions = []

    def addCourse(self, A):
        self.courses.append(A)

    def addSession(self, A):
        self.sessions.append(A)


