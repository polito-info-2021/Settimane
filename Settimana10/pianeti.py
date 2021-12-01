import csv

file_pianeti = open('planets.csv', 'r', encoding='utf-8')

# prima_riga = file_pianeti.readline()
# intestazioni = prima_riga.split()
# for riga in file_pianeti:
#     campi = riga.split(',')
#     campi[0] è il nome
#     float(campi[1]) è la massa
#     ecc...

csv_reader_pianeti = csv.reader(file_pianeti)

pianeti = []

prima = True
for campi in csv_reader_pianeti:
    if prima:
        prima = False
        intestazioni = campi
        print(intestazioni)
    else:
        pianeti.append( [campi[0], float(campi[1]), float(campi[3])] )
        # pianeti.append(campi)


print(intestazioni)
print(pianeti)


file_pianeti.close()
