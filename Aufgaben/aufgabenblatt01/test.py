Jahr = int(input("Welches Jahr haben wir?"))

a = Jahr % 19
b = Jahr % 4
c = Jahr % 7
k = Jahr // 100
p = (8*k+13) // 25
q = k // 4
M = (15 + k - p - q) % 30
d = (19*a + M) % 30
N = (4 + k - q) % 7
e = (2*b + 4*c + 6*d + N) % 7
f = 22+d+e

if f <= 31:
    m = 3
    print("Ostern ist am",f,".",m)
else:
    m = 4
    f = f-31
    print("Ostern ist am",f,".",m)
