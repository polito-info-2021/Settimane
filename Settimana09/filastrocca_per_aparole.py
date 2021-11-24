NOME_FILE = 'mary.txt'

filastrocca = open(NOME_FILE, 'r', encoding='utf-8')

# for riga in filastrocca:
#     # print(riga)
#     parole = riga.split()
#     for parola in parole:
#         parola_pulita = parola.lower().rstrip(',.')
#         print(parola_pulita)

# righe = []
# for riga in filastrocca:
#     righe.append(riga)

righe = filastrocca.readlines()

print(righe)

filastrocca.close()
