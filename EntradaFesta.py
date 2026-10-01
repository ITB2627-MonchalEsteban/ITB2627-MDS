try: 
    Edat = int(input("Quina edat tens?"))
    if Edat >= 18:
        print("Ets major d'edat")

        Vestit = str(input("Tens el bon vestit per entrar a la festa? (Ha de ser blanc)"))
        if Vestit == "blanc":
            print("Vestit correcte, pots entrar a la festa")

            Entrada = int(input("Tens la entrada? (1: Sí, 2: No)"))
            if Entrada == 1:
                print("Pots entrar a la festa")

            elif Entrada == 2:
                print("No pots entrar a la festa, necessites una entrada")
            else:
                print("Opció de vestit no vàlida")

        elif Vestit == "no":
            print("Vestit incorrecte, no pots entrar a la festa")
        else:
            print("Opció de vestit no vàlida")

    else:
        print("No ets major d'edat, no pots entrar a la festa")

except ValueError:
    print("Has d'introduir un números enters")