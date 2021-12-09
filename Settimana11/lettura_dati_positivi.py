# Leggo valori interi positivi da tastiera

def leggi_positivo():
    ok = False
    while not ok:
        try:
            s = input('Numero: ')
            n = int(s)
            ok = True
        except ValueError:
            print("Valore non valido")

    if n <= 0:
        raise ValueError(f'Il valore {n} non è positivo')
    return n


def main():
    valori = []
    for i in range(5):
        try:
            valori.append(leggi_positivo())
        except ValueError as ex:
            valori.append(0)
            # print(str(ex))
    print(valori)


main()
