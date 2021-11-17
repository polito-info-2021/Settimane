# Esercizio 6.3

def main():
    ripeti = True
    while ripeti:
        reddito = int(input("Reddito: "))
        n_figli = int(input("Numero di figli: "))

        if reddito != -1 and n_figli != -1:
            sussidio = calcola_sussidio(reddito, n_figli)
            print(f'Con un reddito {reddito} e {n_figli} figli hai diritto al sussidio di {sussidio}')
        else:
            ripeti = False


def calcola_sussidio(reddito, n_figli):
    if reddito < 20000:
        sussidio = 2000 * n_figli
    elif reddito < 30000 and n_figli >= 2:  # sottinteso >=20000
        sussidio = 1500 * n_figli
    elif (30000 <= reddito < 40000) and n_figli >= 3:  # sottinteso >=30000  SBAGLIATO non posso assumerlo perché la condizione precedente è complessa
        sussidio = 1000 * n_figli
    else:
        sussidio = 0
    return sussidio


main()  # esegui la funzione main, cioè il programma principale
