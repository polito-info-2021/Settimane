parole_uniche = set()

with open('mary.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        parole = line.rstrip().split()
        for parola in parole:
            parola_pulita = parola.strip(',."?')
            parola_pulita = parola_pulita.lower()
            parole_uniche.add(parola_pulita)

print(parole_uniche)

print(f'Il numero di parole uniche è {len(parole_uniche)}')

lista_temp = list(parole_uniche)

lista_temp = sorted(lista_temp)
lista_temp.sort()

parole_uniche.sort()

for p in sorted(parole_uniche):
    print(p)

for i in range(len(parole_uniche)):
    print(parole_uniche[i])
