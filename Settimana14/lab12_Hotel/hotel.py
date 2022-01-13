from operator import itemgetter


def leggi_presenze():
    presenze = []
    with open('presenze.txt', 'r', encoding='utf-8') as file:
        for riga in file:
            campi = riga.rstrip().split(',')
            ospite = {
                'nome': campi[0],
                'tel': campi[1],
                'ingresso': int(campi[2]),
                'uscita': int(campi[3])
            }
            presenze.append(ospite)
    return presenze


def leggi_sospetti():
    with open('sospetti.txt', 'r', encoding='utf-8') as file:
        sospetti = file.readlines()
    for i in range(len(sospetti)):
        sospetti[i] = sospetti[i].rstrip()
    return sospetti


def cerca_contatti(ospite, presenze):
    # cerca se l'ospite è stato presente
    ospite_trovato = None
    for presenza in presenze:
        if presenza['nome'] == ospite:
            ospite_trovato = presenza

    if ospite_trovato == None:
        # non è stato trovato
        return None  # nessun contatto
    else:
        ingresso_ospite = ospite_trovato['ingresso']
        uscita_ospite = ospite_trovato['uscita']

        contatti = []
        for presenza in presenze:
            ingresso_altro = presenza['ingresso']
            uscita_altro = presenza['uscita']

            if (presenza['nome'] != ospite and
                    not (uscita_altro < ingresso_ospite or uscita_ospite < ingresso_altro)):
                contatti.append(presenza)
        return contatti


def main():
    presenze = leggi_presenze()
    # print(presenze)
    sospetti = leggi_sospetti()
    # print(sospetti)
    for ospite in sospetti:
        contatti = cerca_contatti(ospite, presenze)
        if contatti == None:
            print(f'{ospite} non è in archivio')
        elif contatti == []:
            print(f'{ospite} non ha avuto contatti')
        else:
            print(f'Contatti di {ospite}')
            contatti.sort(key=itemgetter('nome'))
            for contatto in contatti:
                print(f'    {contatto["nome"]} - tel. {contatto["tel"]}')


main()

#
# [
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
# ]
#
# {
#     'Anna Rossi': {'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     'Giuseppe Verdi': {'tel': '23432432', 'ingresso': 100, 'uscita': 105}
# }


# ospite          [--------]
# altri    [---]                               NO   uscita_altro < ingresso_ospite
#                              [----]          NO   ingresso_altro > uscita_ospite
#             [------]                         SI
#                      [---------]             SI
#                    [--]                      SI
#             [------------------]             SI

