import datetime

class Person:
    def __init__(self, fName, lName, birth):
        self.fName = fName
        self.lName = lName
        self.birth = birth
        if isinstance(birth, str):
            self.birth = datetime.datetime.strptime(birth, "%Y%m%d").date()
        else:
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

class Personendatenbank:
    def __init__(self, personenliste=[]):
        self.personenliste = personenliste

    def __str__(self):
        return "\n".join(str(person) for person in self.personenliste)

    def leeren(self):
        self.personenliste = []

    def einfuegen(self, person):
        self.personenliste = self.personenliste + [person]

    def findePerson(self, fname, lname):
        for person in self.personenliste:
            if person.fName == fname and person.lName == lname:
                return person
        return None


x = Person("Jesse", "Strunsky", "20050713")
y = Person("Nick","Strunsky","20070812")

z = Personendatenbank([x])
print(z)
z.einfuegen(y)
print(z)
z.findePerson("Jesse", "Strunsky")



