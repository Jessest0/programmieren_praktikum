import datetime

class personen:
    def __init__(self, fName ,lName, birth):
        self.fName = fName
        self.lName = lName
        self.birth = birth


    def __str__(self):
        print(self.fName, self.lName, self.birth)

    def __repr__(self):
        return self.__str__()

    def alter(self):
        heute = datetime.date.today()
        jahre = heute.year - self.birth.year

        if (heute.month, heute.day) < (self.birth.month, self.birth.day):
            jahre-= 1

        print(jahre)
        return jahre

    def naechster_geburtstag(self):
        heute = datetime.date.today()
        jahre = heute.year

        if (heute.month, heute.day) > (self.birth.month, self.birth.day):
            jahre += 1
        print(datetime.date(jahre, self.birth.month, self.birth.day))
        return datetime.date(jahre, self.birth.month, self.birth.day)



geburtsdatum = datetime.date(2024,11,6) #Das alter muss als date varible ausgeggeben sein und nicht als int
x = personen('Arjun', 'Boehler', geburtsdatum)
x.naechster_geburtstag()

