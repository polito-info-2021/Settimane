FILE_POP = 'worldpop.txt'
FILE_AREA = 'worldarea.txt'

FILE_DENSITA = 'world_pop_density.txt'

file_pop = open(FILE_POP, 'r', encoding='utf-8')
file_area = open(FILE_AREA, 'r', encoding='utf-8')
file_densita = open(FILE_DENSITA, 'w', encoding='utf-8')

riga_pop = file_pop.readline()
riga_area = file_area.readline()
while riga_pop != '' and riga_area != '':
    popolazione = int(riga_pop.rstrip().split()[-1])  # estrae l'ultimo elemento, dopo avere separato in corrispondenza di spazi & tab
    nazione = ' '.join(riga_pop.rstrip().split()[:-1])  # estrae gli elementi tranne l'ultimo, e ricostruisce un'unica stringa separata da spazi
    area = int(riga_area.rstrip().split()[-1])
    if area != 0:
        print(f'{nazione:40} {popolazione / area:8.2f}', file=file_densita)
    else:
        print(f'{nazione:40} {"*":>8}', file=file_densita)

    riga_pop = file_pop.readline()
    riga_area = file_area.readline()

# for riga_pop in file_pop:
#     riga_area = file_area.readline()
#     popol = ...


file_pop.close()
file_area.close()
file_densita.close()
