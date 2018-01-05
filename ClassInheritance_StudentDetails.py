class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = float(sum(self.scores) / len(self.scores))

        if avg >= 90.0 and avg <= 100.0:
            return 'O'
        elif avg >= 80.0 and avg < 90.0:
            return 'E'
        elif avg >= 70.0 and avg < 80.0:
            return  'A'
        elif avg >= 55.0 and avg < 70.0:
            return 'P'
        elif avg >= 40.0 and avg < 55.0:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())