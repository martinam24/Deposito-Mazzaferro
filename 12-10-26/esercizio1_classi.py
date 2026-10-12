#Esercizio svolto in classe per capire come funzionano i metodi

class Punto:

    def __init__(self, x:int, y:int):

        self.x = x
        self.y = y

    def muovi(self, dx:int, dy:int):

        self.x += dx
        self.y += dy

    def distanza_da_origine(self):

        return self.x-0, self.y-0


x = int(input('Inserisci la coordinata x: '))
y = int(input('Inserisci la coordinata y: '))

p1 = Punto(x, y)

print(f'Le coordinate del punto sono: ({p1.x}, {p1.y})')

dx = int(input('Inserisci di quanto vuoi spostare la coordinata x: '))
dy = int(input('Inserisci di quanto vuoi spostare la coordinata y: '))

p1.muovi(dx,dy)

print(f'Le coordinate aggiornate sono: ({p1.x}, {p1.y})')


# ESERCIZIO 2
# Dichiariamo una classe chiamata Libro
class Libro:

    # Metodo costruttore
    # Riceve tre parametri: titolo, autore e pagine
    def __init__(self, titolo, autore, pagine):

        # Attributo di istanza che contiene il titolo del libro
        self.titolo = titolo

        # Attributo di istanza che contiene il nome dell'autore
        self.autore = autore

        # Attributo di istanza che contiene il numero di pagine
        self.pagine = pagine

    # Metodo di istanza che restituisce le informazioni del libro
    def info_libro(self):

        # Return restituisce una stringa con le informazioni
        # Il simbolo + unisce le varie parti della stringa
        # str(self.pagine) converte il numero di pagine in stringa
        return ("Il libro " + self.titolo + " è stato scritto da "
                + self.autore + " e ha " + str(self.pagine) + " pagine.")


# CREAZIONE DEGLI OGGETTI DELLA CLASSE LIBRO

# Creiamo il primo oggetto della classe Libro
# Passiamo titolo, autore e numero di pagine
Libro1 = Libro("Assassinio sull'Orient Express", "Agata Christie", 300)

# Creiamo un secondo oggetto della stessa classe
Libro2 = Libro("Lavorare stanca", "Cesare Pavese", 200)


# VISUALIZZAZIONE DELLE INFORMAZIONI

# Richiamiamo il metodo info_libro del primo oggetto
# Il metodo restituisce una stringa 
print(Libro1.info_libro())

# Richiamiamo lo stesso metodo sul secondo oggetto
print(Libro2.info_libro())


# EXTRA

# Creiamo una lista vuota che conterrà gli oggetti Libro
libri = []

# Chiediamo all'utente quanti altri libri vuole creare
# int converte il valore inserito in un numero intero
numero_libri = int(input("Quanti altri libri vuoi creare? "))

# Inizializziamo un contatore a zero
contatore = 0

# Il ciclo si ripete finché il contatore è minore
# del numero di libri che l'utente vuole creare
while contatore < numero_libri:

    # Chiediamo all'utente il titolo del nuovo libro
    titolo = input("Inserisci il titolo: ")

    # Chiediamo all'utente il nome dell'autore
    autore = input("Inserisci l'autore: ")

    # Chiediamo il numero di pagine
    # int converte il valore inserito in un numero intero
    pagine = int(input("Inserisci il numero di pagine: "))

    # CREAZIONE DELL'OGGETTO

    # Creiamo un nuovo oggetto della classe Libro
    # Passiamo i dati inseriti dall'utente al costruttore
    nuovo_libro = Libro(titolo, autore, pagine)

    # Aggiungiamo l'oggetto appena creato alla lista libri
    # e con il metodo append aggiungiamo un elemento alla fine della lista
    libri.append(nuovo_libro)

    # Richiamiamo info_libro sull'oggetto appena creato
    print(nuovo_libro.info_libro())

    # Incrementiamo il contatore di 1 a ogni ripetizione
    # Equivale a contatore = contatore + 1
    contatore += 1



# EXTRA 

libri = []  # creo una lista vuota

numero_libri = int(input("Quanti altri libri vuoi creare? "))

contatore = 0

while contatore < numero_libri:

    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    pagine = int(input("Inserisci il numero di pagine: "))

    # Creazione dell'oggetto
    nuovo_libro = Libro(titolo, autore, pagine)

    libri.append(nuovo_libro)
    print(nuovo_libro.info_libro())

    contatore += 1 

# ESERCIZIO 2


# Creiamo una classe chiamata Contobanca
class Contobanca:

    # Metodo costruttore: viene eseguito quando creiamo un oggetto
    def __init__(self, intestatario, saldo):

        # Attributo di istanza che contiene il nome dell'intestatario
        self.intestatario = intestatario

        # Attributo di istanza che contiene il saldo del conto
        self.saldo = saldo

    # Metodo per depositare denaro sul conto
    def deposita(self, importo):

        # Controlliamo se l'importo è minore o uguale a zero
        if importo <= 0:
            print("Importo non valido")

        # Se l'importo è positivo, possiamo depositarlo
        else:

            # Aggiungiamo l'importo al saldo attuale
            self.saldo += importo

            # Stampiamo il messaggio
            print("Deposito effettuato")

    # Metodo per prelevare denaro dal conto
    def preleva(self, importo):

        # Controlliamo se l'importo è minore o uguale a zero
        if importo <= 0:
            print("Importo non valido")

        # Controlliamo se l'importo supera il saldo disponibile
        elif importo > self.saldo:
            print("Saldo insufficiente")

        # Se l'importo è valido e il saldo è sufficiente
        else:

            # Sottraiamo l'importo dal saldo attuale
            self.saldo -= importo

            # Qui il prelievo è stato effettuato e lo stampiamo
            print("Prelievo effettuato")

    # Metodo per visualizzare il saldo del conto
    def stampa_saldo(self):

        # Stampiamo il nome dell'intestatario e il saldo attuale
        print("Il saldo di", self.intestatario, "è:", self.saldo, "€")


# Chiediamo all'utente di inserire il proprio nome
intestatario = input("Inserisci il nome dell'intestatario: ")

# Creiamo un oggetto della classe Contobanca chiamato conto
# Passiamo il nome dell'intestatario e il saldo iniziale di 0 euro
conto = Contobanca(intestatario, 0)


# CREIAMO IL MENU

# Creiamo una variabile stringa inizialmente vuota
scelta_menu = ""

# Il ciclo continua finché l'utente non scrive "end"
while scelta_menu != "end":

    # Stampiamo le opzioni del menu
    print("1. Deposita")
    print("2. Preleva")
    print("3. Stampa saldo")
    print("end. Fine")

    # Chiediamo all'utente di scegliere un'opzione
    scelta_menu = input("Scegli un numero: ")

    # Se l'utente sceglie 1, vuole depositare denaro
    if scelta_menu == "1":

        # Chiediamo l'importo da depositare
        importo = float(input("Quanto vuoi depositare: "))

        # Richiamiamo il metodo deposita dell'oggetto conto
        # Passiamo il valore della variabile importo
        conto.deposita(importo)

    # Se l'utente sceglie 2, vuole prelevare il denaro
    elif scelta_menu == "2":

        # Chiediamo l'importo da prelevare
        importo = float(input("Quanto vuoi prelevare: "))

        # Richiamiamo il metodo preleva dell'oggetto conto
        conto.preleva(importo)

    # Se l'utente sceglie 3, vuole conoscere il saldo
    elif scelta_menu == "3":

        # Richiamiamo il metodo che stampa il saldo
        conto.stampa_saldo()

    # Se l'utente scrive end, significa che vuole terminare il programma
    elif scelta_menu == "end":

        # Stampiamo il messaggio di chiusura
        print("Qui concludiamo")

    # Se l'utente inserisce qualcos'altro non scritto nel codice stamperà il messaggio seguente
    else:

    
        print("Scelta non valida!")
#Esercizio auto

# Creiamo una classe chiamata Garage
class Garage:

    # Metodo costruttore
    # Riceve il parametro capienza, cioè il numero massimo di auto
    def __init__(self, capienza):

        # Attributo di istanza che contiene la capienza del garage
        self.capienza = capienza

        # Attributo di istanza che contiene la lista delle targhe
        # Inizialmente la lista è vuota perché non ci sono auto
        self.auto_presenti = []

    # Metodo speciale (Dunder Method)
    # Permette di utilizzare len() direttamente sull'oggetto Garage
    def __len__(self):

        # Restituisce il numero di auto presenti nella lista
        return len(self.auto_presenti)

    # Metodo per parcheggiare un'auto
    # Riceve come parametro la targa dell'auto
    def parcheggia(self, targa):

        # Inizialmente supponiamo che l'auto non sia presente
        # infatti con false significa che non abbiamo ancora trovato la targa
        trovata = False

        # Il ciclo for controlla una alla volta le targhe nella lista
        # la variabile auto assume il valore di ogni targa presente
        for auto in self.auto_presenti:

            # Confrontiamo la targa presente nella lista
            # con quella che l'utente vuole parcheggiare
            if auto == targa:

                # Se le targhe sono uguali, l'auto è già presente
                trovata = True

        # Controlliamo se il ciclo for ha trovato la targa
        if trovata == True:

            # Se l'auto è già presente, stampiamo un errore
            print("Errore, auto già presente")

        # Se la targa non è presente, controlliamo la capienza
        # len(self) conta quante auto ci sono nel garage
        elif len(self) >= self.capienza:

            # Se le auto presenti raggiungono la capienza massima
            # il garage è pieno e non possiamo aggiungere altre auto
            print("Errore: garage pieno")

        # Se la targa non è presente e il garage non è pieno
        else:

            # Aggiungiamo la targa alla lista delle auto presenti
            # append() inserisce un nuovo elemento alla fine della lista
            self.auto_presenti.append(targa)

            # Stampiamo un messaggio di conferma
            print("Auto parcheggiata correttamente")

    # Metodo per rimuovere un'auto dal garage
    # Riceve come parametro la targa da rimuovere
    def rimuovi(self, targa):

        # Inizialmente supponiamo che l'auto non sia presente
        trovata = False

        # Il ciclo for scorre tutte le targhe presenti nella lista
        for auto in self.auto_presenti:

            # Confrontiamo ogni targa con quella da rimuovere
            if auto == targa:

                # Se troviamo la targa, impostiamo trovata a True
                trovata = True

        # Controlliamo se abbiamo trovato la targa nella lista
        if trovata == True:

            # Rimuoviamo dalla lista la targa indicata
            # remove() elimina l'elemento specificato
            self.auto_presenti.remove(targa)

            # Stampiamo un messaggio di conferma
            print("Auto rimossa correttamente")

        # Se la targa non è stata trovata nella lista
        else:

            # Stampiamo un messaggio di errore
            print("Errore: auto non presente")

    # Metodo per calcolare il numero di posti liberi
    def posti_liberi(self):

        # Sottraiamo le auto presenti dalla capienza massima
        # len(self) richiama automaticamente il metodo __len__
        # e qui restituisce il numero di posti ancora disponibili
        return self.capienza - len(self)


# CREAZIONE DELL'OGGETTO

# Chiediamo all'utente la capienza del garage
capienza = int(input("Inserisci la capienza del garage: "))

# Creiamo un oggetto della classe Garage chiamato garage
# Passiamo al costruttore la capienza inserita dall'utente
garage = Garage(capienza)


# CREIAMO IL MENU

# Inizializziamo una variabile stringa vuota
scelta_menu = ""

# Il ciclo while continua finché l'utente non scrive "end"
while scelta_menu != "end":

    # Stampiamo le opzioni del menu
    print("1. Parcheggia")
    print("2. Rimuovi")
    print("3. Stampa posti liberi")
    print("4. Stampa auto presenti")
    print("end. Fine")

    # Chiediamo all'utente di scegliere un'opzione
    scelta_menu = input("Scegli un numero: ")

    # Se l'utente sceglie 1, vuole parcheggiare un'auto
    if scelta_menu == "1":

        # Chiediamo la targa dell'auto da parcheggiare
        targa = input("Inserisci la targa: ")

        # Richiamiamo il metodo parcheggia dell'oggetto garage
        # Passiamo come argomento la targa inserita
        garage.parcheggia(targa)

    # Se l'utente sceglie 2, vuole rimuovere un'auto
    elif scelta_menu == "2":

        # Chiediamo la targa dell'auto da rimuovere
        targa = input("Inserisci la targa da rimuovere: ")

        # Richiamiamo il metodo rimuovi dell'oggetto garage
        garage.rimuovi(targa)

    # Se l'utente sceglie 3, vuole conoscere i posti liberi
    elif scelta_menu == "3":

        # Richiamiamo il metodo posti_liberi
        # print visualizza il valore restituito da return
        print("Posti liberi:", garage.posti_liberi())

    # Se l'utente sceglie 4, vuole visualizzare le targhe
    elif scelta_menu == "4":

        # Accediamo all'attributo auto_presenti dell'oggetto
        # e stampiamo la lista delle targhe parcheggiate
        print("Auto presenti:", garage.auto_presenti)

    # Se l'utente scrive end, vuole terminare il programma
    elif scelta_menu == "end":

        # Stampiamo un messaggio di chiusura
        print("Qui concludiamo")

    # Se l'utente inserisce un'opzione non prevista
    else:

        # Stampiamo un messaggio di errore
        print("Scelta non valida!")


