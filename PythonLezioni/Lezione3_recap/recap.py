nome = "Alessandro"
Cognome = "Marsala"
eta = 17
corso = "Tecnico informatico"
altezza = 1.75
presenza = True

print(f"Ciao mi chiamo {nome} e il mio cognome è {Cognome}, ho {eta} anni, frequento il corso {corso}, sono alto {altezza}")

if presenza:
    print("Oggi sono presente")
else:
    print("oggi sono assente")

print("-------- IL MIO AMICO ---------")

#Adesso presenta un tuo compagno/amico di classe. Fai attenzione ad assegnare delle variabili con un altro nome
nome1 = "Luca"
cognome1 = "Benedetto"
eta1 = 18
altezza1 = 1.74
presenza1 = False

print(f"Mi chiamo {nome1}, il mio cognome è {cognome1}, ho {eta1} anni e sono alto {altezza1}")

if presenza1 == False:
    print("Oggi sono assente")
else:
    print("Oggi sono presente")

if eta1 < 60:
    print(f"{nome1} è ancora giovane")
else:
    print(f"{nome1} non è più così giovane")