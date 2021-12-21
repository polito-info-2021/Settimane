from pprint import pprint


def leggi_labirinto(nome_file):
    # 1. legge il file in una lista di stringhe
    with open(nome_file, 'r', encoding='utf-8') as f:
        righe = f.readlines()
    righe = [r.rstrip('\n') for r in righe]
    n_righe = len(righe)
    n_colonne = len(righe[0])

    # 2. costruisce il dizionario richiesto dal testo
    labirinto = {}
    # una entry per ogni corridoio ' '
    for r in range(len(righe)):
        for c in range(len(righe[r])):
            if righe[r][c] == ' ':
                corridoi = set()  # []
                if r > 0 and righe[r - 1][c] == ' ':
                    corridoi.add((r - 1, c))  # .append
                if r < len(righe) - 1 and righe[r + 1][c] == ' ':
                    corridoi.add((r + 1, c))
                if c > 0 and righe[r][c - 1] == ' ':
                    corridoi.add((r, c - 1))
                if c < len(righe[r]) - 1 and righe[r][c + 1] == ' ':
                    corridoi.add((r, c + 1))
                labirinto[(r, c)] = corridoi
    return labirinto, n_righe, n_colonne


def ricerca_uscite(labirinto, n_righe, n_colonne):
    # 1. costruisci un dizionario con tutti '?'
    uscite = {}
    for casella in labirinto:
        uscite[casella] = '?'

    # uscite = {casella: '?' for casella in labirinto}

    # 2. trova la direzione di uscita per i corridoi sui bordi
    for casella in uscite:  # casella = (riga, colonna)
        if casella[0] == 0:  # prima riga?
            uscite[casella] = 'N'
        elif casella[0] == n_righe-1:
            uscite[casella] = 'S'
        elif casella[1] == 0:
            uscite[casella] = 'W'
        elif casella[1] == n_colonne-1:
            uscite[casella] = 'E'
    # pprint(uscite)

    # 3. ripeti molte volte la ricerca dei corridoi adiacenti
    ancora = True
    while ancora:

        ancora = False
        # faccio una "passata" sul labirinto
        for casella in uscite:
            if uscite[casella] == '?':
                # questo è un corridoio di cui non conosco l'uscita
                # ho delle caselle adiacenti con uscita nota??
                for casella_adiacente in labirinto[casella]:
                    if uscite[casella_adiacente] != '?':
                        # ho trovato un adiacente da cui so come uscire
                        # uscite[casella] = direzione per andare da casella a casella_adiacente
                        if casella_adiacente[0]<casella[0]:
                            uscite[casella] = 'N'
                        elif casella_adiacente[0]>casella[0]:
                            uscite[casella] = 'S'
                        elif casella_adiacente[1] < casella[1]:
                            uscite[casella] = 'W'
                        elif casella_adiacente[1] > casella[1]:
                            uscite[casella] = 'E'
                        ancora = True
        # pprint(uscite)
    return uscite

def stampa_uscite(uscite, n_righe, n_colonne):
    for r in range(n_righe):
        for c in range(n_colonne):
            if (r,c) in uscite:
                print(uscite[(r,c)], end='')
            else:
                print('*', end='')
        print()

def main():
    labirinto, n_righe, n_colonne = leggi_labirinto('maze.txt')
    uscite = ricerca_uscite(labirinto, n_righe, n_colonne)
    stampa_uscite(uscite,n_righe,n_colonne)
    # pprint(labirinto)


main()
