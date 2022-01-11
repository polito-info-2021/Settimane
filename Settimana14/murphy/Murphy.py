import pprint

def leggi_frasi(file):
    murphy_file = open(file, "r", encoding="UTF-8")
    frasi = {}
    frase = ""

    for line in murphy_file:
        nome_frase = line.rstrip()
        massima = murphy_file.readline().rstrip("\n")
        while massima != "":
            frase += massima + " "
            massima = murphy_file.readline().rstrip("\n")

        frasi[nome_frase] = frase
        frase = ""

    murphy_file.close()

    return frasi


def leggi_argomenti(file):
    argomenti_file = open(file, "r", encoding="UTF-8")
    parole = set()

    for line in argomenti_file:
        parole.add(line.rstrip())

    return parole


def trova_parola(frasi, parole):
    rilevanti = []

    for item in frasi:
        lista_parole = frasi[item].split()
        for i in range(len(lista_parole)):
            lista_parole[i] = lista_parole[i].strip(',.;:\'\"()').lower()

        if set(lista_parole).intersection(parole) != set():
            rilevanti.append(item)

    return rilevanti


def main():
    frasi = leggi_frasi("Leggi_di_Murphy.txt")
    parole = leggi_argomenti("argomenti.txt")
    rilevanti = trova_parola(frasi, parole)

    if len(rilevanti) == 0:
        print("L'argomenti non si trovano nelle leggi")
    else:
        for i in range(len(rilevanti)):
            print(f'{rilevanti[i]} - ', end="")
            if len(frasi[rilevanti[i]]) > 50:
                print(f'{frasi[rilevanti[i]][:50]}...')
            else:
                print(frasi[rilevanti[i]])


main()
