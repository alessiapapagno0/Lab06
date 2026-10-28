from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        conn=get_connection() #stabilisco la connessione e creo il cursore
        cursore=conn.cursor(dictionary=True)
        query='''SELECT *  
                FROM strumento'''
        cursore.execute(query) #prendo tutti i strumenti dal database
        lista_strumenti=[]
        for row in cursore: #per ogni strumento, creo un oggetto della classe Strumento
            s=Strumento(row['codice'], row['tipo'],row['marca'],int(row['anno_acquisto']),float(row['valore']),row['disponibile'])
            lista_strumenti.append(s) #creo una collezione di oggetti

        if lista_strumenti==[]: #se la lista è vuota, restituisce None
            return None
        else:
            return lista_strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        conn=get_connection()
        cursore=conn.cursor(dictionary=True) #faccio la stessa cosa in questa funzione
        query='''SELECT *
                FROM strumento
                WHERE tipo = %s '''

        cursore.execute(query,(tipo,))

        lista_strumenti_per_tipo= []
        for row in cursore:  # per ogni strumento, creo un oggetto della classe Strumento
            s = Strumento(row['codice'], row['tipo'], row['marca'], int(row['anno_acquisto']), float(row['valore']),
                          row['disponibile'])
            lista_strumenti_per_tipo.append(s)  # creo una collezione di oggetti

        if lista_strumenti_per_tipo == []:  # se la lista è vuota, restituisce None
            return None
        else:
            return lista_strumenti_per_tipo