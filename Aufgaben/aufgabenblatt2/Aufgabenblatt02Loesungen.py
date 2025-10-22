def ist_prim(n):
    if n < 2:
        for i in range(2, int(n-1)):
            if n % i == 0:
                return False
    else:
        return False



ist_prim(25)