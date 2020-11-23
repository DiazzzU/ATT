class Session:
    id = 0
    name = ""

    instructorID = 0

    def __init__(self, id, name, course, instructorID):
        self.course = course
        self.instructorID = instructorID
        self.id = id
        self.name = name
        self.type = 0
        self.groups = []

        if "lab" in self.name:
            self.type = 2
        elif "tut" in self.name:
            self.type = 1
        elif "lec" in self.name:
            self.type = 0
        else:
            self.type = 4

    def addGroup(self, A):
        self.groups.append(A)

    def addGroups(self, groups):
        for x in groups:
            if x not in self.groups:
                self.groups.append(x)