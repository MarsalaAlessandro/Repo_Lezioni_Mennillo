#IF STATEMENT, questo costrutto serve a controllare e prendere una scelta
# Operatori di confronto
# == (uguale a)
# != (diverso da)
# > (maggiore)
# < (minore)
# >= (maggiore uguale)
# <= (minore uguale)

#Tutte le volte che uso un operatore di confronto sto generando un valore booleano

#I valori boolean mi servono proprio negli if statement

#Sintassi:
#if condizione:
#       corpo dell'if che viene eseguito se la condizione è true
#else:
#   corpo dell'else che viene eseguito se la condizione è false

# Esempio 1
piove = False

if piove:
    print("Porto l'ombrello")
else:
    print("Non porto l'ombrello")

# Esempio 2

Eta = 17

if Eta >= 18:
    print("Sono Maggiorenne")
elif Eta < 0:
    print("Età invalida")
else:
    print("Sono Minorenne")

# Esempio 3

etaLorenzo = 18
etasanna = 17

if etaLorenzo > etasanna:
    print(f"Lorenzo ha {etaLorenzo} anni ed è più grande di sanna")
elif etaLorenzo == etasanna:
    print("Sanna e Lorenzo sono coetanei")
else:
    print(f"Sanna ha {etasanna} anni ed è più grande di Lorenzo")

#Esempio 4 - Confronto tra stringhe

parola1 = "ciao"
parola2 = "ciao"
parola3 = "ciao"

if parola1 == parola2:
    print("Le due parole sono uguali")
elif parola1 != parola2:
    print("Le due parole sono diverse")
else:
    print("Non mi hai fornito due parole")

#Esempio 5 - confronto tra stringhe senza tenere conto dell'uppercase o lowercase

stringa1 = "Caffè"
stringa2 = "Caffè"

if stringa1.lower() == stringa2.lower():
    print(f"Le due stringhe sono uguali: {stringa1}")
else:
    print(f"Le due stringhe sono diverse: {stringa1} e {stringa2}")


#Esempio 6 - Altri confronti tra stringhe
#Possiamo confrontare porzioni di stringhe

frase = "Ciao Dario, come stai?"

print(frase.startswith("cia")) #True
print(frase.endswith("?")) #True
print("Dario" in frase) #True

if "Dario" in frase:
    print("La stringa di Dario si trova nella frase")
else:
    print("La parola Dario non si trova nella frase")

if frase.startswith("Cia"):
    print("La frase inizia con Cia")
else:
    print("La frase non comincia con Cia")

# Esempio 7 - Voto e valutazione
# Patente di guida. Per iscrivermi all'esame devo aver compiuto 18 anni.
# Utilizzo il metodo input per recuperare un valore dal terminale

nomestudente = input("Come ti chiami?")
etaStudente = int(input("Quanti anni hai?"))

if etaStudente >= 18:
    print(f"Benvenuto {nomestudente}, puoi iscriverti all'esame di scuola guida")
elif etaStudente < 18 and etaStudente >= 15:
    print(f"Benvenuto {nomestudente}, con la tua età puoi solo accedere all'esame per la patente AM")
else:
    print(f"Benvenuto {nomestudente}, con la tua età non puoi ancora iscriverti da nessuna parte")