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

    def entfernen(self,fname, lname):
        person = self.findePerson(fname, lname)
        if person:
            self.personenliste.remove(person)

    def laden(self,datei):
        datei = open(datei, "r", encoding="utf-8")
        for line in datei:
            print(line)
        datei.close()

    def speichern(selfself, datei):
        datei = open(datei, "r", encoding="utf-8")


def hauptmenue():
    datenbank = Personendatenbank()

    while True:
        print("\n--- Personendatenbank ---")
        print("1: Person hinzufügen")
        print("2: Person suchen")
        print("3: Person entfernen")
        print("4: Alle Personen anzeigen")
        print("5: Datenbank leeren")
        print("0: Beenden")

        auswahl = input("Bitte wählen: ")

        if auswahl == "1":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            geburt = input("Geburtsdatum (YYYYMMDD): ")
            person = Person(vorname, nachname, geburt)
            datenbank.einfuegen(person)
            print("✅ Person hinzugefügt.")

        elif auswahl == "2":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            person = datenbank.findePerson(vorname, nachname)
            if person:
                print(f"👤 Gefunden: {person.fName} {person.lName}")
                print(f"📅 Geburtsdatum: {person.birth}")
                print(f"🎂 Alter: {person.alter()} Jahre")
            else:
                print("❌ Person nicht gefunden.")

        elif auswahl == "3":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            datenbank.entfernen(vorname, nachname)
            print("🗑️ Person entfernt (falls vorhanden).")

        elif auswahl == "4":
            print("\n📋 Personenliste:")
            print(datenbank)

        elif auswahl == "5":
            datenbank.leeren()
            print("🧹 Datenbank geleert.")

        elif auswahl == "0":
            print("👋 Programm beendet.")
            break

        else:
            print("⚠️ Ungültige Eingabe. Bitte erneut versuchen.")

hauptmenue()



