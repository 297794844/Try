class person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print(self):
        print(self.getname(),end=" ")
        print(self.getage())
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
class student(person):
    def __init__(self, name, age, number, university):
        super(student, self).__init__(name, age)
        self.number = number
        self.university = university
    def print(self):
        super(student, self).print()
        print(self.number)

if __name__ == "__main__":
    A = person('Tom', 13)
    B = student('Sam', 13, 1968071, 'Bristol')
    s = ['asd', 'sadsa']
    a = "asd"
    hash = {'name': 'hoho', 'age': 18}
    print("{0:-^20}".format(*s))
    print(f"Hi,I am {a}.")