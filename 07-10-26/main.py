#esercizio punto 1
x = int(input("Inserisci un numero: "))

if x % 2 == 0:
    print("pari")
else:
    print("dispari")

# esercizio punto 2

while True:

    x = int(input("Inserisci un numero positivo: "))

    for i in range(0, x + 1, 1):
        print(i)

    scelta = input("Vuoi ripetere? si/no: ")

    if scelta == "no":
        break
#esercizio punto 3
lista_numeri = [2, 4, 6, 8]

for x in lista_numeri:
    quadrato = x * x
    print(quadrato)
#esercizio punto 4





#esercizio ciclo while

numeri = []

x = int(input("Inserisci un numero: "))

while x != 0:
    numeri.append(x)
    x = int(input("Inserisci un numero: "))

somma = 0

for x in numeri:
    somma = somma + x

print("La somma è:", somma)
#esercizio ciclo for
ripetuto = False

while True:

    parola = input("Inserisci una parola: ")

    for x in parola:
        print(x)

    if ripetuto == True:
        break

    scelta = input("Vuoi ripetere? si/no: ")

    if scelta == "no":
        break

    ripetuto = True
#esercizio ciclo range
x = int(input("Inserisci il numero massimo: "))

for i in range(2, x + 1, 2):
    print(i)

    #esercizio extra 1
       
while True:

    scelta = input("Puoi scegliere esercizio 1, 2, 3 oppure end per uscire: ")


    if scelta == "1":

        # ESERCIZIO 1
        numeri = []

        x = int(input("Inserisci un numero: "))

        while x != 0:
            numeri.append(x)
            x = int(input("Inserisci un numero: "))

        somma = 0

        for x in numeri:
            somma = somma + x

        print("La somma è:", somma)


    if scelta == "2":

        # ESERCIZIO 2
        parola = input("Inserisci una parola: ")

        for x in parola:
            print(x)


    if scelta == "3":

        # ESERCIZIO 3
        x = int(input("Inserisci il numero massimo: "))

        for i in range(2, x + 1, 2):
            print(i)


    if scelta == "end":
        break

#esercizio extra 2
lista = []
while True:

    scelta = input(
        "Scegli: aggiungi, modifica, rimuovi, visualizza, svuota oppure end: ")
        if scelta == "aggiungi":
        elemento = input("Inserisci un elemento: ")
        lista.append(elemento)