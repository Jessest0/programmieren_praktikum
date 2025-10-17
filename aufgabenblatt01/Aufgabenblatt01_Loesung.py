#Aufgabe 1___

#Setze S auf eine leere Liste.
#Wenn L leer ist, beende das Verfahren.
#Finde die kleinste Zahl in L. Wir bezeichnen diese Zahl mit n.
#Entferne die Zahl n aus L. (Wenn Sie mehrfach vorkommt, entferne Sie nur einmal.)
#Füge n hinten an S an.
#Setze bei Schritt 3 fort.

#Das ist eine Größensortieralgorithmus, man nehme die kleinste zahl aus L(die eingabeliste)
#und setze diese kleineste zahl an die hinterstelle stelle in S bis die Liste L leer ist.

#Setze S auf eine leere Liste.
#Wenn L leer ist, beende das Verfahren.
#Sei n die erste Zahl in L.
#Entferne die erste Zahl in L.
#Wenn S mindestens ein Element kleiner oder gleich n enthält: Finde die größte Zahl in S,
# die kleiner oder gleich n ist und füge n dahinter in S ein.
#Wenn S kein Element kleiner oder gleich n enthält (oder S leer ist): Füge n als erstes
# Element in S ein.
#Setze bei Schritt 3 fort.

#Dieser algorithmus tut das gleich wie der davor, nur schaut immer explizit nach der
#kleinsten zahl, was er abhängig von der zählervariable macht, das sortiert die Liste




## Aufgabe 2: Operationen
#Betrachten Sie die folgenden Python-Ausdrücke und bestimmen Sie zunächst ohne Hilfe des Computers ihren Wert und den Typ des Werts. Überprüfen Sie Ihr Ergebnis danach, indem Sie die Ausdrücke mit Python auswerten.

#i = -7 + 3 * 8 = 17 / 17 typ int
#i = 17 / (5/3) * 4 = 40,7999 / code = 40,8 typ float
#i = (9 + (3 - (2 + 3))) / 2 = 3.5 / 3.5 typ float
#i = 5**4/2 = 312.5 / 312.5 typ float
#i = int(-5/2) = -2,5 / -2 weil rundung gegen 0 bzw schneidet nachkomma ab
#print(i)

#Aufgabe 3
#age = int(input("Wie alt bist du? ")) #Die eingabe muss als int erfolgen und nicht als sting
 # weil wir int mit string nicht vergleichen können
#if age >= 18: # >= statt =>
#    print("Du bist volljährig.")
#else:
#    print("Du bist minderjährig.")

#__________

#x = 42
#if x > 42:
#    print("X ist größer 42") #python macht unterschiede bei der zeileneinruekung, heisst
    # der befehl, der nach dem if ausgeführt wird, muss dahinter eingereiht sein
#elif x < 42:
#    print("X ist kleiner 42")
#else:
#    print("X gleich 42")

#%% md

#x = 10
#if x == 10:
#    print("X ist 10")
#else:
#    print("X ist nicht 10")


## Aufgabe 4: Ostertermin
#Der deutsche Mathematiker Carl Friedrich Gauß hat im Jahr 1816 einen Algorithmus für die Berechnung des Osterdatums - genauer, des Ostersonntags - bereitgestellt. Angenommen, die Variable `Jahr` enthält die Jahreszahl (z.B. 2024 für das Jahr 2024), so berechnen die folgenden nacheinander anzuwendenden Formeln das Osterdatum:

Jahr = int(input("Welches Jahr haben wir?"))

a = Jahr % 19
b = Jahr % 4
c = Jahr % 7
k = Jahr // 100
p = (8*k+13) // 25
q = k // 4
M = (15 + k - p - q) % 30
d = (19+a + M) % 30
N = (4 + k - q) % 7
e = (2+b + 4+c + 6+d + N) % 7
f = 22+d+e

if(f <= 31):
    g = 3
else:
    g = 4
    f = f-31
print("Ostern im Jahr",Jahr, "ist am",f,".",g)

# mod = %
#div = // Divisionsrest
# 8k geht nicht, da muss ein * operator dazwischen
