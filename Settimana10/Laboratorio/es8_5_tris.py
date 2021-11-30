# Laboratorio 08, Esercizio 5: Tris

# griglia = tabella 3x3, in cui ciascuna cella conterrà ' ', 'X', 'O'
# Alternative: '', 'X', 'O' /// 0, 1, 2 /// None, 'X', 'O' /// ....

def main():
    griglia = crea_griglia()

    giocatore1 = True
    finito = False
    turni = 0
    while not finito and turni < 9:
        if giocatore1:
            print("Giocatore 1 (X)")
            simbolo = 'X'
        else:
            print("Giocatore 2 (O)")
            simbolo = 'O'

        stampa_griglia(griglia)

        # formato di ingresso: 23  (riga e colonna senza separatori, valori 1, 2, 3)
        #  11 12 13
        #  21 22 23
        #  31 32 33
        mossa = input("Inserisci la tua mossa (rc): ")
        # TODO: CONTROLLA ERRORI
        r = int(mossa[0]) - 1  # da "2" a 1
        c = int(mossa[1]) - 1

        if griglia[r][c] == ' ':
            # mossa lecita, eseguila
            griglia[r][c] = simbolo
            if vittoria2(griglia, simbolo):
                print("Hai vinto!")
                finito = True
        else:
            print("Mossa non permessa - partita interrotta")
            finito = True
            # TODO: fai in modo di ripetere l'inserimento

        turni = turni + 1
        giocatore1 = not giocatore1

    if turni == 9 and finito == False:
        print("PAREGGIO")


def crea_griglia():
    g = []
    for riga in range(3):
        g.append([' '] * 3)  # [ ' ', ' ', ' ' ]
    return g

    # return [[ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ], [ ' ', ' ', ' ' ]]

    # NO (riusa 3 volte la stessa lista anziché 3 righe diverse)
    # ## return [[ ' ', ' ', ' ' ]]*3


def stampa_griglia(griglia):
    for riga in griglia:
        print(' | '.join(riga))
        print('-' * 9)


def vittoria(griglia, simbolo):
    if griglia[0][0] == simbolo and griglia[0][1] == simbolo and griglia[0][2] == simbolo:
        return True
    elif griglia[1][0] == simbolo and griglia[1][1] == simbolo and griglia[1][2] == simbolo:
        return True
    elif griglia[2][0] == simbolo and griglia[2][1] == simbolo and griglia[2][2] == simbolo:
        return True
    elif griglia[0][0] == simbolo and griglia[1][0] == simbolo and griglia[2][0] == simbolo:
        return True
    elif griglia[0][1] == simbolo and griglia[1][1] == simbolo and griglia[2][1] == simbolo:
        return True
    elif griglia[0][2] == simbolo and griglia[1][2] == simbolo and griglia[2][2] == simbolo:
        return True
    elif griglia[0][0] == simbolo and griglia[1][1] == simbolo and griglia[2][2] == simbolo:
        return True
    elif griglia[0][2] == simbolo and griglia[1][1] == simbolo and griglia[2][0] == simbolo:
        return True
    else:
        return False


def vittoria2(griglia, simbolo):
    trovato = False

    # Cerca per righe
    for riga in range(3):
        ok = True
        for col in range(3):
            if griglia[riga][col] != simbolo:
                ok = False
        if ok:
            trovato = True

    # Cerca per colonne
    for col in range(3):
        ok = True
        for riga in range(3):
            if griglia[riga][col] != simbolo:
                ok = False
        if ok:
            trovato = True

    # Cerca diagonale principale
    diag_ok = True
    for r in range(3):
        if griglia[r][r] != simbolo:
            diag_ok = False

    if diag_ok:
        trovato = True

    # Cerca diagonale inversa
    diag_ok = True
    for r in range(3):
        if griglia[r][2 - r] != simbolo:
            diag_ok = False

    if diag_ok:
        trovato = True

    return trovato


main()
