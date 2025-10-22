# Aufgabenblatt 2 Lösung




## Aufgabe 1: Pyramide
Schreiben Sie eine Funktion `pyramid`, die eine Pyramide mit der angegebenen Anzahl von Ebenen ausgibt.

Beachten Sie dabei, dass Leerzeichen mit einem Punkt gefüllt werden.

Beispiel: `levels = 4`
```
 ...#
 ..##
 .###
 ####
```
Lösung:
```
x = "."
y = "#"

def pyramid(n):
    i = 4
    for n in range(1,5):
        i -= 1
        print(x*i+y*n)

pyramid(1)
```



## Aufgabe 2: Größter Gemeinsamer Teiler
Schreiben Sie eine Funktion `ggt`, die den größten gemeinsamen Teiler zweier gegebener natürlicher Zahlen (1,2,3,...) berechnet.
Der größte gemeinsame Teiler zweier ganzer Zahlen ist die größte Zahl, die beide Zahlen ohne Rest teilt.
So ist etwa der größte gemeinsame Teiler von 6 und 9 die Zahl 3.

Für die Berechnung verwenden wir den [euklidschen Algorithmus](https://de.wikipedia.org/wiki/Euklidischer_Algorithmus).
Der Algorithmus lautet wie folgt:

* Gegeben seien die beiden natürliche Zahlen `a` und `b`. (Sie müssen nicht prüfen, ob es sich um natürliche Zahlen handelt!)
* Es müssen folgende Schritte ausgeführt werden.
    1. Wenn `a` und `b` gleich sind, beende das Verfahren. `a` und `b` sind der größte gemeinsame Teiler des ursprünglichen Zahlenpaares.
    2. Ansonsten ersetze die größere Zahl durch die Differenz von größerer und kleinerer Zahl (z.B. `a=a-b` wenn `a` die größere Zahl ist).
    3. Setze bei Schritt 1 fort.

**Beispielrechnung für `a=27` und `b=18`**:
1. Die Zahlen sind nicht gleich. `a` ist größer, also ersetzen wir `a` durch `a-b=27-18=9` und setzen mit den neuen Zahlen `a=9` und `b=18` fort.
2. Die Zahlen sind nicht gleich. `b` ist größer, also ersetzen wir `b` durch `b-a=18-9=9` und setzen mit den neuen Zahlen `a=9` und `b=9` fort.
3. Die Zahlen sind gleich. Der größte gemeinsame Teiler ist also `9`.

**Beispiel**: Das Ergebnis von `gcd(18, 783)` sollte `9` sein.

Testen Sie Ihre Implementierung.

Lösung:
```
def ggt(a, b):
    if(a == b):
        print(a,"Ist der größte gemeinsame Teil der der Ursprungszahl")
        return 1
    elif(a > b):
        a=a-b
        return ggt(a,b)
    else:
        b=b-a
        return ggt(a,b)
ggt(25,5)
```


## Aufgage 3: Primzahlen erkennen
Schreiben Sie eine Funktion `ist_prim`, die `True` zurückgibt, wenn die übergebene natürliche Zahl (1, 2, 3, ...) eine Primzahl ist, und ansonsten `False`.
Eine natürliche Zahl `n` ist genau dann eine Primzahl, wenn sie größer als 1 ist und durch keine der ganzen Zahlen von `2` bis `n-1` (jeweils einschließlich) ohne Rest teilbar ist.

**Hinweis**: Sie dürfen annehmen, dass die übergebene Zahl eine natürliche Zahl ist!

**Beispiel**: Das Ergebnis von `ist_prim(29)` soll `True` sein, das von `ist_prim(25)` soll `False` sein (da 25 durch 5 teilbar ist).
```
def ist_prim(n):

    if(n > 1):
        for i in range(2, n-1):
            if(n % i == 0):
                return False

        return True
    else:
        return False
print(ist_prim(29))
```



