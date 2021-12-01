import csv

film = []

file_film = open('movies.csv', 'r', encoding='utf-8')

file_film.readline()  # leggi e scarta la prima riga

csv_film = csv.reader(file_film)
for campi in csv_film:
    film.append(campi)
file_film.close()

# Pulizia dei campi e conversioni di tipo
for campi in film:
    campi[1] = int(campi[1])  # converti l'anno in numero intero

    # converti la stringa degli attori (separati da virgola) in una lista di stringhe (una per attore)
    attori = campi[4].split(',')  # lista di stringhe

    # for i in range(len(attori)):
    #     attori[i] = attori[i].strip()

    attori = [a.strip() for a in attori]  # rimozione spazi a contorno del singolo attore

    campi[4] = attori  # rimpiazza la stringa con la lista, nel record della lista 'film'

# Quali sono tutti i  film in cui ha recitato un attore inserito da tastiera?

nome_attore = input("Attore: ")
while nome_attore != '':

    elenco = []  # lista con i nomi dei film in cui ha recitato
    for f in film:
        if nome_attore in f[4]:
            elenco.append(f[0])
    elenco.sort()
    print('\n'.join(elenco))  # stampa i nomi dell'elenco, uno per riga

    nome_attore = input("Attore: ")

# Dati due attori, hanno mai lavorato insieme?
