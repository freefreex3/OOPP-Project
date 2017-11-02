import datetime
class Student:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        self.__mark = 0.0
        now = datetime.datetime.now()
        self.__enrolmentDate = str(now.day) + "-" +str(now.month) +"-"+ str(now.year)
    def get_enrolment_date(self):
        return self.__enrolmentDate
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def get_mark(self):
        return self.__mark
    def set_name(self, name):
        self.__name = name
    def set_gender(self, gender):
        self.__gender = gender
    def set_mark(self, mark):
        self.__mark = mark
    def __str__(self):
        s ='Name : {}, Gender : {} and Marks : {} and enrolment: {}'.format(self.get_name(), self.get_gender(), self.get_mark(),self.get_enrolment_date())
        return s

s = Student("Ms Khoo", 'F')
print("=== First view ===")
print(s)
s.set_mark(100)
print("=== Second view ===")
print(s)
