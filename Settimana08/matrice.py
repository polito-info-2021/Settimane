from pprint import pprint

N = 4
M = 5

# costruisco matrice NxM fatta di zeri

matrice = []
for riga in range(N):

    colonna = []
    for col in range(M):
        colonna.append(0)

    matrice.append(colonna)

for riga in range(len(matrice)):
    for col in range(len(matrice[riga])):
        print(matrice[riga][col], end= ' ')
    print()
