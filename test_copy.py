from CircularPositionalList import CircularPositionalList


def run_test_copy():
    l_uno = CircularPositionalList()
    _ = l_uno.add_last(42)
    _ = l_uno.add_last(1)

    l_due = l_uno.copy()
    print('%-25s|%-25s' % (str(l_uno), str(l_due)))
    print('%-25s|%-25s' % (str(l_uno.first().element()), str(l_due.first().element())))
    print('%-25s|%-25s' % (str(l_uno.last().element()), str(l_due.last().element())))
    print('%-25s|%-25s' % (str(l_uno.before(l_uno.first())), str(l_due.before(l_due.first()))))
    print('%-25s|%-25s' % (str(l_uno.after(l_uno.first())), str(l_due.after(l_due.first()))))
    print('%-25s|%-25s' % (str(l_uno.Is_empty()), str(l_due.Is_empty())))
    print('%-25s|%-25s' % (str(l_uno.Is_sorted()), str(l_due.Is_sorted())))
    print('%-25s|%-25s' % (str(l_uno.add_first(5).element()), str(l_due.add_first(5).element())))
    print('%-25s|%-25s' % (str(l_uno.add_last(50).element()), str(l_due.add_last(50).element())))
    print('%-25s|%-25s' % (str(l_uno.add_before(l_uno.first(), 4).element()), str(l_due.add_before(l_due.first(), 4).element())))
    print('%-25s|%-25s' % (str(l_uno.add_after(l_uno.first(), 15).element()), str(l_due.add_after(l_due.first(), 15).element())))
    print('%-25s|%-25s' % (str(l_uno.find(5).element()), str(l_due.find(5).element())))
    print('%-25s|%-25s' % (str(l_uno), str(l_due)))
    print('%-25s|%-25s' % (str(l_uno.replace(l_uno.first(), 78)), str(l_due.replace(l_due.first(), 78))))
    print('%-25s|%-25s' % (str(l_uno), str(l_due)))
    print('%-25s|%-25s' % (str(l_uno.delete(l_uno.first())), str(l_due.delete(l_due.first()))))
    print('%-25s|%-25s' % (str(l_uno), str(l_due)))
    print('%-25s|%-25s' % (str(l_uno.count(42)), str(l_due.count(42))))
    l_uno.reverse()
    l_due.reverse()
    print('%-25s|%-25s' % (str(l_uno), str(l_due)))
    print('%-25s|%-25s' % (str(l_uno.copy()), str(l_due.copy())))
    l_uno.clear()
    l_due.clear()
    print('%-25s|%-25s' % (str(l_uno), str(l_due)))


if __name__ == "__main__":
    run_test_copy()
