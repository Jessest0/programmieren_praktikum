# a = 1
# b = 3
# for n in range(0,4):
#    print("." * b + "#" * a)
#    a = a + 1
#    b = b -1

# def ggt(a, b):
#    if(a == b):
#        print(a,"Ist der größte gemeinsame Teil der der Ursprungszahl")
#        return 1
#    elif(a > b):
#        a=a-b
#        return ggt(a,b)
#    else:
#        b=b-a
#        return ggt(a,b)
# ggt(18,783)

# def ist_prim(n):
#    if(n > 1):
#        for i in range(2, n-1):
#            if(n % i == 0):
#                print("False")
#                return False
#        else:
#            print("True")
#            return True
# ist_prim(99)

# %%
def validate_code(code):
    erg = 0
    for i in range(len(code)):
        if i % 2 == 0:
            erg += int(code[i])
        else:
            erg += int(code[i]) *3
    if erg % 10 == 0:
        print("ist valide")
        return True
    else:
        print("ist nicht valide")
        return False


code = input("Geben Sie einen EAN-13- oder ISBN-13-Code ein:")
if validate_code(code):
    print("Dieser Code ist valide")
else:
    print("Dieser Code ist nicht valide")
