# Tutorium Programmieren (Prof. Dr. Ralf Gerlich) - Aufgabenblatt 4
**Hinweis**: Die Lösung dieser Aufgabe wird in den folgenden Aufgabenblättern erweitert.

Definieren Sie eine Klasse `Person` mit einem geeigneten Konstruktor, die die folgenden Anforderungen erfüllt:

* Eine Person soll einen Nach- und Vornamen sowie ein Geburtsdatum haben.
* Implementieren Sie eine Methode `__str__`, die einen String mit einer gefälligen Darstellung mit Name, Vorname und Geburtsdatum zurückliefert.
* Implementieren Sie eine Methode `__repr__` ohne Parameter, die die Methode `__str__` aufruft und deren Rückgabewert zurückgibt. (Diese dient dazu, dass das Objekt auch in JupyterHub "schön" ausgegeben wird).
* Implementieren Sie eine Methode `alter`, die das Alter der Person in ganzen Jahren zurückgibt. Eine Person, die am 17. Mai 2005 Geburtstag hat, ist am 16. Mai 2025 also noch 19 Jahre alt.
* Implementieren Sie eine Methode `nächster_geburtstag`, die das Datum zurückliefert, an dem die Person zum nächsten Mal Geburtstag hat.

Verwenden Sie für die Darstellung des Datums die [Klasse `date` aus der `datetime`-Bibliothek](https://docs.python.org/3/library/datetime.html#datetime.date).

Testen Sie Ihre Klasse.

**Hinweise**:
- Um das heutige Datum zu ermitteln, können Sie die [Funktion `date.today()` aus der `datetime`-Bibliothek](https://docs.python.org/3/library/datetime.html#datetime.date.today) verwenden.
- `date`-Objekte können direkt per Vergleichsoperatoren `<`,  `<=`,  `>=` und `>` sowie `==` und `!=` miteinander verglichen werden.
- Es gibt keine Funktion in der Standardbibliothek, mit der Sie die Differenz zweier `datetime`-Objekte in ganzen Jahren bestimmen können. Sie müssen die Felder der `datetime`-Objekte selbst verwenden.
```
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

```