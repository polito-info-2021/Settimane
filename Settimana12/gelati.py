vendite = {}

with open('icecream.txt', 'r', encoding='utf-8') as f:
    for line in f:
        campi = line.rstrip().split(':')

        vendite[campi[0]] = [float(campi[1]), float(campi[2]), float(campi[3])]
        # [float(x) for x in campi[1:]]

print(vendite)

for gusto in sorted(vendite):
    # print(gusto, vendite[gusto][0], vendite[gusto][1],
    #       vendite[gusto][2], )
    print(f'{gusto:25s}{vendite[gusto][0]:10.2f}{vendite[gusto][1]:10.2f}{vendite[gusto][2]:10.2f}{sum(vendite[gusto]):10.2f}')

print(' '*25, end='')
for negozio in range(3):
    somma = 0
    for gusto in vendite:
        somma = somma + vendite[gusto][negozio]
    print(f'{somma:10.2f}', end='')
print()