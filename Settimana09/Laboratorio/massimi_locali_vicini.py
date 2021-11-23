# Laboratorio 8, Esercizio 8, Massimi locali più vicini

numeri = [1, 2, 3, 2, 1, 1, 4, 6, 8, 7, 6, 5, 6, 5, 4, 3, 2, 9]

pos_massimi = []

for pos in range(1, len(numeri) - 1):  # tutti i numeri tranne il primo e l'ultimo
    if numeri[pos] > numeri[pos - 1] and numeri[pos] > numeri[pos + 1]:
        print(f'Il valore {numeri[pos]} alla posizione {pos} è un massimo locale')
        pos_massimi.append(pos)

# print(pos_massimi)
# pos_massimi = [ 2, 8, 12 ]
"""
IDEA
1) costruisco una lista in cui metto gli INDICI delle posizioni dei max locali
2) analizzo questa lista calcolando la differenza tra gli elementi consecutivi
3) trovo il minimo di queste differenze
"""
if len(pos_massimi) >= 2:

    min_differenza = 100000  # len(numeri)
    pos_min_differenza = -1

    for i in range(len(pos_massimi) - 1):
        differenza = pos_massimi[i + 1] - pos_massimi[i]
        if differenza < min_differenza:
            min_differenza = differenza
            pos_min_differenza = i
        print(f'(i={i}) Massimi in posizione {pos_massimi[i]} e {pos_massimi[i + 1]} : differenza {differenza}')

    print(f'I massimi locali più vicini sono distanti {min_differenza}')
    print(f'e si trovano in posizione {pos_massimi[pos_min_differenza]} e {pos_massimi[pos_min_differenza+1]}')
    print(f'ed il valore è {numeri[pos_massimi[pos_min_differenza]]} e {numeri[pos_massimi[pos_min_differenza+1]]}')

    # pos_min_differenza == 1  : posizione all'interno di pos_massimi
    # pos_massimi[pos_min_differenza] == 8  : primo massimo
    # pos_massimi[pos_min_differenza+1] == 12  : secondo massimo
    # numeri[pos_massimi[pos_min_differenza]] : valore primo max
    # numeri[pos_massimi[pos_min_differenza+1]] : valore secondo max
else:
    print("Non ci sono abbastanza massimi locali per risolvere l'esercizio")