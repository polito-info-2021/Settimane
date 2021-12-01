FILENAME_INPUT = 'estremi.dat'
FILENAME_OUTPUT = 'differenze.dat'

file_estremi = open(FILENAME_INPUT, 'r', encoding='utf-8')

dati = []

for line in file_estremi:
    campi = line.rstrip().split()
    x = int(campi[0])
    y = int(campi[1])
    print(x,y)
    dati.append([x, y])

file_estremi.close()

print(dati)

diff = []
for record in dati:
    diff.append( record[0]-record[1] )

print(diff)

file_differenze = open(FILENAME_OUTPUT, 'w', encoding='utf-8')

for d in diff:
    # file_differenze.write(str(d)+'\n')
    # file_differenze.write(f'{d}\n')
    print(d, file=file_differenze)

file_differenze.close()

with open(FILENAME_OUTPUT, 'w', encoding='utf-8') as file_differenze:
    for d in diff:
        print(d, file=file_differenze)

print('finito')
