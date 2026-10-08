#1. Esercizio Base: Indovina il numero
# Inseriamo il numero segreto
# Inseriamo il numero segreto
numero_segreto = int(input("Inserisci il numero segreto: "))


# Funzione per indovinare
def indovina(a = 0):

    if a == numero_segreto:
        print("Indovinato!")
        return True

    elif a < numero_segreto:
        print("Il numero segreto è più alto!")
        pass

    else:
        print("Il numero segreto è più basso!")
        pass

    return False


# Inizio del programma
while True:

    numero = int(input("Prova a indovinare il numero: "))

    if indovina(numero):
        break

#2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
# Chiediamo il numero all'utente
n = int(input("Inserisci un numero N: "))
# Funzione Fibonacci
def fibonacci(n = 0):

    a = 0
    b = 1

    if n < 0:
        print("Inserisci un numero positivo")
        return False
    
    while a <= n: #continua a stampare i numeri di Fibonacci finché non supera il valore inserito dall'utente.
        print(a)

        somma = a + b # somma diventa 1
        a = b  # a diventa 1
        b = somma # b diventa 1

