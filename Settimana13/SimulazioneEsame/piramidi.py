# Soluzione proposta all'esercizio "Piramidi"

mappa = []
file = open('mappa.txt', 'r')
for riga in file:
    campi = riga.rstrip().split()

    # campi = [int(x) for x in campi]
    for i in range(len(campi)):
        campi[i] = int(campi[i])
    mappa.append(campi)
file.close()

# print(mappa)

cime = []  # lista di tuple (altezza, riga, colonna)

n_righe = len(mappa)
n_colonne = len(mappa[0])

for r in range(len(mappa)):
    for c in range(len(mappa[r])):
        trovata = True

        if r>0 and mappa[r][c]<mappa[r-1][c]:
            trovata = False

        if r<n_righe-1 and mappa[r][c]<mappa[r+1][c]:
            trovata = False

        if c>0 and mappa[r][c]<mappa[r][c-1]:
            trovata = False

        if c<n_colonne-1 and mappa[r][c]<mappa[r][c+1]:
            trovata = False

        if r>0 and c>0 and mappa[r][c]<mappa[r-1][c-1]:
            trovata = False
        if r>0 and c<n_colonne-1 and mappa[r][c]<mappa[r-1][c+1]:
            trovata = False
        if r<n_righe-1 and c>0 and mappa[r][c]<mappa[r+1][c-1]:
            trovata = False
        if r<n_righe-1 and c<n_colonne-1 and mappa[r][c]<mappa[r+1][c+1]:
            trovata = False

        if mappa[r][c]>0 and trovata:
            cime.append((mappa[r][c], r, c))

# print(cime)

somma = 0
for cima in cime:
    print(cima[0], cima[1], cima[2])
    somma = somma + cima[0]

print(f'Altezza media: {somma/len(cime)}')
