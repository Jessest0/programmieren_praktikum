# Tutorium Programmieren (Prof. Dr. Ralf Gerlich) - Aufgabenblatt 5

## Aufgabe 1: Personendatenbank

**Hinweis**: Die Lösung dieser Aufgabe wird in den folgenden Aufgabenblättern erweitert.

Definieren Sie eine Klasse `Personendatenbank` mit einem geeigneten Konstruktor, die die folgenden Anforderungen erfüllt:

* Die Personendatenbank soll eine Liste von Personen enthalten, wobei eine Person durch ein Objekt der Klasse `Person` aus der vorigen Aufgabe repräsentiert wird.
* Implementieren Sie die folgenden Methoden:
    - `leeren`: Leert die Liste der Personen.
    - `einfügen(person)`: Fügt das Personenobjekt `person` in die Liste der Personen ein.
    - `findePerson(name, vorname)`: Liefert das Personenobjekt aus der Datenbank, dessen Name und Vorname den Strings `name` und `vorname` entsprechen. Wenn keine solche Person existiert, soll `None` zurückgegeben werden.
    - `entfernen(name, vorname)`: Entfernt die Person mit dem angegebenen Namen und Vornamen aus der Datenbank.

Schreiben Sie in Jupyter ein Hauptprogramm, das die Verwaltung und Nutzung dieser Datenbank mit der folgenden Funktionalität erlaubt:
- Person hinzufügen
- Person suchen (nach Name und Vorname)
- Person entfernen

Bei "Person suchen" soll entweder Name, Vorname, Geburtsdatum und Alter der Person ausgegeben werden, oder eine entsprechende Meldung, wenn die Person nicht in der Datenbank enthalten ist.

Implementieren Sie eine Hauptschleife, das ein entsprechendes Menü präsentiert, nach einer Auswahl fragt und dann die entsprechende Funktionalität ausführt, mit allen erforderlichen Nachfragen bei der Nutzerin oder beim Nutzer.

Testen Sie das Programm.

```
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


```

# Aufgabe 2: Auszug aus Jupyter

#%% md
Setzen Sie ein Projekt in PyCharm auf, in dem Ihr Personaldatenbank-Programm auch außerhalb von Jupyter ausgeführt werden kann. Lagern Sie die Klassen dabei in ein Modul `personendatenbank` aus. Das Hauptprogramm soll in einem gesonderten Modul `hauptprogramm` enthalten sein.

Testen Sie, ob Ihr Programm noch korrekt funktioniert.

**Hinweis**: Erstellen Sie aus Ihrem Projektverzeichnis eine ZIP-Datei und reichen Sie diese als Lösung in FELIX ein.

.