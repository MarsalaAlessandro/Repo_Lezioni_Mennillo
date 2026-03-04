# Questo è un commento
# Cos'è una variabile?
# è un contenitore che memorizza un valore. Questo valore può cambiare durante l'esecuzione del codice

nome = "Alessandro"
eta = 17
corso = "tecnico informatico"
altezza = 1.78

#indipendentemente dal tipo che scelgo non viene dichiarato da nessuna parte:
#questo comportamento è tipico dei linguaggi debolmente tipizzati

# Esercizio: Istanzia 2 variabili (nome a tua scelta) di tipo intero. con queste 2 variabili elabora le 4 operazioni matematica, stampa in console con un print i risultati.

x = 4
y = 6

print(x + y)
print(x - y)
print(x*y)
print(x/y)

#oppure

somma = x + y
sottrazione = x - y
moltiplicazione = x * y
Divisione = x / y

print(somma)
print(sottrazione)
print(moltiplicazione)
print(Divisione)

#numeri con la virgola o float

pi = 3.14159
temperatura = 21.5

print(type(pi))
print(type(temperatura))

calcolo = 0.1 + 0.2
print(calcolo) #0.3000000000004 attenti alla precisione
print(round(calcolo, 2)) #round(numero, precisione) questo metodo arrotonda

#stringhe : sono sequenze immutabili di caratteri. Le stringhe sono il modo umano di comunicare

nome = "abc"
email = "erfer@gmail.com"
corso = "tecnico informatico"

#concatenazione tra stringhe

print(nome + " " + email + " " + corso)

print(nome, "-", email, "eta: ", eta, "anni") #visto che l'età è un numero utilizzo la , per concatenare le stringhe

#f-string è il modo moderno di formattare le stringhe
#la stringa comincia con la f all'esterno delle "" e richiamo attraverso le {}
#il nome delle variabili. Anche in questo caso posso miscelare le variabili

print(f"{nome} - email: {email} - età: {eta}")

#Esercizio

mioNome = "Alessandro"
mioCognome = "Marsala"
miaEta = 17
mioCorso = "Tecnico Informatico"

print(f"mi chiamo {mioNome}, il mio cognome è {mioCognome}, ho {miaEta} anni, frequento il corso {mioCorso}")