from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):
    """
    La classe implementa una sequenza la cui rappresentazione interna è basata su una PositionalList di cui eredita
    numerosi comportamenti e l'implementazione doppiamente linkata. Per ottenere comportamento circolare sono aggiunti
    due attributi che mantengono i riferimenti alla position in testa e in coda alla lista. Per semplicità si consideri
    la sequenza come contenente elementi omogenei sui quali è definita una relazione d'ordine. Come ulteriore
    precondizione, si considerino come ordinate solo le liste che rispettano ordinamento ascendente.
    """

    def __init__(self):
        """
        _head position che indica il primo elemento della lista
        _tail position che indica l'ultimo elemento della lista
        _size indica la dimensione della lista
        """
        self._head = None
        self._tail = None
        self._size = 0

    def _make_position(self, node):
        """
        Override del metodo della classe padre per rispettare la nostra implementazione. Complessità computazionale O(1).
        """
        return self.Position(self, node)

    def add_first(self, e):
        """
        Aggiunge un elemento in testa alla lista. Complessità computazionale O(1).
        :param e: elemento da aggiungere
        :return: position contenente l'elemento aggiunto
        """
        if self.Is_empty():
            # Inserimento in caso di lista vuota
            node_to_add = self._Node(e, None, None)
            # Collego il nodo a se stesso
            node_to_add._next = node_to_add
            node_to_add._prev = node_to_add
            # Creo la position a cui far puntare head e tail
            pos_to_add = self._make_position(node_to_add)
            self._tail = pos_to_add
            self._head = pos_to_add
            self._size += 1
        else:
            # Inserimento in caso di lista con almeno una position
            predecessor = self._tail
            successor = self._head
            # Riutilizzo dell'interfaccia di inserimento della classe padre
            pos_to_add = self._insert_between(e, predecessor._node, successor._node)
            self._head = pos_to_add
        return pos_to_add

    def add_last(self, e):
        """
        Aggiunge un elemento in coda alla lista. Complessità computazionale O(1).
        :param e: elemento da aggiungere
        :return: position contenente l'elemento aggiunto
        """
        if self.Is_empty():
            # Inserimento in caso di lista vuota#inserimento in caso di lista vuota
            node_to_add = self._Node(e, None, None)
            # Collego il nodo a se stesso
            node_to_add._next = node_to_add
            node_to_add._prev = node_to_add
            # Creo la position a cui far puntare head e tail
            pos_to_add = self._make_position(node_to_add)
            self._tail = pos_to_add
            self._head = pos_to_add
            self._size += 1
        else:
            # Inserimento in caso di lista con almeno una position
            predecessor = self._tail
            successor = self._head
            # Riutilizzo dell'interfaccia di inserimento della classe padre
            pos_to_add = self._insert_between(e, predecessor._node, successor._node)
            self._tail = pos_to_add
        return pos_to_add

    def add_before(self, p, e):
        """
        Inserisce un elemento prima di una data position. Complessità computazionale O(1).
        :param p: position a cui far precedere l'elemento da inserire
        :param e: elemento da inserire nella lista
        :return: position contenente l'elemento aggiunto
        """
        # Controllo della validità della position fornita
        _ = self._validate(p)
        # Caso di inserimento in testa
        if p == self._head:
            pos_to_add = self.add_first(e)
        else:
            # Inserimento generico riutilizzando l'interfaccia della classe padre
            pos_to_add = self._insert_between(e, self._before(p)._node, p._node)
        return pos_to_add

    def add_after(self, p, e):
        """
        Inserisce un elemento dopo una data position. Complessità computazionale O(1).
        :param p: position a cui far seguire l'elemento da inserire
        :param e: elemento da inserire nella lista
        :return: position contenente l'elemento aggiunto
        """
        # Controllo della validità della position fornita
        _ = self._validate(p)
        # Caso di inserimento in coda
        if p == self._tail:
            pos_to_add = self.add_last(e)
        else:
            # Inserimento generico riutilizzando l'interfaccia della classe padre
            pos_to_add = self._insert_between(e, p._node, self._after(p)._node)
        return pos_to_add

    def first(self):
        """
        Restituisce la position identificata come prima nella lista. Complessità computazionale O(1).
        :return: position associata al primo elemento, o None se la lista è vuota
        """
        if self._size == 0:
            return None
        else:
            return self._head

    def last(self):
        """
        Restituisce la position identificata come ultima nella lista. Complessità computazionale O(1).
        :return: position associata all'ultimo elemento, o None se la lista è vuota
        """
        if self._size == 0:
            return None
        else:
            return self._tail

    def _before(self, p):
        """
        Restituisce la position che precede l'argomento passato. Interfaccia non pubblica per lo scorrimento della lista
        per position. Complessità computazionale O(1).
        :param p: position di cui trovare il predecessore
        :return: position che precede p
        """
        # Non è necessaria la validazione poiché avviene nella chiamata all'interfaccia della classe padre
        if self.Is_empty():
            return None
        else:
            return super().before(p)

    def before(self, p):
        """
        Restituisce l'elemento nella position che precede l'argomento passato. Complessità computazionale O(1).
        :param p: position di cui trovare il predecessore
        :return: elemento contenuto nella position predecessore di p
        """
        # Non è necessaria la validazione poiché avviene nella chiamata all'interfaccia della classe padre
        if self.Is_empty() or self._size == 1:
            return None
        else:
            return super().before(p).element()

    def _after(self, p):
        """
        Restituisce la position che succede l'argomento passato. Interfaccia non pubblica per lo scorrimento della lista
        per position. Complessità computazionale O(1).
        :param p: position di cui trovare il successore
        :return: position che segue p
        """
        if self.Is_empty():
            return None
        else:
            return super().after(p)

    def after(self, p):
        """
        Restituisce l'elemento nella position che succede l'argomento passato. Complessità computazionale O(1).
        :param p: position di cui trovare il successore
        :return: elemento contenuto nella position successore di p
        """
        # Non è necessaria la validazione poiché avviene nella chiamata all'interfaccia della classe padre
        if self.Is_empty() or self._size == 1:
            return None
        else:
            return super().after(p).element()

    def Is_empty(self):
        """
        Verifica se la lista è vuota. Complessità computazionale O(1).
        :return: True se la lista è vuota, altrimenti False
        """
        return self._size == 0

    def Is_sorted(self):
        """
        Verifica che gli elementi della lista siano ordinati in senso crescente. Complessità computazionale O(_size).
        :return: True se la lista è ordinata, False altrimenti
        """
        # Attenzione, come precondizione si suppone che la lista sia ordinata se e solo se in ordine crescente
        current_p = self._head
        next_p = self._after(current_p)
        # Scorre la lista fin quando non ritorna alla testa e verifica la condizione di ordinamento su coppie di elemnti
        while next_p != self._head:
            if current_p.element() <= next_p.element():
                current_p = self._after(current_p)
                next_p = self._after(next_p)
            else:
                return False
        return True

    def find(self, e):
        """
        Verifica se un elemento è presente nella lista. Complessità computazionale O(_size).
        :param e: elemento da ricercare
        :return: position contenente la prima occorrenza dell'elemento e se trovato, None altrimenti
        """
        # Scorre la lista verificando la condizione di uguaglianza fra gli elementi
        for elem in self:
            if e == elem:
                return self._make_position(self._Node(elem, None, None))
        return None

    def delete(self, p):
        """
        Cancella una position dalla lista. Complessità computazionale O(1).
        :param p: position da eliminare
        :return: elemento della position eliminata
        """
        # Controllo su cancellazione della testa
        if p == self._head:
            self._head = self._after(p)
        # Controllo su cancellazione della coda
        elif p == self._tail:
            self._tail = self._before(p)
        # Cancellazione di un elemento generico usando l'interfaccia della classe padre che si occupa di invalidare
        # la position da cancellare. In questa fase viene anche validata la position
        return super().delete(p)

    def clear(self):
        """
        Elimina tutte le position della lista. Complessità computazionale O(_size).
        """
        # Scorre la lista e cancella la position corrente usando l'interfaccia della classe padre che si occuperà anche
        # di invalidare la position corrente
        current = self._head
        while self._size > 0:
            next_position = self._after(current)
            self.delete(current)
            current = next_position

    def replace(self, p, e):
        """
        Sostituisce l'elemento in position p con quello passato per argomento. Complessità computazionale O(1).
        :param p: position di cui sostituire l'elemento
        :param e: elemento da sostituire
        :return: vcchio elemento sostituito
        """
        # Validazione della position effettuata a livello superiore tramite l'interfaccia offerta dalla classe padre
        return super().replace(p, e)

    def count(self, e):
        """
        Conta il numero di occorrenze per un dato elemento. Complessità computazionale O(_size).
        :param e: elemento di cui contare le occorrenze
        :return: numero di occorrenze dell'elemento richiesto
        """
        # Scorre la lista contando le occorrenze di e, in caso di nessuna corrispondenza restituisce 0
        counter = 0
        for x in self:
            if x == e:
                counter += 1
        return counter

    def reverse(self):
        """
        Inverte l'ordine degli elementi nella lista. Complessità computazionale O(_size).
        """
        # Scorre la lista invertendo per ogni nodo contenuto nelle position i riferimenti al suo successore e predecessore
        prev_head = self._head
        prev_tail = self._tail
        curr = self._head
        temp_next = curr._node._next
        for i in range(0, self._size):
            curr._node._next = curr._node._prev
            curr._node._prev = temp_next
            curr = self._before(curr)
            temp_next = curr._node._next
        self._head = prev_tail
        self._tail = prev_head

    def copy(self):
        """
        Restituisce una nuova lista copia esatta della lista corrente. Complessità computazionale O(_size).
        :return: CircularPositionalList copia della corrente lista
        """
        # Scorre la lista effettuandone una deep copy
        list_obj = CircularPositionalList()
        for x in self:
            list_obj.add_last(x)
        return list_obj

    def __len__(self):
        """
        Restituisce la dimensione della lista. Complessità computazionale O(1).
        :return: dimensione della lista
        """
        return self._size

    def __iter__(self):
        """
        Generatore che permette di iterare sugli elementi della lista. Complessità computazionale O(1) per ogni yield.
        """
        current = self._head
        for i in range(0, self._size):
            yield current.element()
            current = self._after(current)

    def __add__(self, l2):
        """
        Operatore di somma che concatena due liste. Complessità computazionale O(_size+l2._size).
        :param l2: lista da concatenare alla corrente
        :return: lista contenente gli elementi della lista corrente e di quella passata per argomento
        """
        # Scorre separatamente le due liste e ne appende gli elementi alla lista da restituire
        list_to_ret = list()
        for x in self:
            list_to_ret.append(x)
        for x2 in l2:
            list_to_ret.append(x2)
        return list_to_ret

    def __contains__(self, item):
        """
        Operatore di appartenenza. Complessità computazionale O(1).
        :param item: position di cui verificare l'appartenenza alla lista
        :return: True se item appartiene alla lista, False altrimenti
        """
        try:
            _ = self._validate(item)
        except BaseException:
            # print(e)
            return False
        return True

    def __getitem__(self, item):
        """
        Operatore di accesso agli elementi. Commplessità computazionale O(1).
        :param item: position di cui retituire l'elemento
        :return: elemento associato alla position item
        """
        # È sufficiente la validazione della position per avere certezza della presenza di item
        return self._validate(item)._element

    def __setitem__(self, key, value):
        """
        Operatore di modifica. Cambia l'elemento della position key con value. Complessità computazionale O(1).
        :param key: position di cui modificare l'elemento
        :param value: nuovo elemento da inserire in key
        """
        self.replace(key, value)

    def __delitem__(self, key):
        """
        Operatore di cancellazione. Elimina una position. Complessità computazionale O(1).
        :param key: position da cancellare
        """
        self.delete(key)

    def __str__(self):
        """
        Operatore di trasformazione in stringa. Complessità computazionale O(_size).
        :return: rappresentazione in stringa di caratteri della lista
        """
        string = ''
        for elem in self:
            string += str(elem)+', '
        return string[:-2]
