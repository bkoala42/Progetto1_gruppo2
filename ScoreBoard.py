from utils import *
import copy


class ScoreBoard:
    """
    La classe è implementata mantenendo la lista di scores ordinata, in modo tale da rendere efficienti le operazioni
    top() e last() che non richiedono un ordinamento al momento della chiamata.
    Si è supposto che queste fossero le operazioni più richieste e la gestione dell'ordinamento avviene all'inserimento.
    """
    class Score:
        """
        Classe innestata che rappresenta lo score
        """
        def __init__(self, nome, score, data):
            self._nome = nome
            self._score = score
            self._data = data

        def __ge__(self, other):
            """
            Override dell'operatore >= basato sul confronto del solo campo score. Complessità computazionale O(1).
            """
            return self._score >= other._score

        def __gt__(self, other):
            """
            Override dell'operatore > basato sul confronto del solo campo score. Complessità computazionale O(1).
            """
            return self._score > other._score

        def __eq__(self, other):
            """
            Override dell'operatore == che verifica l'uguaglianza tra due score. La condizione è
            verificata se tutti i campi dei due score coincidono. Complessità computazionale O(1).
            """
            return self._score == other._score and self._data == other._data and self._nome == other._nome

        def __str__(self):
            return '%-12s|%-5s|%-5s' % (str(self._nome), str(self._score), str(self._data))

    def __init__(self, x=10):
        """
        Crea uno scoreboard di dimensione x.
        """
        self._l = CircularPositionalList()
        self._max_size = x

    def __len__(self):
        """
        Restituisce la dimensione dello scoreboard. Complessità computazionale O(1).
        """
        return self._max_size

    def __str__(self):
        """
       Restituisce una rappresentazione in stringa dello scoreboard. Complessità computazionale O(_max_size).
       """
        t = '\n\t\tScoreboard\n'
        i = 0
        curr = self._l.last()
        while i < len(self._l):
            t += str(curr.element()) + '\n'
            curr = self._l._before(curr)
            i += 1
        return t

    def size(self):
        """
        Restituisce il numero di score contenuti nello scoreboard. Complessità computazionale O(1).
        """
        return len(self._l)

    def Is_empty(self):
        """
        Verifica che lo scoreboard sia vuoto. In caso positivo restituisce True, altrimenti False.
        Complessità computazionale O(1).
        """
        return self._l.Is_empty()

    def insert(self, s):
        """
        Inserisce lo score s parametro nello scoreboard in ordine. Nel caso in cui nello scoreboard siano già presenti
        score uguali l'inserimento viene rifiutato. Se lo scoreboard è pieno l'inserimento avviene solo se lo score s
        da inserire è migliore dello score peggiore presente nello scoreboard. Tale inserimento non modifica la
        dimensione poiché lo score peggiore viene scartato. Complessità computazionale O(_max_size).
        """
        # Controlla se lo scoreboard è pieno
        if self.size() < self._max_size:
            # Inserisce semplicemente in testa se lo scoreboard è vuoto o lo score da inserire è peggiore dei correnti
            if self._l.Is_empty() or not s >= self._l.first().element():
                self._l.add_first(s)
            # Inserisce semplicemente in coda se lo score è migliore del corrente migliore
            elif s >= self._l.last().element():
                self._l.add_last(s)
            else:
                # Cerca la posizione di inserimento
                curr = self._l.first()
                while s >= curr.element():
                    # esci se lo score è già presente
                    if s == curr.element():
                        return
                    else:
                        curr = self._l._after(curr)
                # Inserisce
                self._l.add_before(curr, s)
        # Inserimento a scoreboard pieno solo se s è migliore dello score peggiore salvato
        elif s > self._l.first().element():
            # Inserisce semplicemente in coda se lo score è migliore del corrente migliore

            if s >= self._l.last().element():
                self._l.add_last(s)
            else:
                # Cerca la posizione di inserimento
                curr = self._l.first()
                while s >= curr.element() and curr != self._l.last():
                    if s == curr.element():
                        # esci se lo score è già presente
                        return
                    curr = self._l._after(curr)
                # Inserisce
                self._l.add_before(curr, s)
            # Cancella l'ultimo score, ovvero il peggiore
            self._l.delete(self._l.first())

    def merge(self, new):
        """
        Fonde lo scoreboard corrente allo scoreboard new. Il nuovo scoreboard conterrà al più un numero di score
        pari alla dimensione dello score corrente. Complessità computazionale O(_max_size).
        """
        # Merge degli scores tramite la funzione merge del modulo utils
        merged_scoreboards = merge(self._l, new._l)
        self._l.clear()
        curr = merged_scoreboards.last()
        for i in range(0, min(self._max_size, len(merged_scoreboards))):
            # Siccome la lista restituita dalla merge è in ordine crescente, la insert() entra
            # sempre nel caso dell'add_last() e ha complessità O(1)
            self.insert(copy.deepcopy(curr.element()))
            curr = merged_scoreboards._before(curr)

    def top(self, i=1):
        """
        Restituisce i migliori i score nello scoreboard. Complessità computazionale O(i).
        """
        best_scores = []
        # Scorre gli scores e li appende alla lista da restituire
        curr = self._l.last()
        while i > 0:
            best_scores.append(curr)
            curr = self._l._before(curr)
            i -= 1
        return best_scores

    def last(self, i=1):
        """
        Restituisce i peggiori i score nello scoreboard. Complessità computazionale O(i).
        """
        worst_scores = []
        # Scorre gli scores e li appende alla lista da restituire
        curr = self._l.first()
        while i > 0:
            worst_scores.append(curr)
            curr = self._l._after(curr)
            i -= 1
        return worst_scores
