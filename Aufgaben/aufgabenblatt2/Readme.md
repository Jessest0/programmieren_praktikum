# Aufgabenblatt 2

# Aufgabe 1
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

## Aufgabe 2
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