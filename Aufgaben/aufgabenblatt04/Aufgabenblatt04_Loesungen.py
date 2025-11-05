import datetime

class Person:
    def __init__(self, fName, lName, birth):
        self.fName = fName
        self.lName = lName
        self.birth = birth

    def __str__(self):
        return f'{self.fName} {self.lName} {self.birth}'

    def __repr__(self):
        return self.__str__()

    def alter(self):
        heute = datetime.date.today()
        jahre = heute.year - self.birth.year

        if (heute.month, heute.day) < (self.birth.month, self.birth.day):
            jahre-= 1

        return jahre

    def naechster_geburtstag(self):
        heute = datetime.date.today()
        jahre = heute.year

        if (heute.month, heute.day) > (self.birth.month, self.birth.day):
            jahre += 1

        return datetime.date(jahre, self.birth.month, self.birth.day)

geburtsdatum = datetime.date(2005, 7, 13)
x = Person('Jesse', 'Strunsky', geburtsdatum)

print(x)
print( x.naechster_geburtstag())
