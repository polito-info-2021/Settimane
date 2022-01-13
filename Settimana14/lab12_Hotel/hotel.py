from operator import itemgetter


def leggi_presenze():
    """
    Acquisisci dal file presenze.txt i dati sugli ospiti dell'hotel,
    memorizzandoli in una lista di dizionari
    :return: lista di dizionari {nome, tel, ingresso, uscita}
    """
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
    """
    Acquisisce dal file sospetti.txt i nomi dei sospetti, costruendo una lista di stringhe
    :return: lista di stringhe contenenti i nomi dei sospetti
    """
    with open('sospetti.txt', 'r', encoding='utf-8') as file:
        sospetti = file.readlines()
    for i in range(len(sospetti)):
        sospetti[i] = sospetti[i].rstrip()
    return sospetti


def cerca_contatti(ospite, presenze):
    """
    Determina se un ospite ha avuto dei contatti, controllando le sovrapposizioni
    tra i giorni di permanenza in hotel
    :param ospite: il nome (stringa) di un singolo ospite
    :param presenze: l'elenco completo delle presenze
    :return: se l'ospite non è in archivio: None. Se l'ospite non ha avuto contatti: [].
    Se l'ospite ha avuto contatti: una lista di presenze.
    """
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

            # verifico se 'presenza' è da considerarsi come un contatto
            # condizione 1: 'presenza' non è lo stesso di 'ospite' (non devo controllare
            # con me stesso
            # condizione 2: le date dicono che c'è stata una sovrapposizione
            # (vedi nota in fondo al file per la spiegazione)
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

# DETERMINAZIONE DELL'AVVENUTA SOVRAPPOSIZIONE O MENO:
# Indichiamo con [---] il periodo di permanenza di una persona:
#
# ospite          [--------]
#
# Le varie condizioni in cui i potrà trovare un 'altro', rispetto
# a quelle dell'ospite (qui sopra) sono tutte e sole le 6 seguenti:
#
# altro1    [---]                              NO   uscita_altro < ingresso_ospite
# altro2                       [----]          NO   ingresso_altro > uscita_ospite
# altro3      [------]                         SI
# altro4               [---------]             SI
# altro5             [--]                      SI
# altro6      [------------------]             SI
#
# Le condizioni con SI dicono che c'è stata una sovrapposizione, quelle con NO dicono
# che non ci può essere stata.
# Quindi:
#  non sovrapposizione = uscita_altro < ingresso_ospite or ingresso_altro > uscita_ospite
#  sovrapposizione = not( quello di sopra ^^ )


# STRUTTURA DATI UTILIZZATA:
# LISTA DI DIZIONARI
#
# [
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     { 'nome': 'Anna Rossi', 'tel': '23432432', 'ingresso': 100, 'uscita': 105},
# ]

# ALTRA POSSIBILE STRUTTURA DATI (non utilizzata qui):
# DIZIONARIO (chiave=nome) di DIZIONARI (record presenza)
# {
#     'Anna Rossi': {'tel': '23432432', 'ingresso': 100, 'uscita': 105},
#     'Giuseppe Verdi': {'tel': '23432432', 'ingresso': 100, 'uscita': 105}
# }
