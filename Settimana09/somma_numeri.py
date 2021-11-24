# LEGGO IL FILE

numeri = open('numeri.txt', 'r', encoding='utf-8')

# num = []  # lista di float con i numeri presenti nel file
# riga = numeri.readline()
# while riga != '':
#     n = float(riga)
#     num.append(n)
#
#     riga = numeri.readline()

num = numeri.readlines()

# for i in range(len(num)):
#     num[i] = float(num[i])

num = [ float(v) for v in num ]

numeri.close()

# CALCOLO SOMMA E MEDIA

somma = sum(num)
media = somma / len(num)

# CREO IL FILE DI USCITA

outfile = open('numeri_elaborati.txt', 'w', encoding='utf-8')
for n in num:
    outfile.write(f'{n:8.2f}\n')
outfile.write('-'*10 + '\n')
outfile.write(f'Somma = {somma:8.2f}\n')
outfile.write(f'Media = {media:8.2f}\n')
outfile.close()
