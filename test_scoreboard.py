from datetime import date

from ScoreBoard import ScoreBoard


def test_empty_list_is_empty():
    """
    Analizza se lo scoreboard sia vuoto o meno.
    """
    s = ScoreBoard()
    s_empty = s.Is_empty()
    s.insert(s.Score("Armando", 4, date(2018, 10, 16)))
    s_not_empty = s.Is_empty()
    if s_empty and not s_not_empty:
        print("Test test_empty_list_is_empty passed")
    else:
        print("Test test_empty_list_is_empty failed")


def test_size():
    """
    Analizza la dimensione dello scoreboard nei casi vuoto e con contenuto.
    """
    s = ScoreBoard(3)
    empty_sz = s.size()
    s.insert(s.Score("Armando", 4, date(2018, 10, 16)))
    s.insert(s.Score("Armandino", 15, date(2018, 10, 15)))
    s.insert(s.Score("Armandone", 33, date(2018, 10, 15)))
    not_empty_sz = s.size()
    if empty_sz == 0 and not_empty_sz == 3:
        print("Test test_size passed")
    else:
        print("Test test_size failed")


def test_len():
    """
    Controlla la corretta dimensione massima dello scoreboard.
    """
    s = ScoreBoard(4)
    s1 = ScoreBoard()
    if len(s) == 4 and len(s1) == 10:
        print("Test test_len passed")
    else:
        print("Test test_len failed")


def test_insert():
    """
    Controlla l'inserimento nello scoreboard non pieno.
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 4, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 15, date(2018, 10, 15)))
    s.insert(s.Score("Armando2", 33, date(2018, 10, 15)))
    if s.size() == 3:
        print("Test test_insert passed")
    else:
        print("Test test_insert failed")


def test_worst_score_insert():
    """
    Controlla che non venga ammesso un inserimento di score a scoreboard pieno se peggiore di quelli presenti.
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 23, date(2018, 10, 15)))
    s.insert(s.Score("Armando2", 33, date(2018, 10, 15)))
    s.insert(s.Score("Armando2", 13, date(2018, 10, 15)))
    if s.size() == 3 and s._l.first().element()._score == 23:
        print("Test test_worst_score_insert passed")
    else:
        print("Test test_worst_score_insert failed")


def test_score_insert_at_full():
    """
    Analizza l'inserimento di uno score valido a scoreboard pieno, eliminando il peggiore.
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 23, date(2018, 10, 15)))
    s.insert(s.Score("Armando2", 33, date(2018, 10, 15)))
    s.insert(s.Score("Armando2", 89, date(2018, 10, 15)))
    if s.size() == 3 and s._l.first().element()._score == 33:
        print("Test test_score_insert_at_full passed")
    else:
        print("Test test_score_insert_at_full failed")


def test_score_insert_duplicate():
    """
    Analizza che non venga ammesso l'inserimento di score duplicati.
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 23, date(2018, 10, 15)))
    s.insert(s.Score("Armando2", 23, date(2018, 10, 15)))
    if s.size() == 2:
        print("Test test_score_insert_duplicate passed")
    else:
        print("Test test_score_insert_duplicate failed")


def test_merge():
    """
    Controlla che il merge di due scoreboard non vuoti non superi la dimensione massima consentita.
    """
    s = ScoreBoard(7)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armandone", 55, date(2018, 10, 15)))
    new_s = ScoreBoard(2)
    new_s.insert(new_s.Score("Armandino", 57, date(2018, 10, 15)))
    new_s.insert(new_s.Score("Armanduccio", 60, date(2018, 10, 15)))
    # print(s)
    # print(new_s)
    s.merge(new_s)
    # print(s)
    # print(new_s)
    # L'implementazione interna salva gli scoreboard in ordine crescente,
    # quindi la lista degli _score inernamente sarà:
    # [44, 55, 57, 60]
    if s.size() == 4 and \
            str(s._l.last().element()._score) == "60" and \
            str(s._l.first().element()._score) == "44" and \
            str(s._l.first()._node._next._element._score) == "55" and \
            str(s._l.first()._node._next._next._element._score) == "57":
        print("Test test_merge passed")
    else:
        print("Test test_merge failed")


def test_merge_larger():
    """
    Analizza il merge di due scoreboard non vuoti che supera la dimensione massima consentita
    """
    s = ScoreBoard(4)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))  # non inserito
    s.insert(s.Score("Armandone", 55, date(2018, 10, 15)))  # inserito
    new_s = ScoreBoard(6)
    new_s.insert(new_s.Score("Armandino", 57, date(2018, 10, 15)))  # inserito
    new_s.insert(new_s.Score("Armanduccio", 60, date(2018, 10, 15)))  # inserito
    new_s.insert(new_s.Score("Armandello", 42, date(2018, 10, 18)))  # non inserito
    new_s.insert(new_s.Score("Armandetto", 10, date(2018, 10, 18)))  # non inserito
    new_s.insert(new_s.Score("Armandastro", 73, date(2018, 10, 18)))  # inserito
    s.merge(new_s)
    if s.size() == 4 and \
            str(s._l.last().element()._score) == "73" and \
            str(s._l.first().element()._score) == "55" and \
            str(s._l.first()._node._next._element._score) == "57":
        print("Test test_merge_larger passed")
    else:
        print("Test test_merge_larger failed")


def test_duplicate_insert_merge():
    s = ScoreBoard(7)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 55, date(2018, 10, 15)))
    s.insert(s.Score("Armandello", 5, date(2018, 10, 15)))

    t = ScoreBoard(3)
    t.insert(t.Score("Arman", 4, date(2018, 10, 16)))
    t.insert(t.Score("Armand", 55, date(2018, 10, 15)))
    t.insert(t.Score("Armandello", 5, date(2018, 10, 15)))

    s.merge(t)
    if s.size() == 5:
        print("Test test_duplicate_insert_merge passed")
    else:
        print("Test test_duplicate_insert_merge failed")


def test_top_default():
    """
    Analizza la top() con parametro di default.
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 55, date(2018, 10, 15)))
    score_top = s.top()
    if score_top[0].element()._score == 55:
        print("Test test_top_default passed")
    else:
        print("Test test_top_default failed")


def test_top():
    """
    Analizza la top().
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 55, date(2018, 10, 15)))
    s.insert(s.Score("Armandello", 61, date(2018, 10, 16)))
    score_top = s.top(2)
    if score_top[0].element()._score == 61 and score_top[1].element()._score == 55:
        print("Test test_top passed")
    else:
        print("Test test_top failed")


def test_last_default():
    """
    Analizza la last() con parametro di default.
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 55, date(2018, 10, 15)))
    score_top = s.last()
    if score_top[0].element()._score == 44:
        print("Test test_last_default passed")
    else:
        print("Test test_last_default failed")


def test_last():
    """
    Analizza la last().
    """
    s = ScoreBoard(3)
    s.insert(s.Score("Armando", 44, date(2018, 10, 16)))
    s.insert(s.Score("Armando2", 55, date(2018, 10, 15)))
    s.insert(s.Score("Armandello", 5, date(2018, 10, 15)))
    score_top = s.last(2)
    if score_top[0].element()._score == 5 and score_top[1].element()._score == 44:
        print("Test test_last passed")
    else:
        print("Test test_last failed")


def test_top_last_empty():
    """
    Analizza top() e last() su scoreboard vuoto.
    """
    s = ScoreBoard(3)
    lasts = s.last()
    firsts = s.top()
    if len(lasts) == 1 and len(firsts) == 1 and lasts[0] is None and firsts[0] is None:
        print("Test test_top_last_empty passed")
    else:
        print("Test test_top_last_empty failed")


def run_test_scoreboard():
    test_empty_list_is_empty()
    test_insert()
    test_worst_score_insert()
    test_score_insert_at_full()
    test_score_insert_duplicate()
    test_merge()
    test_merge_larger()
    test_duplicate_insert_merge()
    test_top_default()
    test_last_default()
    test_top()
    test_last()
    test_top_last_empty()
    test_size()
    test_len()


if __name__ == "__main__":
    run_test_scoreboard()



