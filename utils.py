from CircularPositionalList import CircularPositionalList
import copy


def bubblesorted(item):
    """
    Implementazione della funzione di ordinamento tramite metodo built-in di che usa l'algoritmo di ordinamento 'Timsort'.
    Complessità computazionale O(nlogn).
    :param item: lista da ordinare
    :return to_order_list: lista contenente la lista di ingresso dopo averla ordinata
    """
    to_order_list = []
    for x in item:
        to_order_list.append(x)
    to_order_list.sort()
    for x in to_order_list:
        yield x


def bubblesort(l):
    """
    Implementazione dell'algoritmo di ordinamento 'Bubblesort'. Complessità computazionale O(n²). Nell'implementazione
    della consegna si è però preferito l'ordinameneto con il metodo predefinito di python per il sorting che sfrutta
    l'algoritmo TimSort a complessità O(nlogn) nel caso peggiore, e quindi più efficiente.
    :param l: lista da ordinare in loco
    :return:
    """
    scambio = True
    while scambio:
        scambio = False
        first = l.first()
        for i in range(0, len(l)-1):
            second = l._after(first)
            if l[first] >= l[second]:
                appoggio = l[first]
                l[first] = l[second]
                l[second] = appoggio
                scambio = True
            first = l._after(first)


def merge(list1, list2) -> CircularPositionalList:
    """
    Implementazione dell'algoritmo di merge di due liste passate come parametri di ingresso.
    Complessità computazionale O(n).
    :param list1: prima lista da inserire nell'unione, preordinata
    :param list2: seconda lista da inserire nell'unione, preordinata
    :return list_to_return: lista risultante dall'unione, preservando l'ordinamento e la dimensione massima della prima lista
    """
    # Precondizione liste ordinate, controllare solo se le liste sono ordinate
    if list1.Is_empty() and list2.Is_empty():       # Controllo se la lista1 è vuota e se la lista2 è ordinata
        raise ValueError('both lists are empty')
    elif list1.Is_empty():
        return list2
    elif list2.Is_empty():                          # Controllo se la lista2 è vuota e se la lista1 è ordinata
        return list1
    else:
        index1 = 0
        index2 = 0
        list_to_return = CircularPositionalList()
        node1 = list1.first()
        node2 = list2.first()
        while index2 < len(list2) and index1 < len(list1):
            if list1[node1] >= list2[node2]:
                list_to_return.add_last(copy.deepcopy(list2[node2]))
                node2 = list2._after(node2)
                index2 += 1
            else:
                list_to_return.add_last(copy.deepcopy(list1[node1]))
                node1 = list1._after(node1)
                index1 += 1
        while index2 < len(list2):
            list_to_return.add_last(copy.deepcopy(list2[node2]))
            node2 = list2._after(node2)
            index2 += 1
        while index1 < len(list1):
            list_to_return.add_last(copy.deepcopy(list1[node1]))
            node1 = list1._after(node1)
            index1 += 1
        return list_to_return
