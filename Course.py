class Course:

    id = 0
    name = ""
    type = ""

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        self.sessions = []
        self.structure = 0
        self.groups = []

    def addSession(self, A):
        self.sessions.append(A)

    def addGroup(self, A):
        self.groups.append(A)

    def addGroups(self, groups):
        for x in self.groups:
            if x not in self.groups:
                self.groups.append(x)

    def findLec(self):
        for x in self.sessions:
            if x.type == 0:
                return x

    def findTut(self):
        for x in self.sessions:
            if x.type == 1:
                return x

    def makeStructure(self):
        a = 0
        b = 0
        c = 0
        for x in self.sessions:
            if x.type == 0:
                a = 1
            if x.type == 1:
                b = 1
            if x.type == 2:
                c = 1
        if a + b + c == 3:
            self.structure = 2
        elif a == 1 and b == 0 and c == 1:
            self.structure = 1
        elif a == 1 and b == 0 and c == 0:
            self.structure = 0
        else:
            self.structure = 3
