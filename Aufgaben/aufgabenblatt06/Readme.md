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


```