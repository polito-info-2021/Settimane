# Soluzione esercizio 4.3 del Lab04

n = int(input("Lato: "))

# Stampa il quadrato
# faccio n righe
# con n asterischi per riga

for riga in range(n):
    # print('*' * n)

    for col in range(n):
        print('*', end='')
    print()

print('\n' * 3)

# Stampa il rombo

for riga in range(n):
    spazi = n - riga - 1
    aster = 1 + 2 * riga
    # print(f'{spazi=} {aster=}')
    print(' ' * spazi + '*' * aster)

for riga in range(n - 2, -1, -1):
    spazi = n - riga - 1
    aster = 1 + 2 * riga
    # print(f'{spazi=} {aster=}')
    print(' ' * spazi + '*' * aster)
