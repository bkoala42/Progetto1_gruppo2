from CircularPositionalList import CircularPositionalList
from utils import bubblesorted, merge, bubblesort


def test_bubblesorted():
    """
    Verfica la funzione di ordinamento sia per input vuoto che non.
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(7)
    list_obj.add_first(9)
    list_obj.add_first(3)
    list_obj.add_first(10)
    ordered = []
    for x in bubblesorted(list_obj):
        ordered.append(x)
    if str(ordered) == "[3, 7, 9, 10]":
        print("Test test_bubblesorted_not_empty passed")
    else:
        print("Test test_bubblesorted_not_empty failed")


def test_bubblesort():
    """
    Verifica la funzione di ordinamento con bubblesort, sia per input vuoto che non.
    """
    list_obj = CircularPositionalList()
    list_obj.add_first(7)
    list_obj.add_first(9)
    list_obj.add_first(3)
    list_obj.add_first(10)
    bubblesort(list_obj)
    if str(list_obj) == "3, 7, 9, 10":
        print("Test test_bubblesort passed")
    else:
        print("Test test_bubblesort failed")


def test_merge():
    """
    Verifica la funzione di unione merge su input ordinati.
    :return:
    """
    l1 = CircularPositionalList()
    l1.add_first(23)
    l1.add_first(21)
    l1.add_first(10)
    l2 = CircularPositionalList()
    l2.add_first(30)
    l2.add_first(21)
    l2.add_first(7)
    l3 = merge(l1, l2)

    fl = CircularPositionalList()
    fl.add_last(44)
    fl.add_last(55)
    sl = CircularPositionalList()
    sl.add_last(57)
    sl.add_last(60)
    merged_list = merge(fl, sl)

    if l3.Is_sorted() and merged_list.Is_sorted():
        print("Test test_merge passed")
    else:
        print("Test test_merge failed")


def test_merge_deep_copy():
    l1 = CircularPositionalList()
    l2 = CircularPositionalList()
    l1.add_last([2, 5, 6])
    l2.add_last([66, 6, 0])
    m = merge(l1, l2)
    l1.first().element().append(42)

    if len(m.first().element()) == 3:
        print("Test test_merge_deep_copy passed")
    else:
        print("Test test_merge_deep_copy failed")


def run_test_algo():
    test_bubblesorted()
    test_bubblesort()
    test_merge()
    test_merge_deep_copy()


if __name__ == "__main__":
    run_test_algo()
