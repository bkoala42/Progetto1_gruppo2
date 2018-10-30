from CircularPositionalList import CircularPositionalList


def leggi(stringa):
    tmp = None
    while not isinstance(tmp, int):
        try:
            tmp = int(input(stringa))
        except BaseException as exp:
            print("Inserisci un intero!\n")
    return tmp


def run_interactive_test():

    print("Test Interattivo.")
    print("Si presuppone che il software venga utilizzato mediante input appropriati.\n")
    print("Menù:")
    print("1)crea una lista;")
    print("2)inserisci un elemento in testa;")
    print("3)inserisci un elemento in coda;")
    print("4)preleva primo elemento;")
    print("5)preleva ultimo elemento;")
    print("6)stampa lista;")
    print("7)svuota la lista;")
    print("8)elimina l'ultimo elemento inserito;")
    print("9)cerca un elemento;")
    print("10)esci dal test.\n")

    lista = None
    scelta = None
    pos = None

    while(True):
        while (not isinstance(scelta, int)) or (isinstance(scelta, int) and (scelta <= 0 or scelta >= 11)):
            try:
                scelta = int(input("Inserisci una scelta (intero): "))
                if scelta <= 0 or scelta >= 11:
                    print("La scelta deve essere un intero compreso tra 1 e 10.")
            except BaseException as exp:
                print("Inserisci un intero!\n")

        if(scelta == 1):
            if(lista == None):
                lista =  CircularPositionalList()
            else:
                print("Lista già creata.")

        if(scelta == 2):
            tmp = leggi("Fornire l'intero da inserire in testa alla lista:\n")
            pos = lista.add_first(tmp)
            print("La lista è: "+ str(lista))
            print("La size della lista è: "+ str(len(lista)))
            if not (len(lista) == 0 or len(lista) == 1):
                print("L'elemento before di {0} è: {1}".format(pos.element(), lista.before(pos)))
                print("L'elemento after di {0} è: {1}".format(pos.element(), lista.after(pos)))

        if (scelta == 3):
            tmp = leggi("Fornire l'intero da inserire in coda alla lista:\n")
            lista.add_last(tmp)
            print("La lista è: " + lista.__str__())
            print("La size della lista è: " + str(len(lista)))

        if (scelta == 4):
            print("La lista è: "+lista.__str__())

        if (scelta == 5):
            if len(lista) == 0:
                print("Lista vuota. Impossibile prelevare il primo elemento")
            print(lista.first())

        if(scelta == 6):
            if len(lista) == 0:
                print("Lista vuota. Impossibile prelevare l'ultimo elemento")
            print(lista.last())

        if (scelta == 7):
            if len(lista) == 0:
                print("Lista già vuota")
            lista.clear()
            print("Lista svuotata")

        if (scelta == 8):
            if (pos in lista):
                print("Rimozione dell'elemento: " + str(pos.element()))
                lista.delete(pos)
            else:
                print("Niente da rimuovere.")

        if (scelta == 9):
            tmp = leggi("Inserisci l'elemento da ricercare:")
            pos1 = lista.find(tmp)
            if pos == None:
                print("Elemento non trovato.")
            else:
                print("Elemento trovato.")

        if (scelta == 10):
            print("Per maggiori informazioni controllare il file di test verifica.py")
            exit(0)

        try:
            scelta = int(input("Inserisci una scelta (intero):"))
            if scelta <= 0 or scelta >= 11:
                print("La scelta deve essere un intero compreso tra 1 e 10.")
        except BaseException as exp:
            print("Inserisci un intero!\n")


if __name__ == '__main__':
    run_interactive_test()
