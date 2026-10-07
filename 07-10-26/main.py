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
lista_numeri = [4, 7, 2, 10, 5]


