"""
Generiamo un programma con cui poter leggere un elenco di voti (terminando
con 0) e stampare una serie di informazioni su tali voti:
- media
- i voti in ordine crescente
- la media, escludendo il voto peggiore
- la media, escludendo i due voti peggiori
- la media degli ultimi 4 voti
"""


def leggi_voti():
    """
    Acquisisce da tastiera una serie di voti terminata da 0

    :return: la lista dei voti
    """
    voti = []

    voto = int(input("Inserisci un voto (0 per finire): "))

    while voto != 0:
        voti.append(voto)

        voto = int(input("Inserisci un voto (0 per finire): "))
    return voti


def calcola_media(voti):
    """
    Calcola la media di una lista di voti

    :param voti: lista contenente i voti
    :return: valore della media
    """
    return sum(voti) / len(voti)


def calcola_30(voti):
    """
    Determina quale sia il primo 30 ottenuto e lo stampa. Segnala anche se non ci fosse nessun 30.

    :param voti: voti da analizzare
    """
    if 30 in voti:
        print("Il tuo primo 30 è l'esame numero: ", voti.index(30) + 1)
    else:
        print("Non hai nessun 30")


def stampa_voti_ordinati(voti):
    """
    Ordina i voti e li stampa in ordine numerico crescente

    :param voti: voti ottenuti
    """
    # voti.sort() -> no perché perderei l'ordine di inserimento dei voti

    voti_ordinati = sorted(voti)
    # #oppure
    voti_ordinati = list(voti)
    voti_ordinati.sort()

    print(f'I voti in ordine crescente sono {voti_ordinati}')


def media_tranne_voto_peggiore(voti):
    """
    Calcola la media dei voti, dopo avere escluso il voto peggiore.

    :param voti: elenco dei voti
    :return: valore della media depurata
    """
    peggiore = min(voti)

    # voti_senza_peggiore = list(voti)
    # voti_senza_peggiore.remove(peggiore)
    # return calcola_media(voti_senza_peggiore)

    return (sum(voti) - peggiore) / (len(voti) - 1)


def media_tranne_2peggiori(voti):
    """
    Calcola la media dei voti, dopo avere escluso i due voti peggiori.

    :param voti: elenco dei voti
    :return: valore della media depurata
    """
    # voti_ordinati = sorted(voti)
    # voti_ordinati = voti_ordinati[2:]
    # return calcola_media(voti_ordinati)
    voti2 = list(voti)
    peggiore = min(voti2)
    voti2.remove(peggiore)
    peggiore = min(voti2)
    voti2.remove(peggiore)
    return calcola_media(voti2)


def media_ultimi4(voti):
    """
    Calcola la media degli ultimi 4 esami sostenuti, in ordine di inserimento.

    :param voti: elenco dei voti
    :return: valore della media
    """
    return calcola_media(voti[-4:])


def main():
    voti = leggi_voti()  # leggi dall'utente
    # voti = [21, 23, 30, 28, 28, 18, 30]
    media = calcola_media(voti)
    print(f'Media = {media}')
    calcola_30(voti)
    stampa_voti_ordinati(voti)
    media_senza_peggiore = media_tranne_voto_peggiore(voti)
    print(f'Media senza il peggiore = {media_senza_peggiore}')
    media_senza_2peggiori = media_tranne_2peggiori(voti)
    print(f'Media senza i 2 peggiori = {media_senza_2peggiori}')


# esegui il programma
main()
