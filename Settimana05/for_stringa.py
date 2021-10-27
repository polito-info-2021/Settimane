# Data una stringa inserita dall'utente,
# stampare tutte le vocali in posizione pari
# all'interno della stringa.

testo = 'Elefante'

# VERSIONE 1: CICLO WHILE con gestione manuale dell'indice
pos = 0
while pos < len(testo):
    lettera = testo[pos].lower()
    if (lettera in "aeiou") and (pos % 2 == 0):
        print(f'trovato {lettera} in posizione {pos}')
    pos = pos + 1

# SBAGLIATO!!! IL METODO FIND RITORNA SEMPRE IL *PRIMO* VALORE
# IN CASO DI DUPLICATI L'ALGORITMO FALLISCE
# for ch in testo:
#     pos = testo.find(ch)
#     if ch.lower() in "aeiou" and (pos % 2 == 0):
#         print(f'trovato {ch} in posizione {pos}')

pos = 0
for ch in testo:
    if ch.lower() in "aeiou" and (pos % 2 == 0):
        print(f'trovato {ch} in posizione {pos}')
    pos = pos + 1

for pos in range(len(testo)):
    lettera = testo[pos].lower()
    if (lettera in "aeiou") and (pos % 2 == 0):
        print(f'trovato {lettera} in posizione {pos}')

for (pos, lettera) in enumerate(testo):
    if (lettera.lower() in "aeiou") and (pos % 2 == 0):
        print(f'trovato {lettera} in posizione {pos}')
