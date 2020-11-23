from Group import Group
from Instructor import Instructor
from Course import Course
from Session import Session
from Room import Room
import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
timeSlots = ["9:00", "10:40", "12:40", "14:20", "16:00", "17:40", "19:20"]
timeTable = []

instructors = []
courses = []
sessions = []
rooms = []
allGroups = []
sessionIDS = 0
instructorIDS = 0
courseIDS = 0

def findInstructor(name):
    for x in instructors:
        if x.name == name:
            return x
    return None

def findCourse(name, year):
    for x in courses[year]:
        if x.name == name:
            return x
    return None

def isOK(day, time, session, room):
    for x in timeTable[day][time]:
        a = x[0]
        b = x[1]
        if a.instructorID == session.instructorID:
            return False
        if len(list(set(a.groups) & set(session.groups))) > 0:
            return False
        if b.room == room.room:
            return False
    return True

f = open("1year.csv", "r")
s = f.readline()
s = f.readline()

courses.append([])
while len(s) > 0:
    s = s.split(', ')
    s[len(s)-1] = s[len(s)-1][:-1]
    courseName = s[0][0:s[0].find('{')-1]
    sessionName = s[0][s[0].find('{') + 1:s[0].find('}')]
    groups = s[2].split('/')

    for x in groups:
        if x not in allGroups:
            allGroups.append(x)

    A = findInstructor(s[1])
    if A == None:
        A = Instructor(instructorIDS, s[1])
        instructorIDS = instructorIDS + 1
        instructors.append(A)

    C = findCourse(courseName, 0)
    if C == None:
        C = Course(courseIDS, courseName, "core")
        courseIDS = courseIDS + 1
        courses[0].append(C)

    session = Session(sessionIDS, sessionName, C, A.id)
    sessionIDS = sessionIDS + 1

    A.addSession(session)
    C.addSession(session)

    C.addGroups(groups)
    session.addGroups(groups)

    sessions.append(session)

    s = f.readline()

f.close()

courses.append([])

f = open("2year.csv", "r")
s = f.readline()
s = f.readline()

courses.append([])
while len(s) > 0:
    s = s.split(', ')
    s[len(s)-1] = s[len(s)-1][:-1]
    courseName = s[0][0:s[0].find('{')-1]
    sessionName = s[0][s[0].find('{') + 1:s[0].find('}')]
    groups = s[2].split('/')

    for x in groups:
        if x not in allGroups:
            allGroups.append(x)

    A = findInstructor(s[1])
    if A == None:
        A = Instructor(instructorIDS, s[1])
        instructorIDS = instructorIDS + 1
        instructors.append(A)

    C = findCourse(courseName, 1)
    if C == None:
        C = Course(courseIDS, courseName, "core")
        courseIDS = courseIDS + 1
        courses[1].append(C)

    session = Session(sessionIDS, sessionName, C, A.id)
    sessionIDS = sessionIDS + 1

    A.addSession(session)
    C.addSession(session)

    C.addGroups(groups)
    session.addGroups(groups)

    sessions.append(session)

    s = f.readline()

f.close()

courses.append([])
courses.append([])

A = Room("107", 0)
rooms.append(A)
A = Room("108", 0)
rooms.append(A)
A = Room("106", 1)
rooms.append(A)
A = Room("105", 1)
rooms.append(A)
for i in range (15):
    A = Room(str(i + 200), 2)
    rooms.append(A)

for i in range(5):
    timeTable.append([])

for x in timeTable:
    for i in range(len(timeSlots)):
        x.append([])

for i in range(0, 4, 1):
    for x in courses[i]:
        x.makeStructure()

years = [0, 1]

while len(years)>0:
    random.shuffle(years)
    year = years[0]
    random.shuffle(courses[year])
    if len(courses[year]) == 0:
        continue
    course = courses[year][0]
    for x in courses[year]:
        if x.structure == 2 or x.structure == 1:
            course = x
            break
    if course.structure == 2:
        t = -1
        d = -1
        r = -1
        for time in range(0, len(timeSlots) - 1):
            for day in range(0, 5):
                for room in rooms:
                    if room.isOK(course.findLec()) and room.isOK(course.findTut()) and isOK(day, time, course.findLec(), room) and isOK(day, time + 1, course.findTut(), room):
                        t = time
                        d = day
                        r = room
                        break
                if t != -1:
                    break
            if t != -1:
                break
        timeTable[d][t].append([course.findLec(), r])
        timeTable[d][t + 1].append([course.findTut(), r])

        for x in course.sessions:
            t1 = -1
            d1 = -1
            r1 = -1
            if x.type != 2:
                continue
            for day in range(d, 5):
                for time in range(3, len(timeSlots)):
                    for room in rooms:
                        if room.isOK(x) and isOK(day, time, x, room):
                            t1 = time
                            d1 = day
                            r1 = room
                    if t1 != -1:
                            break
                if t1 != -1:
                    break

            if t1 == -1:
                for day in range(0, 5):
                    for time in range(3, len(timeSlots)):
                        for room in rooms:
                            if room.isOK(x) and isOK(day, time, x, room):
                                t1 = time
                                d1 = day
                                r1 = room
                        if t1 != -1:
                            break
                    if t1 != -1:
                        break


            timeTable[d1][t1].append([x, r1])

    if course.structure == 1:
        t = -1
        d = -1
        r = -1
        for time in range(0, len(timeSlots) - 1):
            for day in range(0, 5):
                for room in rooms:
                    if room.isOK(course.findLec()) and isOK(day, time, course.findLec(), room):
                        t = time
                        d = day
                        r = room
                        break
                if t != -1:
                    break
            if t != -1:
                break
        timeTable[d][t].append([course.findLec(), r])

        for x in course.sessions:
            t1 = -1
            d1 = -1
            r1 = -1
            if x.type != 2:
                continue
            for day in range(d, 5):
                for time in range(3, len(timeSlots)):
                    for room in rooms:
                        if room.isOK(x) and isOK(day, time, x, room):
                            t1 = time
                            d1 = day
                            r1 = room
                    if t1 != -1:
                            break
                if t1 != -1:
                    break

            if t1 == -1:
                for day in range(0, 5):
                    for time in range(3, len(timeSlots)):
                        for room in rooms:
                            if room.isOK(x) and isOK(day, time, x, room):
                                t1 = time
                                d1 = day
                                r1 = room
                        if t1 != -1:
                            break
                    if t1 != -1:
                        break

            timeTable[d1][t1].append([x, r1])

    if course.structure == 0:
        t = -1
        d = -1
        r = -1
        for time in range(0, len(timeSlots) - 1):
            for day in range(0, 5):
                for room in rooms:
                    if room.isOK(course.findLec()) and isOK(day, time, course.findLec(), room):
                        t = time
                        d = day
                        r = room
                        break
                if t != -1:
                    break
            if t != -1:
                break
        timeTable[d][t].append([course.findLec(), r])

    if course.structure == 3:
        for x in course.sessions:
            t1 = -1
            d1 = -1
            r1 = -1
            for day in range(0, 5):
                for time in range(0, len(timeSlots)):
                    for room in rooms:
                        if room.isOK(x) and isOK(day, time, x, room):
                            t1 = time
                            d1 = day
                            r1 = room
                    if t1 != -1:
                        break
                if t1 != -1:
                    break

            timeTable[d1][t1].append([x, r1])

    courses[year].remove(course)
    if len(courses[year]) == 0:
        years.remove(year)

f = open("timetable.csv", "w")

s = "Time/Groups, "
for x in allGroups:
    s = s + x + ', '

s = s[:-2]

f.write(s + '\n')

for day in range(0, 5):
    cnt = 0
    for x in timeTable[day]:
        arr = [timeSlots[cnt], " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        cnt = cnt + 1
        for y in x:
            for g in y[0].groups:
                gg = (20-int(g[1:3])) * 6
                gg = gg + int(g[len(g) - 2: ])
                arr[gg] = y[0].course.name + " (" + y[0].name + ") " + y[1].room
        s = ""
        for x in arr:
            s = s    + x + ', '
        f.write(s + '\n')
    arr = ["------------", "---------------", "--------------", "---------------", "---------------", "--------------", "------------", "---------------", "--------------", "---------------", "---------------", "--------------"]
    s = ""
    for x in arr:
        s = s + x + ', '
    f.write(s + '\n')
f.close()


