"""
Scrivere un programma che acquisisca dall'utente le coordinate di una casella
della scacchiera (nel formato 'g5'), e determini se la casella specificata
sia bianca o nera.
"""

# 1. Acquisisci i dati
casella = input('Inserisci le coordinate di una casella (es. g5): ')
# casella = casella.lower()

# 2. Controlla la validità dei dati
# le coordinate della casella devono essere una stringa di 2 caratteri
if len(casella) != 2:
    print(f'La casella {casella} è nel formato errato, lunga {len(casella)} caratteri anziché 2')
else:  # 'gg'
    colonna = casella[0].lower()  # 'g'
    riga = casella[1]  # '5'
    # di cui il primo una lettera 'a'-'h', il secondo una cifra 1-8
    # 'b7' ok  / 'z9' no / 'A2' ? ok / '7b' ? no / 'a' no / 'b7c' no

    # if colonna in 'abcdefgh': #ok
    # if colonna=='a' or colonna=='b' or colonna=='c'... : #ok
    # if 'a' <= colonna <= 'h': #ok
    # if colonna >= 'a' and colonna <= 'h': #ok
    # if colonna < 'a' or colonna > 'h': #err
    # if not('a' <= colonna <= 'h'): #err
    if ('a' <= colonna <= 'h') and ('1' <= riga <= '8'):

        # 3. Determina il colore della casella
        # Determina il NUMERO della colonna ('a'->1 ... 'h'->8)
        num_riga = int(riga)

        if colonna == 'a':
            num_colonna = 1
        elif colonna == 'b':
            num_colonna = 2
        elif colonna == 'c':
            num_colonna = 3
        elif colonna == 'd':
            num_colonna = 4
        elif colonna == 'e':
            num_colonna = 5
        elif colonna == 'f':
            num_colonna = 6
        elif colonna == 'g':
            num_colonna = 7
        else:
            num_colonna = 8

        num_colonna = ord(colonna) - (ord('a') - 1)  # 96

        # in che posizione si trova colonna all'interno di "abcdefgh" ?
        # num_colonna = "abcdefgh".find(colonna)+1

        # Calcola la somma del numero di riga + numero di colonna
        # Se questa somma è pari -> nera, altrimenti -> bianca
        if (num_riga + num_colonna) % 2 == 0:
            colore = 'nera'
        else:
            colore = 'bianca'

        # 4. Stampa il risultato
        print(f'La casella {casella} è {colore}')

    else:
        print('Le coordinate non sono valide')
