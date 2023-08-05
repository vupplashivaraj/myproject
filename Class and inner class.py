class Student:
    def __init__(self, name, rolno):
        self.name = name
        self.rolno = rolno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rolno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student('Shivaraj', 10)
s2 = Student('Roja', 12)
lap1 = s1.lap
lap2 = s2.lap

s1.show()

