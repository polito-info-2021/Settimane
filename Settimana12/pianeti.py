import csv

pianeti = []
pianeti_diz = {}

with open('planets.csv', 'r', encoding='utf-8') as infile:
    infile.readline() # butta via la prima riga

    reader = csv.reader(infile)

    for campi in reader:
        # campi = line.rstrip().split(',')
        pianeta = {
            'nome': campi[0],
            'massa': float(campi[1]),
            'gravita': float(campi[4])
        }
        pianeti.append(pianeta)
        pianeti_diz[campi[0]] = pianeta

print(pianeti)

# Determina il pianeta che ha la massima gravità

maxg = 0.0
nome_max = ''
for pianeta in pianeti:
    if pianeta['gravita'] > maxg:
        nome_max = pianeta['nome']
        maxg = pianeta['gravita']
print(f'La massima gravità si trova su {nome_max} e vale {maxg}')
