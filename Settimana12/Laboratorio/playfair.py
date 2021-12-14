def main():
    chiave = input('Chiave? ')
    matrice = crea_matrice(chiave)
    nome_file_in = input('File di ingresso? ')
    nome_file_out = input('File codificato? ')
    file_in = open(nome_file_in, 'r')
    file_out = open(nome_file_out, 'w')

    testo_chiaro = file_in.read()
    testo_chiaro = pulisci_file(testo_chiaro)
    # elimino tutti i carattere non alfabetici
    # rendere pari il numero di caratteri totali

    for pos in range(0, len(testo_chiaro), 2):
        # codifica testo_chiaro[pos] e testo_chiaro[pos+1]
        nuova = codifica(testo_chiaro[pos:pos + 2], matrice)
        file_out.write(nuova)
    file_out.write('\n')

    file_in.close()
    file_out.close()

    # ABCDEF -> AB CD EF -> BA DC PM -> BADCPM
    # ABC, D EF. -> ()A()B ()C(, )D ( )E()F (.) ->
        # ()B()A ()D(, )C ( )P()M (.)


def codifica(coppia, matrice):
    """
    Prende una coppia di lettere (alfabetiche maiuscole) e restituisce
    la coppia codificata (stringa di 2 caratteri) secondo la matrice.

    :param coppia: coppia di lettere da convertire
    :param matrice: cifrario 5x5
    :return: coppia di lettere convertite
    """
    r1, c1 = trova_coordinate(coppia[0], matrice)
    r2, c2 = trova_coordinate(coppia[1], matrice)

    if r1 == r2 or c1 == c2:
        return matrice[r2][c2] + matrice[r1][c1]
    else:
        return matrice[r2][c1] + matrice[r1][c2]


def trova_coordinate(ch, matrice):
    for r in range(len(matrice)):
        if ch in matrice[r]:
            c = matrice[r].index(ch)
            return (r, c)
    print("ERRORE!!!!")


def crea_matrice(chiave):
    """
    Riceve una stringa qualsiasi, e costruisce la matrice di playfair

    :param chiave: parola alfabetica qualsiasi
    :return: matrice 5x5
    """
    chiave = chiave.upper()
    if not chiave.isalpha():
        raise ValueError("Chiave non alfabetica")
    chiave.replace("J", "I")

    lettere = list(chiave)  # ['P', 'L', 'A', ...]
    lettere = lettere + list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

    senza_duplicati = []
    for ch in lettere:
        if ch not in senza_duplicati:
            senza_duplicati.append(ch)

    matrice = []
    for r in range(5):
        matrice.append(senza_duplicati[r * 5:r * 5 + 5])

    return matrice


def pulisci_file(testo):
    testo = testo.upper()
    testo = testo.replace(' ', '').replace('\n', '')
    testo = testo.replace('J', 'I')

    if len(testo) % 2 != 0:
        testo = testo + 'Z'

    return testo


# matrice = [
#     list("PLAYF"),
#     list("IRBCD"),
#     list("EGHKM"),
#     list("NOQST"),
#     list("UVWXZ")
# ]

# matrice = crea_matrice("playfair")
#
# print(codifica("AB", matrice))
# print(codifica("CD", matrice))
# print(codifica("EF", matrice))
#
# print(codifica("HI", matrice))
# print(codifica("WH", matrice))
# print(codifica("AT", matrice))
# print(codifica("SU", matrice))
# print(codifica("PZ", matrice))
#
# print(codifica("BE", matrice))
# print(codifica("HW", matrice))
# print(codifica("QF", matrice))
# print(codifica("XN", matrice))
# print(codifica("UF", matrice))
#
# print(crea_matrice("playfair"))

main()
