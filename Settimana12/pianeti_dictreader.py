import csv

pianeti = []
pianeti_diz = {}

with open('planets.csv', 'r', encoding='utf-8') as infile:

    reader = csv.DictReader(infile, fieldnames=['nome', 'massa', 'diametro', 'densita'])

    for pianeta in reader:
        pianeti['massa'] = float(pianeti['massa'])
        pianeti.append(pianeta)
        pianeti_diz[pianeta['Planet']] = pianeta

print(pianeti)

# Determina il pianeta che ha la massima gravità
#
# maxg = 0.0
# nome_max = ''
# for pianeta in pianeti:
#     if pianeta['gravita'] > maxg:
#         nome_max = pianeta['nome']
#         maxg = pianeta['gravita']
# print(f'La massima gravità si trova su {nome_max} e vale {maxg}')
