class Student:
    def __str__(self):
        return "Student"

    def printStudent(self):
        print(self.__str__())


class GranduteStudent(Student):
    def __str__(self):
        return "Graduate Student"


a = Student()
b = GranduteStudent()
a.printStudent()
b.printStudent()
