giorni = [ 'Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

print(giorni)

# lunghezze = []
# for giorno in giorni:
#     lunghezze.append(len(giorno))
#
# print(lunghezze)

lunghezze = [ len(giorno) for giorno in giorni ]
print(lunghezze)
