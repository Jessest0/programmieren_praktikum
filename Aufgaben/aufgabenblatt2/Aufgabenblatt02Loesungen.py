def ist_prim(n):

    if(n > 1):
        for i in range(2, n-1):
            if(n % i == 0):
                return False

        return True
    else:
        return False
print(ist_prim(29))
