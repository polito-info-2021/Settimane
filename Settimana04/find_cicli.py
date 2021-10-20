name = 'John Wayne John Johnx'

# Cerca TUTTE LE occorrenza di 'n' nel nome
cerca = 'n'

pos = 0
conta = 0  ## B1
while pos<len(name):
    # conta = 0  ## B2

    if name[pos] == cerca:
        print(name[pos], 'in posizione', pos) ## A1
        conta = conta + 1
        # conta = 0  ## B3

        # print(f'Ho trovato {conta} volte la stringa {cerca}') ## 3
    pos = pos + 1
    # print(f'Ho trovato {conta} volte la stringa {cerca}') ## 2

print(f'Ho trovato {conta} volte la stringa {cerca}') ## 1
# print(name[pos], 'in posizione', pos) ## A2
