def decoratore(funzione):

    def wrapper():
        print("Prima della funzione")
        funzione()
        print("Dopo la funzione")

    return wrapper


@decoratore
def saluta():
    print("Ciao Martina!")


saluta()

#funzioni richiamabili dal menu. Da qui tramite il while posso scegliere l'esercizio che voglio fare.

import random


def menu(): ## Qui inizializziamo la lista vuota e, attraverso if ed elif,
# scegliamo quale esercizio eseguire in base alla scelta dell'utente. 

    n = 0
    lista = []

    while True:

        scelta = input("Quale esercizio vuoi fare? Scegli da 1 a 7, premi 0 per uscire: ")

        if scelta == "1":
            n = numero_positivo()
            lista = []
            print("Hai inserito:", n)

        elif scelta == "2":
            n = numero_positivo()
            lista = genera_lista(n)
            print("Lista generata:", lista)

        elif scelta == "3":
            if lista == []:
                n = numero_positivo()
                lista = genera_lista(n)
                print("Lista generata:", lista)

            somma_pari(lista)

        elif scelta == "4":
            if lista == []:
                n = numero_positivo()
                lista = genera_lista(n)
                print("Lista generata:", lista)

            numeri_dispari(lista)

        elif scelta == "5":
            numero = int(input("Inserisci un numero: "))

            if numero_primo(numero):
                print("Il numero è primo")
            else:
                print("Il numero non è primo")

        elif scelta == "6":
            if lista == []:
                n = numero_positivo()
                lista = genera_lista(n)
                print("Lista generata:", lista)

            stampa_primi(lista)

        elif scelta == "7":
            if lista == []:
                n = numero_positivo()
                lista = genera_lista(n)
                print("Lista generata:", lista)

            somma_totale(lista)

        elif scelta == "0":
            break

# 1. Chiedere un numero intero positivo 
# Chiediamo all'utente un numero intero positivo.
# Il ciclo while continua finché non viene inserito un numero maggiore di zero.

def numero_positivo():

    while True:

        x = int(input("Inserisci un numero positivo: "))

        if x > 0:
            break

        print("Devi inserire un numero positivo")

    return x


# 2. Generare una lista di n numeri casuali tra 1 e n

def genera_lista(n):

    lista = []

    for i in range(n):
        lista.append(random.randint(1, n)) #stiamo generando un numero casuale da 1 a n

    return lista


# 3. Calcolare la somma dei numeri pari nella lista

def somma_pari(lista):

    somma = 0

    for numero in lista: 
    # Scorriamo la lista e controlliamo se i numeri sono pari

        if numero % 2 == 0:
            somma = somma + numero

    print("La somma dei pari è:", somma)


# 4. Stampare tutti i numeri dispari della lista

def numeri_dispari(lista):

    print("I numeri dispari sono:")

    for numero in lista:

        if numero % 2 != 0:
            print(numero)


# 5. Determinare se un numero è primo

def numero_primo(numero):

    if numero <= 1: # Qui verifichiamo e diciamo se il numero è minore o uguale a 1 non è primo
        return False

    for i in range(2, numero):  # Controlliamo se il numero è divisibile per altri numeri

        if numero % i == 0:
            return False

    return True


# 6. Stampare i numeri primi nella lista

def stampa_primi(lista):

    print("I numeri primi sono:")

    for numero in lista:
        if numero_primo(numero):
            print(numero)

# 7. Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è 
# un numero primo e stampa il risultato
def somma_totale(lista):

    somma = 0

    for numero in lista:  # In questo punto sommiamo tutti i numeri presenti nella lista
        somma = somma + numero

    print("La somma totale è:", somma)

    if numero_primo(somma): # Richiamiamo la funzione numero_primo per controllare la somma
        print("La somma è un numero primo")
    else:
        print("La somma non è un numero primo")

# IL programma si avvia 
print("Partenza del menu")
menu()
