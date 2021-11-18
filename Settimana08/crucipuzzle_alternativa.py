# Soluzione esercizio Crucipuzzle
from pprint import pprint


def leggi_matrice():
    matrice = [
        ['E', 'B', 'C', 'D', 'E'],
        ['F', 'D', 'R', 'I', 'J'],
        ['K', 'O', 'O', 'N', 'O'],
        ['T', 'Q', 'R', 'L', 'T']
    ]
    return matrice


def trova_parola(parola, matrice, r0, c0, dr, dc):
    r,c = r0,c0
    for lettera in parola:
        if r<0 or r>=len(matrice) or c<0 or c>=len(matrice[0]):
            return False
        if matrice[r][c] != lettera:
            return False
        r,c = r+dr, c+dc
    return True

def cerca_parola(parola, matrice):
    for r in range(len(matrice)):
        for c in range(len(matrice[0])):
            if matrice[r][c] == parola[0]:
                if trova_parola(parola, matrice, r, c, 0, 1):
                    print(f'Trovato dalla posizione {r},{c} in direzione ➡')
                if trova_parola(parola, matrice, r, c, 0, -1):
                    print(f'Trovato dalla posizione {r},{c} in direzione ⬅')
                if trova_parola(parola, matrice, r, c, 1, 0):
                    print(f'Trovato dalla posizione {r},{c} in direzione ⬇')
                if trova_parola(parola, matrice, r, c, -1, 0):
                    print(f'Trovato dalla posizione {r},{c} in direzione ⬆')

                if trova_parola(parola, matrice, r, c, 1, 1):
                    print(f'Trovato dalla posizione {r},{c} in direzione ↘')
                if trova_parola(parola, matrice, r, c, 1, -1):
                    print(f'Trovato dalla posizione {r},{c} in direzione ↙')
                if trova_parola(parola, matrice, r, c, -1, 1):
                    print(f'Trovato dalla posizione {r},{c} in direzione ↗')
                if trova_parola(parola, matrice, r, c, -1, -1):
                    print(f'Trovato dalla posizione {r},{c} in direzione ↖')


def main():
    matrice = leggi_matrice()
    pprint(matrice)

    parola = input("Parola: ")
    while parola:
        cerca_parola(parola, matrice)
        parola = input("Parola: ")


main()
