length = int(input("Wie groß soll das Passwort sein?"))

def passwort(length):
    if length > 8 && length < 200:
        print(".")
        return True

    else:
        print("Das Passwort muss zwischen 8 und 200 Zeichen haben")
        return False

passwort(length)