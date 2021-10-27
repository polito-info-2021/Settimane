# stampare una tabella di RIGHE righe e COL colonne
# in cui ciascuna casella contenga il valore dato
# da (numero di riga) ** (numero di colonna)

RIGHE = 5
COL = 7

# 1 - stampa l'intestazione della tabella
print('| ', end='')
for col in range(1, COL + 1):
    print(f'x^{col:<8}', end=' | ')
print()
lung = (2 + COL * 13 - 1)
print('-' * lung)

# 2 - ripeti per RIGHE volte la stampa di una singola riga
for riga in range(1, RIGHE + 1):
    # 2.1 - stampa la riga di posizione {riga}
    # print(riga**1, riga**2, riga**3, riga**4, riga**5)
    print('| ', end='')
    for col in range(1, COL + 1):
        potenza = riga ** col
        print(f'{potenza:10}', end=' | ')
    print()
