# Dvir Sadon
class Person:
    def __init__(self, name='dvir', age=16):
        self.__name = name
        self.__age = age

    def say(self):
        print'wuddup :)'

    def __str__(self):
        return self.__name + ' is ' + str(self.__age) + ' years old '

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def setname(self, name):
        self.__name = name

    def setage(self, age):
        self.__age = age


class Teacher(Person):
    def __init__(self, name='daniel', age=30, salary=50):
        Person.__init__(self, name, age)
        self.__salary = salary

    def say(self):
        print 'Good morning!'

    def __str__(self):
        return self.__name + ' is ' + str(self.__age)+' years old, hourly income is ' + str(self.__salary)


class Student(Person):
    def __init__(self, name='ete', age=16, grade=85):
        super(self.__class__, self).__init__(name, age)
        self.__grade = grade

    def getgrade(self):
        return self.__grade

    def setgrade(self, grade):
        self.__grade = grade


class BigThing():
    pass
teacher1 = Teacher()
teacher1.say()