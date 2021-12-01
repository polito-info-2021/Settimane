import csv

film = []

file_film = open('movies.csv', 'r', encoding='utf-8')

file_film.readline()   # leggi e scarta la prima riga

csv_film = csv.reader(file_film)
for campi in csv_film:
    film.append(campi)

file_film.close()

for campi in film:
    campi[1] = int(campi[1])
    attori = campi[4].split(',')

    # for i in range(len(attori)):
    #     attori[i] = attori[i].strip()

    attori = [ a.strip() for a in attori ]

    campi[4] = attori


# Quali sono tutti i  film in cui ha recitato un attore inserito da tastiera?

nome_attore = input("Attore: ")
while nome_attore!='':

    elenco = []  # lista con i nomi dei film in cui ha recitato
    for f  in film:
        if nome_attore in f[4]:
            elenco.append(f[0])
    elenco.sort()
    print('\n'.join(elenco))  # stampa i nomi dell'elenco, uno per riga

    nome_attore = input("Attore: ")

# Dati due attori, hanno mai lavorato insieme?
