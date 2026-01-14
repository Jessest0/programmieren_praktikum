import datetime
import os

class Name:
    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

    def __str__(self):
        return f"{self.vorname} {self.name}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Name):
            return False
        return self.name == other.name and self.vorname == other.vorname

    def __hash__(self):
        return hash((self.name, self.vorname))


class Person:
    def __init__(self, name: Name, birth):
        self.name = name
        if isinstance(birth, str):
            self.birth = datetime.datetime.strptime(birth, "%d%m%Y").date()
        else:
            self.birth = birth

    def __str__(self):
        return f'{self.name} {self.birth}'

    def __repr__(self):
        return self.__str__()

    def alter(self):
        heute = datetime.date.today()
        jahre = heute.year - self.birth.year
        if (heute.month, heute.day) < (self.birth.month, self.birth.day):
            jahre -= 1
        return jahre

    def naechster_geburtstag(self):
        heute = datetime.date.today()
        jahre = heute.year
        if (heute.month, heute.day) > (self.birth.month, self.birth.day):
            jahre += 1
        return datetime.date(jahre, self.birth.month, self.birth.day)


class Personendatenbank:
    def __init__(self, personen=None):
        if personen is None:
            personen = {}
        self.personen = personen   # Dictionary: Name → Person

    def __str__(self):
        return "\n".join(str(person) for person in self.personen.values())

    def leeren(self):
        self.personen = {}

    def einfuegen(self, person):
        self.personen[person.name] = person

    def findePerson(self, vorname, nachname):
        suchname = Name(nachname, vorname)
        return self.personen.get(suchname, None)

    def entfernen(self, vorname, nachname):
        suchname = Name(nachname, vorname)
        if suchname in self.personen:
            del self.personen[suchname]

    def speichern(self, dateiname):
        with open(dateiname, "w", encoding="utf-8") as f:
            for person in self.personen.values():
                zeile = f"{person.name.vorname},{person.name.name},{person.birth.strftime('%d%m%Y')}\n"
                f.write(zeile)


def laden(dateiname):
    datenbank = Personendatenbank()

    if os.path.exists(dateiname):
        with open(dateiname, "r", encoding="utf-8") as datei:
            for line in datei:
                line = line.strip().replace("\ufeff", "").replace("\r", "").replace('"', '')
                teile = line.split(",")
                if len(teile) != 3:
                    print(f"⚠️ Ungültige Zeile übersprungen: {line}")
                    continue

                vorname, nachname, birth = [teil.strip() for teil in teile]

                try:
                    name = Name(nachname, vorname)
                    person = Person(name, birth)
                    datenbank.einfuegen(person)
                except ValueError as e:
                    print(f" Fehler beim Verarbeiten von '{line}': {e}")
    else:
        print(f" Datei '{dateiname}' nicht gefunden. Leere Datenbank wird erstellt.")

    return datenbank


def hauptmenue():
    dateipfad = "database.csv"
    datenbank = laden(dateipfad)

    while True:
        print("\n--- Personendatenbank ---")
        print("1: Person hinzufügen")
        print("2: Person suchen")
        print("3: Person entfernen")
        print("4: Alle Personen anzeigen")
        print("5: Datenbank leeren")
        print("6: Datenbank speichern")
        print("7: Datenbank erneut laden")
        print("0: Beenden")

        auswahl = input("Bitte wählen: ")

        if auswahl == "1":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            geburt = input("Geburtsdatum (DDMMYYYY): ")

            name = Name(nachname, vorname)
            person = Person(name, geburt)
            datenbank.einfuegen(person)
            print("Person hinzugefügt.")

        elif auswahl == "2":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            person = datenbank.findePerson(vorname, nachname)
            if person:
                print(f" Gefunden: {person.name}")
                print(f" Geburtsdatum: {person.birth}")
                print(f" Alter: {person.alter()} Jahre")
            else:
                print(" Person nicht gefunden.")

        elif auswahl == "3":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            datenbank.entfernen(vorname, nachname)
            print(" Person entfernt (falls vorhanden).")

        elif auswahl == "4":
            print("\n Personenliste:")
            print(datenbank)

        elif auswahl == "5":
            datenbank.leeren()
            print(" Datenbank geleert.")

        elif auswahl == "6":
            datenbank.speichern(dateipfad)
            print(f" Datenbank gespeichert in '{dateipfad}'.")

        elif auswahl == "7":
            datenbank = laden(dateipfad)
            print(f" Datenbank erneut geladen aus '{dateipfad}'.")

        elif auswahl == "0":
            print(" Programm beendet.")
            break

        else:
            print(" Ungültige Eingabe. Bitte erneut versuchen.")


hauptmenue()