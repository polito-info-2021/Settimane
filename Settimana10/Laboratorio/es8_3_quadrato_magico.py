# Laboratorio 08, Esercizio 3: Quadrato Magico

quadrato = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

magico = True

# Verifica che ci siano tutti e soli i numeri tra 1 e 16
for num in range(1, 17):
    # c'è il numero 'num' nella matrice?
    # deve essere in almeno una riga
    num_ok = False
    for riga in quadrato:
        if num in riga:
            num_ok = True
    if not num_ok:
        magico = False

# Verifica la somma delle righe
somma = sum(quadrato[0])  # uso la prima riga come riferimento

for riga in quadrato:
    if sum(riga) != somma:
        magico = False

# Verifica la somma delle colonne
for c in range(4):  # c: indice di colonna
    s = 0  # somma elementi colonna c
    for r in range(4):
        s = s + quadrato[r][c]
    if s != somma:
        magico = False

# Verifica diagonale discendente
s = 0
for r in range(4):
    s = s + quadrato[r][r]
if s != somma:
    magico = False

# Verifica diagonale ascendente
s = 0
for r in range(4):
    s = s + quadrato[r][3 - r]
if s != somma:
    magico = False

print(f'Quadrato magico {magico}')
