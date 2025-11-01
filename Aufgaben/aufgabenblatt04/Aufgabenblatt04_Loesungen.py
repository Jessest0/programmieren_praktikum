class Person:
    def __init__(self, fName, lName, birth):
        def __str__(self):
            self.fName = fName
            self.lName = lName
            self.birth = birth

        def __str__(self, fName, lName, birth):
            self.fName = str(fName)
            self.lName = str(lName)
            self.birth = str(birth)

x = Person("Jesse", "Strunsky", 2005)
print(x.__str__())
