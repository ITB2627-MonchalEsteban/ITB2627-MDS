edat = 0
try:
    edat = int(input("Quina edat tens?"))
except ValueError:
    print("Has d'introduir un número enter")

if edat == int:
    if edat>=18:
        print("Ets major d'edat")
        if edat>=16:
            print("Pots conduir")
    else:
        if edat>16:
            print("Pots conduir")
    print("No ho ets i no pots conduir")

print("Programa Finalitzat")