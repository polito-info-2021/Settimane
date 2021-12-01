FILENAME_INPUT = 'estremi.dat'
FILENAME_OUTPUT = 'differenze.dat'

file_estremi = open(FILENAME_INPUT, 'r', encoding='utf-8')
file_differenze = open(FILENAME_OUTPUT, 'w', encoding='utf-8')

for line in file_estremi:
    campi = line.rstrip().split()
    x = int(campi[0])
    y = int(campi[1])
    d = x - y
    print(d, file=file_differenze)

file_estremi.close()
file_differenze.close()



with open(FILENAME_INPUT, 'r', encoding='utf-8') as file_estremi:
    with open(FILENAME_OUTPUT, 'w', encoding='utf-8') as file_differenze:
        for line in file_estremi:
            campi = line.rstrip().split()
            x = int(campi[0])
            y = int(campi[1])
            d = x - y
            print(d, file=file_differenze)
