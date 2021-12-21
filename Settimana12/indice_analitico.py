# creiamo un DIZIONARIO
# - CHIAVE: termine da inserire
# - VALORE: INSIEME
#             - numeri di pagina

# analitico = {
#     'example': {7, 10},
#     'index': {7},
#     'program': {7, 11}
# }

analitico = {}

with open('indexdata.txt', 'r', encoding='utf-8') as f:
    for line in f:
        campi = line.rstrip().split(':')
        pag = int(campi[0])
        termine = campi[1]

        print(f'Il termine {termine} compare a pagina {pag}')

        if termine not in analitico:
            analitico[termine] = {pag}
        else:
            analitico[termine].add(pag)
            # analitico[termine] = analitico[termine].union({pag})

print(analitico)

for termine in sorted(analitico):
    pagine = analitico[termine]
    lista_pagine = sorted(pagine)
    lista_pagine = [str(x) for x in lista_pagine]
    elenco_pagine = ', '.join(lista_pagine)
    print(f'{termine}: {elenco_pagine}')