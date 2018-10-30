from CircularPositionalList import CircularPositionalList
from TdP_collections.list.positional_list import PositionalList

'''
Definizione dei metodi di test di unità della classe CircularPositionalList per i metodi
'''


def test_empty_list_is_empty():
    """
    Verifica che la lista sia vuota
    """
    cpl = CircularPositionalList()
    if cpl.Is_empty():
        print("Test test_empty_list_is_empty passed")
    else:
        print("Test test_empty_list_is_empty failed")


def test_full_list_is_empty():
    """
    Verifica che la lista non sia vuota
    """
    cpl = CircularPositionalList()
    cpl.add_last(42)
    cpl.add_last(48)
    cpl.add_last(55)
    cpl.add_last(54)
    cpl.add_first(13)
    # print(cpl)
    if not cpl.Is_empty() and str(cpl) == "13, 42, 48, 55, 54":
        print("Test test_full_list_is_empty passed")
    else:
        print("Test test_full_list_is_empty failed")


def test_empty_list_last():
    """
    Verifica last() su lista vuota
    """
    cpl = CircularPositionalList()
    if cpl.last() is None:
        print("Test test_empty_list_last passed")
    else:
        print("Test test_empty_list_last failed")


def test_empty_list_first():
    """
    Verifica che first() su lista vuota restituisca None
    """
    cpl = CircularPositionalList()
    if cpl.first() is None:
        print("Test test_empty_list_first passed")
    else:
        print("Test test_empty_list_first failed")


def test_first_and_last():
    """
    Verifica first() e last() su lista non vuota
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(5)
    _ = cpl.add_first(67)
    _ = cpl.add_first(5)
    _ = cpl.add_first(42)
    _ = cpl.add_last(88)
    if cpl.first().element() is 42 and cpl.last().element() is 88:
        print("Test test_first_and_last passed")
    else:
        print("Test test_first_and_last failed")


def test_empty_list_before_after():
    """
    Verifica che before(p) e after(p) in caso di predecessore mancante restituiscano None
    """
    cpl = CircularPositionalList()
    pos = cpl.add_last(33)
    if cpl.before(pos) is None and cpl.after(pos) is None:
        print("Test test_empty_list_before_after passed")
    else:
        print("Test test_empty_list_before_after failed")


def test_before_exception():
    """
    Verifica before(p) su una position non ammessa
    """
    cpl1 = CircularPositionalList()
    cpl2 = CircularPositionalList()
    pos = cpl2.add_last(33)
    _ = cpl1.add_last(1)
    _ = cpl1.add_last(2)
    try:
        cpl1.before(pos)
    except ValueError:
        print("Test test_before_exception passed")
        return
    print("Test test_before_exception failed")


def test_after_exception():
    """
    Verifica after(p) su una position non ammessa
    """
    cpl1 = CircularPositionalList()
    cpl2 = CircularPositionalList()
    pos = cpl2.add_last(33)
    _ = cpl1.add_last(1)
    _ = cpl1.add_last(2)
    try:
        cpl1.after(pos)
    except ValueError:
        print("Test test_after_exception passed")
        return
    print("Test test_after_exception failed")


def test_before_and_after():
    """
    Verifica after(p) e before(p) nel caso nominale, sia per position interne alla lista che per gli estremi
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(5)
    in2 = cpl.add_first(67)
    first = cpl.add_first(5)
    last = cpl.add_last(88)
    res_before = cpl.before(first)
    res_after = cpl.after(last)
    in2_after = cpl.after(in2)
    in2_before = cpl.before(in2)
    if res_before == 88 and res_after == 5 and in2_after == 5 and in2_before == 5:
        print("Test test_before_and_after passed")
    else:
        print("Test test_before_and_after failed")


def test_add_first():
    """
    Verifica l'inserimento in testa
    """
    cpl = CircularPositionalList()
    cpl.add_first(33)
    cpl.add_first(42)
    if not cpl.Is_empty() and cpl.first().element() == 42:
        print("Test test_add_first passed")
    else:
        print("Test test_add_first failed")


def test_add_last():
    """
    Verifica l'inserimento in coda
    """
    cpl = CircularPositionalList()
    cpl.add_last(33)
    cpl.add_last(42)
    if not cpl.Is_empty() and cpl.last().element() == 42:
        print("Test test_add_last passed")
    else:
        print("Test test_add_last failed")


def test_add_before():
    """
    Verifica l'inserimento di un elemento prima di una data position
    """
    cpl = CircularPositionalList()
    p = cpl.add_last(4)
    _ = cpl.add_last(10)
    # list is [10,4]
    pos = cpl.add_before(p, 42)
    # list is [10,42,4]
    if not cpl.Is_empty() and cpl.after(pos) == 4 and cpl.before(pos) == 10:
        print("Test test_add_before passed")
    else:
        print("Test test_add_before failed")


def test_add_after():
    """
    Verifica l'inserimento di un elemento dopo una data position
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(4)
    p = cpl.add_last(1)
    _ = cpl.add_last(10)
    # list is [4,1,10]
    pos = cpl.add_after(p, 42)
    # list is [4,1,42,10]
    if not cpl.Is_empty() and cpl.after(pos) == 10 and cpl.before(pos) == 1:
        print("Test test_add_after passed")
    else:
        print("Test test_add_after failed")


def test_wrong_position_add_before_after():
    """
    Verifica l'inserimento di un elemento prima/dopo una data position non valida
    """
    cpl = CircularPositionalList()
    pl = PositionalList()
    w = pl.add_last(5)
    try:
        cpl.add_before(w, 5)
    except ValueError:
        # print(e)
        try:
            cpl.add_after(w, 5)
        except ValueError:
            # print(e)
            print("Test test_wrong_position_add_before_after passed")
            return
    print("Test test_wrong_position_add_before_after failed")


def test_find():
    """
    Verifica find() con elemento presente o meno (se non presente restituisce None)
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(33)
    _ = cpl.add_last(56)
    pos1 = cpl.find(33)
    pos2 = cpl.find(555)
    if pos1.element() == 33 and pos2 is None:
        print("Test test_find passed")
    else:
        print("Test test_find failed")


def test_find_first_occurence():
    """
    Verifica la restituzione del primo risultato utile di find()
    """
    cp = CircularPositionalList()
    _ = cp.add_last(14)
    _ = cp.add_last(33)
    _ = cp.add_last(56)
    _ = cp.add_last(33)
    _ = cp.add_last(67)

    occ = cp.find(33)
    if occ.element() == 33:
        print("Test test_find_first_occurence passed")
    else:
        print("Test test_find_first_occurence failed")


def test_empty_list_is_sorted():
    """
    Verifica se una lista vuota è ordinata
    """
    # Se la lista è vuota restituisce True
    cpl = CircularPositionalList()
    try:
        res_b = cpl.Is_sorted()
    except BaseException as e:
        print(e)
        print("Test test_empty_list_is_sorted failed")
        return
    if res_b:
        print("Test test_empty_list_is_sorted passed")
    else:
        print("Test test_empty_list_is_sorted failed")


def test_is_sorted():
    """
    Verifica se una lista non vuota è ordinata
    """
    # First not ordered list
    fcpl = CircularPositionalList()
    _ = fcpl.add_last(10)
    _ = fcpl.add_first(7)
    _ = fcpl.add_first(5)
    _ = fcpl.add_first(10)
    first_b = fcpl.Is_sorted()
    # Second ascending order
    scpl = CircularPositionalList()
    _ = scpl.add_last(2)
    _ = scpl.add_last(4)
    _ = scpl.add_last(6)
    _ = scpl.add_last(8)
    _ = scpl.add_last(10)
    second_b = scpl.Is_sorted()
    if not first_b and second_b:
        print("Test test_is_sorted passed")
    else:
        print("Test test_is_sorted failed")


def test_replace_existing_position():
    """
    Verifica replace su una position esistente
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(9)
    list_obj.add_first(3)
    list_obj.add_last(0)
    pos = list_obj.add_first(5)
    old = list_obj.replace(pos, 100)
    if str(list_obj) == "100, 3, 9, 0" and old == 5:
        print("Test test_replace_existing_position passed")
    else:
        print("Test test_replace_existing_position failed")


def test_replace_illegal_type():
    """
    Verifica il replace con una position non ammessa
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(9)
    list_obj.add_first(3)
    try:
        list_obj.replace("Test sentence", 100)
    except TypeError:
        print("Test test_replace_illegal_type passed")
        return
    print("Test test_replace_illegal_type failed")


def test_replace_value_error():
    """
    Verifica il replace con una position di un altro container
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(9)
    list_obj.add_first(3)
    o = CircularPositionalList()
    position = o.add_first(99)
    try:
        list_obj.replace(position, 100)
    except ValueError:
        print("Test test_replace_value_error passed")
        return
    print("Test test_replace_value_error failed")


def test_empty_list_delete(p):
    """
    Verifica la cancellazione da una lista vuota
    """
    # p appartiene ad un'altra lista causa exception
    list_obj = CircularPositionalList()
    right_p = list_obj.add_last(42)
    try:
        list_obj.delete(p)
    except ValueError:
        # print(e)
        pass
    list_obj.delete(right_p)
    # Proviamo ad eliminare di nuovo right_p causa exception ValueError perchè il nodo è None
    try:
        list_obj.delete(right_p)
    except ValueError:
        print("Test test_empty_list_delete passed")
        return
    print("Test test_empty_list_delete failed")


def test_delete_existing_head():
    """
    Verifica la cancellazione dalla lista della position head
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(7)
    list_obj.add_first(9)
    list_obj.add_first(3)
    pos = list_obj.add_first(10)
    list_obj.delete(pos)
    if str(list_obj) == "3, 9, 7":
        print("Test test_delete_existing_head passed")
    else:
        print("Test test_delete_existing_head failed")


def test_delete_existing_tail():
    """
    Verifica la cancellazione dalla lista della position tail
    """
    list_obj = CircularPositionalList()
    pos = list_obj.add_first(7)
    list_obj.add_first(9)
    list_obj.add_first(3)
    list_obj.add_first(10)
    list_obj.delete(pos)
    if str(list_obj) == "10, 3, 9":
        print("Test test_delete_existing_tail passed")
    else:
        print("Test test_delete_existing_tail failed")


def test_delete_existing_middle():
    """
    Verifica la cancellazione dalla lista di una position generica
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(7)
    list_obj.add_first(9)
    pos = list_obj.add_first(3)
    list_obj.add_first(10)
    list_obj.delete(pos)
    if str(list_obj) == "10, 9, 7":
        print("Test test_delete_existing_middle passed")
    else:
        print("Test test_delete_existing_middle failed")


def test_empty_list_clear():
    """
    Verifica clear su una lista vuota, non deve rilanciare eccezioni
    """
    # non deve lanciare eccezioni nè restituire qualcosa
    cpl = CircularPositionalList()
    try:
        cpl.clear()
    except BaseException as e:
        print(e)
        print("Test test_empty_list_clear failed")
        return
    print("Test test_empty_list_clear passed")


def test_clear():
    """
    Verifica clear su una lista non vuota, non deve rilanciare eccezioni
    """
    cpl = CircularPositionalList()
    pos = cpl.add_last(5)
    _ = cpl.add_first(67)
    _ = cpl.add_first(5)
    _ = cpl.add_first(42)
    _ = cpl.add_last(88)
    try:
        cpl.clear()
    except BaseException as e:
        print(e)
    if cpl.Is_empty():
        try:
            cpl.before(pos)
        except ValueError:
            print("Test test_clear passed")
    else:
        print("Test test_clear failed")


def test_empty_list_count():
    """
    Verifica count su una lista vuota
    """
    cpl = CircularPositionalList()
    if cpl.count(5) == 0 and cpl.count("ppp") == 0:
        print("Test test_empty_list_count passed")
    else:
        print("Test test_empty_list_count failed")


def test_count():
    """
    Verifica il conteggio di occorrenze di un elemento presente o meno
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(5)
    _ = cpl.add_first(42)
    _ = cpl.add_first(42)
    _ = cpl.add_first(1)
    _ = cpl.add_first(42)
    _ = cpl.add_last(88)
    if cpl.count(42) == 3 and cpl.count(33) == 0 and cpl.count(5) == 1:
        print("Test test_count passed")
    else:
        print("Test test_count failed")


def test_empty_list_reverse():
    """
    Verifica reverse su una lista vuota
    """
    cpl = CircularPositionalList()
    # lista vuota lancia exception AttributeError
    try:
        cpl.reverse()
    except AttributeError:
        print("Test test_empty_list_reverse passed")
        return
    print("Test test_empty_list_reverse failed")


def test_reverse():
    """
    Verifica reverse su una lista non vuota
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(5)
    _ = cpl.add_last(42)
    _ = cpl.add_last(10)
    _ = cpl.add_last(1)
    _ = cpl.add_last(77)
    cpl.reverse()
    if str(cpl) == "77, 1, 10, 42, 5":
        print("Test test_reverse passed")
    else:
        print("Test test_reverse failed")


def test_copy():
    """
    Verifica la funzionalità di copia della lista
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(42)
    _ = cpl.add_last(10)
    _ = cpl.add_last(1)
    _ = cpl.add_last(77)
    cpl_copy = cpl.copy()
    if str(cpl) == str(cpl_copy) and isinstance(cpl, CircularPositionalList) and \
            isinstance(cpl_copy, CircularPositionalList) and cpl is not cpl_copy:
        print("Test test_copy passed")
    else:
        print("Test test_copy failed")


'''
Definizione dei metodi di test di unità della classe CircularPositionalList per gli operatori
'''


def test_len():
    """
    Verifica l'operatore len
    """
    cpl = CircularPositionalList()
    if len(cpl) == 0:
        _ = cpl.add_last(42)
        _ = cpl.add_last(10)
        _ = cpl.add_last(1)
        _ = cpl.add_last(77)
        if len(cpl) == 4:
            print("Test test_len passed")
        else:
            print("Test test_len failed")


def test_in():
    """
    Verifica l'operatore in
    """
    cpl = CircularPositionalList()
    spl = CircularPositionalList()
    p1 = cpl.add_last(42)
    p2 = cpl.add_last(10)
    p3 = cpl.add_last(1)
    p4 = cpl.add_last(77)
    if p1 in cpl and p2 in cpl and p3 in cpl and p4 in cpl and p1 not in spl:
        print("Test test_in passed")
    else:
        print("Test test_in failed")


def test_get_item():
    """
    Verifica l'operatore di accesso x[p]
    """
    cpl = CircularPositionalList()
    p1 = cpl.add_last(42)
    p2 = cpl.add_last(10)
    p3 = cpl.add_last(1)
    if cpl[p1] == 42 and cpl[p2] == 10 and cpl[p3] == 1:
        try:
            _ = cpl["illegal_item"]
        except TypeError:
            print("Test test_get_item passed")
    else:
        print("Test test_get_item failed")


def test_add():
    """
    Verifica l'operatore +
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last("This")
    _ = cpl.add_last("is")
    _ = cpl.add_last("a")
    _ = cpl.add_last("list")

    scpl = CircularPositionalList()
    _ = scpl.add_last("and")
    _ = scpl.add_last("I")
    _ = scpl.add_last("modify")
    _ = scpl.add_last("it")
    returned_list = cpl + scpl
    # print(str(returned_list))
    if len(returned_list) == 8 and returned_list.pop(7) == "it":
        print("Test test_add passed")
    else:
        print("Test test_add failed")


def test_set_item():
    """
    Verifica l'operatore di modifica x[p] = e
    """
    cpl = CircularPositionalList()
    p1 = cpl.add_last(42)
    p2 = cpl.add_last(10)
    p3 = cpl.add_last(1)
    try:
        cpl[p1] = 2
        cpl[p2] = 3
        cpl[p3] = 4
    except BaseException as e:
        print(e)
    if cpl[p1] == 2 and cpl[p2] == 3 and cpl[p3] == 4:
        print("Test test_set_item passed")
    else:
        print("Test test_set_item failed")


def test_del():
    """
    Verifica l'operatore del
    """
    cpl = CircularPositionalList()
    p1 = cpl.add_last(42)
    p2 = cpl.add_last(10)
    p3 = cpl.add_last(1)
    try:
        del cpl[p1]
        del cpl[p2]
        del cpl[p3]
    except BaseException as e:
        print(e)
    if cpl.Is_empty():
        print("Test test_del passed")
    else:
        print("Test test_del failed")


def test_iter():
    """
    Generatore che restituisce gli elementi della lista a partire da quello che è
    identificato come primo fino a quello che è identificato come ultimo
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(42)
    _ = cpl.add_last(10)
    _ = cpl.add_last(1)
    support_list = list()
    for f in cpl:
        support_list.append(f)
    if support_list[0] == 42 and support_list[2] == 1:
        print("Test test_iter passed")
    else:
        print("Test test_iter failed")


def test_str():
    """
    Verifica l'operatore str
    """
    cpl = CircularPositionalList()
    _ = cpl.add_last(42)
    _ = cpl.add_last(10)
    _ = cpl.add_last(1)
    if str(cpl) == "42, 10, 1":
        print("Test test_str passed")
    else:
        print("Test test_str failed")


def run_test_base():
    cpl = CircularPositionalList()
    position = cpl.add_last(4)

    test_empty_list_is_empty()
    test_full_list_is_empty()
    test_empty_list_first()
    test_empty_list_last()
    test_empty_list_before_after()
    test_after_exception()
    test_before_exception()
    test_add_first()
    test_add_last()
    test_add_before()
    test_add_after()
    test_wrong_position_add_before_after()
    test_before_and_after()
    test_first_and_last()
    test_empty_list_is_sorted()
    test_is_sorted()
    test_replace_existing_position()
    test_replace_illegal_type()
    test_replace_value_error()
    test_empty_list_delete(p=position)
    test_empty_list_clear()
    test_delete_existing_head()
    test_delete_existing_middle()
    test_delete_existing_tail()
    test_clear()
    test_empty_list_count()
    test_count()
    test_empty_list_reverse()
    test_reverse()
    test_copy()
    test_find()
    test_find_first_occurence()
    # print('\n')
    test_len()
    test_in()
    test_get_item()
    test_set_item()
    test_add()
    test_del()
    test_iter()
    test_str()


if __name__ == '__main__':
    run_test_base()
