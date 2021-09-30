import csv
import operator

from matplotlib import pyplot


FILENAME = '14BHDLZ_2022_shuffled.csv'

# Leggi l'elenco degli studenti e salvalo in una lista di liste
def leggi(nome_file):
    file = open(nome_file, 'r', newline='')
    reader = csv.reader(file)
    prima = True
    studenti = []
    for line in reader:
        if prima:  # skip first line (headers)
            prima = False
        else:
            studenti.append(line)
    file.close()
    return studenti


# estrai i nomi (first name) da un elenco di studenti
def estrai_nomi(elenco):
    lista_nomi = []
    for riga in elenco:
        lista_nomi.append(riga[2])
    return lista_nomi


# Calcola le frequenze dei vari nomi presenti in un array
def frequenze(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] = freq[token] + 1
        else:
            freq[token] = 1
    return freq


# calcola il massimo valore presente nelle frequenze
def max_frequenza(freq):
    return max(freq.values())


def nomi_piu_frequenti(freq, max):
    return [nome for (nome, frequenza) in freq.items() if frequenza == max]


def main():
    stud = leggi(FILENAME)
    nomi = estrai_nomi(stud)
    print(f"Nella classe ci sono {len(stud)} studenti")
    freq = frequenze(nomi)
    max_freq = max_frequenza(freq)
    print(f"Il nome più frequente compare {max_freq} volte")
    nomi_max = nomi_piu_frequenti(freq, max_freq)
    print(f"Si tratta di : {', '.join(nomi_max)}")
    # estrai solo i nomi che compaiono almeno 3 volte
    freq2 = {k: v for (k, v) in freq.items() if v >= 3}
    print(
        f"I nomi che compaiono più di una volta sono {', '.join(sorted(list(freq2.keys())))}."
    )

    hist = list(sorted(list(freq2.items()), key=operator.itemgetter(1), reverse=True))
    pyplot.barh([h[0] for h in hist], [h[1] for h in hist])
    pyplot.show()


main()
