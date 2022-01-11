# leggere i file ... decidere tipi struttura di dati
# confrontare emtrambi

prodottiFile = open("prodotti.txt", "r", encoding="UTF-8")
prodottiVenditori = {}

for line in prodottiFile:
    dati = line.split()
    prodottiVenditori[dati[0]] = {dati[1]}

prodottiFile.close()

acquisitiFile = open("acquisti.txt", "r", encoding="UTF-8")
acquisti = {}

for line in acquisitiFile:
    dati = line.split()

    if dati[0] not in acquisti:
        acquisti[dati[0]] = {dati[1]}
    else:
        acquisti[dati[0]].add(dati[1])


for elemento in acquisti.items():
    ufficiale = prodottiVenditori[elemento[0]]
    rivenditori = elemento[1]

    if len(rivenditori.difference(ufficiale)) > 0:
        print("Codice prodotto: ", elemento[0])
        print("Rivenditore ufficiale: ", ", ".join(ufficiale))
        print("Lista rivenditori: ", ", ".join(rivenditori))
        print("\n")
