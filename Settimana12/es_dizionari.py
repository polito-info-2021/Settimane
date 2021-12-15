voti = {
    "Bruno": [19, 20, 21],

    "Antonio": [30, 30, 30, 29],
}

voti["Carlo"] = [25]

print(voti)

# stampa tutti gli studenti
for nome in voti:
    lista_voti = voti[nome]
    media = sum(lista_voti)/len(lista_voti)
    print(f'La media di {nome} è {media}')

for item in voti.items():
    # print(item)
    nome = item[0]
    lista_voti = item[1]

for nome, lista_voti in voti.items():
    media = sum(lista_voti)/len(lista_voti)
    print(f'La media di {nome} è {media}')
