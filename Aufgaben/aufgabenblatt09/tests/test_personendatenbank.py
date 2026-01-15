import datetime
from Aufgabenblatt09_Loesungen import Name, Person, Personendatenbank


# ---------- Tests für Person.alter ----------
def test_alter_vor_geburtstag():
    heute = datetime.date.today()
    birth = datetime.date(heute.year - 30, heute.month, heute.day + 1 if heute.day < 28 else heute.day - 1)
    p = Person(Name("Test", "Max"), birth)
    assert p.alter() == 29


def test_alter_am_geburtstag():
    heute = datetime.date.today()
    birth = datetime.date(heute.year - 20, heute.month, heute.day)
    p = Person(Name("Test", "Max"), birth)
    assert p.alter() == 20


# ---------- Tests für Person.naechster_geburtstag ----------
def test_naechster_geburtstag_in_zukunft():
    heute = datetime.date.today()
    birth = datetime.date(1990, heute.month, heute.day + 1 if heute.day < 28 else heute.day - 1)
    p = Person(Name("Test", "Max"), birth)

    result = p.naechster_geburtstag()
    assert result.month == birth.month
    assert result.day == birth.day


def test_naechster_geburtstag_heute():
    heute = datetime.date.today()
    birth = datetime.date(1990, heute.month, heute.day)
    p = Person(Name("Test", "Max"), birth)

    assert p.naechster_geburtstag() == heute


# ---------- Tests für Personendatenbank.einfuegen ----------
def test_einfuegen():
    db = Personendatenbank()
    p = Person(Name("Doe", "John"), "01012000")
    db.einfuegen(p)

    assert db.personen[p.name] == p


# ---------- Tests für Personendatenbank.findePerson ----------
def test_finde_person_existiert():
    db = Personendatenbank()
    p = Person(Name("Doe", "John"), "01012000")
    db.einfuegen(p)

    assert db.findePerson("John", "Doe") == p


def test_finde_person_existiert_nicht():
    db = Personendatenbank()
    assert db.findePerson("Max", "Mustermann") is None


# ---------- Tests für Personendatenbank.entfernen ----------
def test_entfernen():
    db = Personendatenbank()
    p = Person(Name("Doe", "John"), "01012000")
    db.einfuegen(p)

    db.entfernen("John", "Doe")
    assert db.findePerson("John", "Doe") is None

#cd "C:\ELA\1. Semester\Programmieren\programmieren_praktikum\Aufgaben\aufgabenblatt09"
#py -m pytest

