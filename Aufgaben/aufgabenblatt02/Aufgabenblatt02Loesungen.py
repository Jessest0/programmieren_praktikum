def validate_code(code):

    if code == code[12]:
        erg = 0
        for i in range(0, len(code)):
                if i % 2 == 0:
                    erg += int(code[i])
                else:
                    erg += int(code[i]) * 3

        if (erg % 10 == 0):
            return True
        else:
            return False


code = input("Geben Sie einen EAN-13- oder ISBN-13-Code ein:")
if validate_code(code):

    print("Dieser Code ist valide")
else:
    print("Dieser Code ist nicht valide")
