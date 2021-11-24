"""
Determinare la frequenza con cui, nel racconto di Alice, compaiono
le parole di diversa lunghezza.

Es.
Lunghezza 1: 2000 parole
Lunghezza 2: 1300 parole'
...
Lunghezza 13: 2 parole
"""

# 1) LEGGO IL FILE E COSTRUISCO UNA LISTA CON TUTTE LE PAROLE
# parole = ['Alice', 'was', 'beginning', 'to', ....]
parole = []
filein = open('alice.txt', 'r', encoding='utf-8')
for riga in filein:
    # print(riga)

    parole_riga = riga.strip().split()
    # print(parole)
    for parola in parole_riga:
        parola_pulita = parola.lower().strip('.,-"?!\':`;()')
        parole.append(parola_pulita)
filein.close()
# print(parole)

# 2) CREO UNA "LISTA DI CONTATORI" CHE MEMORIZZA LE VARIE LUNGHEZZE
# lunghezze = [ 0, 2000, 1300, ... 2 ]

lunghezze_parole = [ len(p) for p in parole ]
# print(lunghezze_parole)

max_lunghezza = max(lunghezze_parole)

lunghezze = [0] * (max_lunghezza+1)

for lun in lunghezze_parole:
    lunghezze[lun] = lunghezze[lun] + 1

print(lunghezze)

print(len(lunghezze))

lunghezze2 = [0]
for lun in range(1, max_lunghezza+1):
    lunghezze2.append(lunghezze_parole.count(lun))

print(lunghezze2)
