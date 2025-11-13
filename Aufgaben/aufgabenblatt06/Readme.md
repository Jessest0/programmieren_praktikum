# Tutorium Programmieren (Prof. Dr. Ralf Gerlich) - Aufgabenblatt 6

Erweitern Sie das Modul `personendatenbank` aus dem vorigen Aufgabenblatt wie folgt:
* Implementieren Sie eine Funktion `laden(datei)`, die ein Dateiobjekt `datei` erhält, daraus eine Liste von Personenobjekten einliest und ein Objekt der Klasse `Personendatenbank` zurückliefert, die die Personenobjekte aus der Datei enthält.
* Implementieren Sie eine Methode `speichern(datei)` in der Klasse `Personendatenbank`, die ein Dateiobjekt `datei` erhält und alle Personen aus der Personendatenbank so in der angegebenen Datei abspeichert, dass die Datei mit der obigen Funktion `laden` wieder eingelesen werden kann.

Erweitern Sie Ihr Hauptprogramm so, dass zu Beginn eine Personendatenbank aus einer vorgegebenen Datei geladen und per Menübefehl die Personendatenbank in derselben Datei abgespeichert werden kann. Wenn die Datei zu Beginn nicht existiert, soll eine leere Personendatenbank erstellt werden.

**Hinweise**:
* Implementieren Sie Ihre Lösung in PyCharm (auf Basis der Lösung des vorigen Aufgabenblatts) und reichen Sie eine ZIP-Datei mit Ihrem Projektverzeichnis in FELIX ein.
* Die Lösung dieser Aufgabe wird in den folgenden Aufgabenblättern erweitert.
* Wenn Sie wollen, können Sie die Möglichkeiten des Moduls [`csv`](https://docs.python.org/3/library/csv.html) aus der Python-Standardbibliothek verwenden, um diese Aufgabe zu lösen.
* Um zu prüfen, ob die Datei existiert, können Sie die Funktion [`exists` aus dem Modul `os.path`](https://docs.python.org/3/library/os.path.html#os.path.exists) verwenden.

Testen Sie das Programm.
```
import datetime
import os

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
            jahre -= 1
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

    def entfernen(self, fname, lname):
        person = self.findePerson(fname, lname)
        if person:
            self.personenliste.remove(person)

    def speichern(self, dateiname):
        with open(dateiname, "w", encoding="utf-8") as f:
            for person in self.personenliste:
                zeile = f"{person.fName},{person.lName},{person.birth.strftime('%Y%m%d')}\n"
                f.write(zeile)

# Globale Funktion zum Laden
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
                fName, lName, birth = [teil.strip() for teil in teile]
                try:
                    person = Person(fName, lName, birth)
                    datenbank.einfuegen(person)
                except ValueError as e:
                    print(f"⚠️ Fehler beim Verarbeiten von '{line}': {e}")
    else:
        print(f"📁 Datei '{dateiname}' nicht gefunden. Leere Datenbank wird erstellt.")
    return datenbank

# Hauptmenü
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
            geburt = input("Geburtsdatum (YYYYMMDD): ")
            person = Person(vorname, nachname, geburt)
            datenbank.einfuegen(person)
            print("Person hinzugefügt.")

        elif auswahl == "2":
            vorname = input("Vorname: ")
            nachname = input("Nachname: ")
            person = datenbank.findePerson(vorname, nachname)
            if person:
                print(f" Gefunden: {person.fName} {person.lName}")
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
            print("🧹 Datenbank geleert.")

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

# Start
hauptmenue()

```