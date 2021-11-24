filastrocca = open("mary.txt", "r")

c = 0
riga='x'
while riga!='':
    riga = filastrocca.readline()

    riga2 = riga.rstrip('\n')
    print(f'Riga {c}: "{riga2}"')

    c = c+1
filastrocca.close()

filastrocca = open("mary.txt", "r")

c = 0
riga = filastrocca.readline()
while riga != '':
    riga2 = riga.rstrip('\n')
    print(f'Riga {c}: "{riga2}"')

    c = c+1
    riga = filastrocca.readline()
filastrocca.close()

# riga = filastrocca.readline().rstrip('\n')
# print(f'Prima riga: "{riga}"')
#
# riga = filastrocca.readline().rstrip('\n')
# print(f'Seconda riga: "{riga}"')
#
# riga = filastrocca.readline().rstrip('\n')
# print(f'Terza riga: "{riga}"')
