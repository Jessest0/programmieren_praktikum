import datetime
# -----------------------------------------------
# Klasse Name (Aufgabe 7)
# Speichert Vor- und Nachnamen in einem eigenen Objekt.
# Diese Klasse brauchen wir später als Schlüssel im Dictionary.
# -----------------------------------------------
class Name:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    def __str__(self):
        return f"{self.vorname} {self.nachname}"

    # Damit wir Name-Objekte vergleichen können
    def __eq__(self, other):
        return (self.vorname, self.nachname) == (other.vorname, other.nachname)

    # Damit wir Name-Objekte als Schlüssel in Dictionaries benutzen können
    def __hash__(self):
        return hash((self.vorname, self.nachname))


# -----------------------------------------------
# Klasse Person (Aufgabe 7)
# Jetzt hat Person nicht mehr fName + lName,
# sondern ein einziges Feld "name", das ein Name-Objekt ist.
# -----------------------------------------------
class Person:
    def __init__(self, name, birth):
        # name MUSS ein Name-Objekt sein
        self.name = name

        # Geburtsdatum wie in den vorherigen Aufgaben verarbeiten
        if isinstance(birth, str):
            self.birth = datetime.datetime.strptime(birth, "%Y%m%d").date()
        else:
            self.birth = birth

    def __str__(self):
        return f"{self.name} – {self.birth}"

    # Alter berechnen wie gehabt
    def alter(self):
        heute = datetime.date.today()
        jahre = heute.year - self.birth.year
        if (heute.month, heute.day) < (self.birth.month, self.birth.day):
            jahre -= 1
        return jahre

    # Nächsten Geburtstag bestimmen
    def naechster_geburtstag(self):
        heute = datetime.date.today()
        jahr = heute.year
        if (heute.month, heute.day) > (self.birth.month, self.birth.day):
            jahr += 1
        return datetime.date(jahr, self.birth.month, self.birth.day)


# -----------------------------------------------
# Personendatenbank (Aufgabe 7)
# Jetzt nicht mehr als Liste, sondern Dictionary:
#   Schlüssel = Name-Objekt
#   Wert     = Person-Objekt
# -----------------------------------------------
class Personendatenbank:
    def __init__(self, personen_dict=None):
        # Falls nichts übergeben wurde, ein leeres Dictionary
        if personen_dict is None:
            personen_dict = {}
        self.personen = personen_dict

    def __str__(self):
        if not self.personen:
            return "Datenbank ist leer"
        # Wir geben die Personen einfach untereinander aus
        return "\n".join(str(p) for p in self.personen.values())

    # Alles löschen
    def leeren(self):
        self.personen = {}

    # Neue Person einfügen (wird über Namen als Key gespeichert)
    def einfuegen(self, person):
        self.personen[person.name] = person

    # Person anhand von Vor- und Nachname suchen
    def findePerson(self, vorname, nachname):
        key = Name(vorname, nachname)
        return self.personen.get(key, None)

    # Person entfernen
    def entfernen(self, vorname, nachname):
        key = Name(vorname, nachname)
        if key in self.personen:
            del self.personen[key]

    # Datenbank speichern (für Aufgabe 6 adaptiert)
    def speichern(self):
        with open("personen.txt", "w", encoding="utf-8") as f:
            for p in self.personen.values():
                geb = p.birth.strftime("%Y%m%d")
                f.write(f"{p.name.vorname},{p.name.nachname},{geb}\n")


# -----------------------------------------------
# Hilfsfunktion zum Laden aus Datei
# Baut wieder Name- und Person-Objekte zusammen.
# -----------------------------------------------
def laden():
    personen = {}
    try:
        with open("personen.txt", "r", encoding="utf-8") as f:
            for zeile in f:
                teile = zeile.strip().split(",")
                if len(teile) == 3:
                    vorname, nachname, geb = teile
                    name = Name(vorname, nachname)
                    person = Person(name, geb)
                    personen[name] = person
        return Personendatenbank(personen)
    except FileNotFoundError:
        # Falls Datei noch nicht existiert
        return Personendatenbank()


# -----------------------------------------------
# Ab hier läuft das eigentliche Programm
# -----------------------------------------------
print("Lade Personendatenbank…")
z = laden()
print("Datenbank geladen!")

# Beispielpersonen (wie in deinen vorherigen Aufgaben)
walter = Person(Name("Walter", "White"), "19580907")
jesse = Person(Name("Jesse", "Pinkman"), "19840924")
alp = Person(Name("Alp", "Ham"), "20061127")

# Falls Datenbank leer ist → Startpersonen hinzufügen
if not z.personen:
    print("Füge Startpersonen hinzu…")
    z.einfuegen(walter)
    z.einfuegen(jesse)

# -----------------------------------------------
# Einfaches Menü wie in den vorherigen Aufgaben
# -----------------------------------------------
while True:
    print("\nPersonendatenbank – Menü:")
    print("1 - Alle Personen anzeigen")
    print("2 - Alp hinzufügen")
    print("3 - Walter suchen")
    print("4 - Jesse entfernen")
    print("5 - Datenbank leeren")
    print("6 - Datenbank speichern")
    print("7 - Datenbank neu laden")
    print("0 - Programm beenden")

    auswahl = input("Auswahl: ")

    if auswahl == "0":
        print("Programm beendet.")
        break

    elif auswahl == "1":
        print(z)

    elif auswahl == "2":
        z.einfuegen(alp)
        print("Alp wurde hinzugefügt.")

    elif auswahl == "3":
        p = z.findePerson("Walter", "White")
        print(p if p else "Walter konnte nicht gefunden werden.")

    elif auswahl == "4":
        z.entfernen("Jesse", "Pinkman")
        print("Jesse wurde entfernt.")

    elif auswahl == "5":
        z.leeren()
        print("Datenbank geleert.")

    elif auswahl == "6":
        z.speichern()
        print("Datenbank gespeichert.")

    elif auswahl == "7":
        z = laden()
        print("Datenbank neu geladen.")