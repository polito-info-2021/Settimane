parole_storia = set()

with open('alice.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        parole = line.rstrip().split()
        for parola in parole:
            parola_pulita = parola.strip(',."?`\'();:!-')
            parola_pulita = parola_pulita.lower()
            parole_storia.add(parola_pulita)

print(len(parole_storia))

parole_dizionario = set()
with open('words.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        parole_dizionario.add(line.rstrip().lower())

print(len(parole_dizionario))

if not parole_storia.issubset(parole_dizionario):
    print("Ci sono parole errate!")
    parole_errate = parole_storia.difference(parole_dizionario)
    print(sorted(parole_errate))

# parole_errate = []
# for parola1 in parole_storia:
#     if not parola1 in parole_dizionario:
#         parole_errate = parole_errate.append(parola1)

