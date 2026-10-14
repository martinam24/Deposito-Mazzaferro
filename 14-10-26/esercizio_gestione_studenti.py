
#Incapsulamento è il principio della programmazione orientata agli oggetti che permette di controllare l'accesso agli attributi.
#Name mangling è il meccanismo di Python che modifica internamente i nomi degli attributi che iniziano con __.

#Esercizio Sistema di gestione studenti
# CLASSE PERSONA
class Persona:

    # Metodo costruttore
    def __init__(self, nome, eta):

        # Attributi privati
        self.__nome = nome
        self.__eta = eta

    # Getter per leggere il nome
    def get_nome(self):
        return self.__nome

    # Setter per modificare il nome
    def set_nome(self, nome):

        if nome != "":
            self.__nome = nome
            print("Nome modificato") #avvisiamo l'utente che il nome è sttao cambiato correttamente

        else:
            print("Nome non valido")

    # Getter per leggere l'età
    def get_eta(self):
        return self.__eta

    # Setter per modificare l'età
    def set_eta(self, eta):

        if eta < 0:
            print("Età non valida")

        else:
            self.__eta = eta
            print("Età modificata")

    # Metodo per presentare la persona
    def presentazione(self):

        print("Sono", self.__nome, "e ho", self.__eta, "anni")


# CLASSE STUDENTE

# Dalla classe studente Studente ereditiamo la classe Persona
class Studente(Persona):

    # Metodo costruttore
    def __init__(self, nome, eta, voti):

        # Inizializziamo nome ed età della classe Persona
        Persona.__init__(self, nome, eta)

        # Attributo privato che contiene la lista dei voti
        self.__voti = voti

    # Metodo per calcolare la media dei voti
    def calcola_media(self):

        # Creiamo una variabile per la somma
        somma = 0

        # Controlliamo che ci siano voti
        if len(self.__voti) == 0:
            return 0

        else:

            # Scorriamo tutti i voti della lista
            for voto in self.__voti:

                # Sommiamo i voti
                somma = somma + voto

            # Calcoliamo la media
            media = somma / len(self.__voti)

            # Restituiamo la media
            return media

    # Metodo per stampare le informazioni dello studente
    def stampa_studente(self):

        print("Studente:", self.get_nome())
        print("Età:", self.get_eta())
        print("Media dei voti:", self.calcola_media())


# CLASSE PROFESSORE

# Qui ereditiamo la classe Persona che poi definisce quella di Professore
class Professore(Persona):

    # Metodo costruttore
    def __init__(self, nome, eta, materia):

        # Inizializziamo nome ed età della classe Persona
        Persona.__init__(self, nome, eta)

        # Attributo privato che contiene la materia insegnata
        self.__materia = materia

    # Metodo per stampare le informazioni del professore
    def stampa_professore(self):

        print("Professore:", self.get_nome())
        print("Età:", self.get_eta())
        print("Materia insegnata:", self.__materia)


# CREO GLI OGGETTI DI OGNI CLASSE

# Oggetto classe Persona
persona1 = Persona("Michele", 32)

# Oggetto Studente
studente1 = Studente("Martina", 25, [21, 23, 28, 24])

# Oggetto della classe Professore
professore1 = Professore("Esposito", 57, "Inglese")

# Qui vediamo i risultati stampati

print("\nPRESENTAZIONE PERSONA")
persona1.presentazione()

print("\nPRESENTAZIONE STUDENTE")
studente1.stampa_studente()

print("\nPRESENTAZIONE PROFESSORE")
professore1.stampa_professore()
