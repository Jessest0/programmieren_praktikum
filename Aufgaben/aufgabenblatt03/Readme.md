
## Aufgabe 1: Zufallszahlen raten
Schreiben Sie ein Programm für das folgende Zahlenratespiel:

1. Das Programm wählt eine zufällige Zahl zwischen 0 und 127 (jeweils einschließlich).
2. Die Benutzerin oder der Benutzer hat 7 Versuche, die Zahl zu erraten.
3. Bei jedem Versuch soll das Programm angeben, ob die Zahl zu hoch oder zu niedrig ist.
4. Wenn die Zahl erraten wurde, wird die Benutzerin bzw. der Benutzer beglückwünscht.

**Hinweis**: Nutzen Sie die Funktion [`random.randint()`](https://docs.python.org/3/library/random.html#random.randint) aus der `random`-Bibliothek.

**Zusatzfrage (optional)**: Woher kommen wohl die "krummen" Zahlen in der Aufgabenstellung? Gibt es eine Strategie, mit der Sie dieses Spiel immer gewinnen können?

### Lösung

```
import random

x = random.randint(0,127)

for i in range(1,7):
    y = int(input("Raten Sie die Zahl "))
    if y < x:
        print("Die gesuchte Zahl ist größer als ihre Eingabe, Sie haben ",i,"Versuche verbraucht")

    elif y > x:
        print("Die gesuchte Zahl ist kleiner als ihre Eingabe, Sie haben ",i,"Versuche verbraucht")
    else:
        print("Glückwunsch",y,"ist die gesuchte Zahl")

```

## Aufgabe 2: Countdown


Schreiben sie ein Programm, das einen Countdown ausgibt:

1. Das Programm fragt die Nutzerin oder den Nutzer nach einer positiven ganzen Zahl (1, 2, ...). Ist die Zahl nicht positiv, gibt das Programm eine Fehlermeldung aus. Sie müssen nicht prüfen, ob es sich um eine ganze Zahl handelt (das Programm darf dann mit einem Programmfehler abgebrochen werden).
2. Das Programm zählt von der angegebenen Zahl im Sekundentakt bis einschließlich 1 herunter (z.B. `5`, `4`, `3`, `2`, `1`).
3. Das Programm gibt den Text "Lift off!" aus.

*Hinweis*: Um eine Sekunde zu warten, können Sie die Funktion [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep) verwenden.

## Lösung

```
import time

x = int(input("Geben sie eine Sekundenzahl an"))

for x  in range(x, -1, -1):
    if x >= 1:
        print(x)
        time.sleep(1)
    else:
        print("Lift off!")
```

## Aufgabe 3: Reaktionszeit messen

Schreiben Sie ein Programm, das die Reaktionszeit der Nutzerin oder des Nutzers misst:

1. Das Programm wartet eine zufällige Anzahl von Sekunden.
2. Nach Ablauf der Zeit gibt es eine Meldung aus und wartet auf eine Eingabe.
3. Nach der Eingabe gibt es die Reaktionszeit der Nutzerin oder des Nutzers in Sekunden aus.

**Hinweise**
* Verwenden Sie die Funktion `time.sleep()`, um die gewünschte Zeit zu warten.
* Die Funktion `time.time_ns()` gibt Ihnen die [Unixzeit](https://de.wikipedia.org/wiki/Unixzeit) in Nanosekunden (1 Nanosekunde = 1/1 000 000 000 Sekunde) aus. Die Reaktionszeit können Sie bestimmen, indem Sie einmal vor der Meldung und einmal nach der Eingabe die aktuelle Unixzeit bestimmen und die Differenz aus den beiden Zeiten berechnen.
* Nutzen Sie die Funktion [`random.uniform()`](https://docs.python.org/3/library/random.html#random.uniform), um eine zufällige Kommazahl in einem bestimmten Bereich zu erzeugen. Alle Zahlen im angegebenen Bereich werden mit gleicher Wahrscheinlichkeit vorkommen (sog. Gleichverteilung oder "Uniform Random Distribution", daher der Name der Funktion).

```
import random
import time

waittime = random.uniform( 2, 10)
time.sleep(waittime)

starttime = time.time_ns()

input("Drücken sie schnell Enter")

endtime = time.time_ns()

reactiontime = (endtime - starttime) / 1000000

print(reactiontime)

```

## Aufgabe 4

```

1.Eingabe mit Input in eine variable speichern, gibt an wie viele zeichen 

x = int(Input("Geben sie an wie lang das Passwort sein soll")

2. if abfrage ob passwort: 
	if Input < 8 or Input > 200:
		for i in range(0, len(x)):
			PW[i] =  randomchoise(sting.ascii:letters + string Digits)
	else: 
		return false
	

print("Ihr Passwort ist", PW)

```
