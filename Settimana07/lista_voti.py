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

    while voto!=0:
        voti.append(voto)

        voto = int(input("Inserisci un voto (0 per finire): "))
    return voti


def calcola_media(voti):
    """
    Calcola la media di una lista di voti

    :param voti: lista contenente i voti
    :return: valore della media
    """
    return sum(voti)/len(voti)

def calcola_30(voti):
    if 30 in voti:
        print("Il tuo primo 30 è: ", voti.index(30)+1)
    else:
        print("Non hai nessun 30")

def stampa_voti_ordinati(voti):
    # - i voti in ordine crescente

    # voti.sort() -> no perché perderei l'ordine di inserimento dei voti

    voti_ordinati = sorted(voti)
    # #oppure
    voti_ordinati = list(voti)
    voti_ordinati.sort()

    print(f'I voti in ordine crescente sono {voti_ordinati}')


def media_tranne_voto_peggiore(voti):
    peggiore = min(voti)

    # voti_senza_peggiore = list(voti)
    # voti_senza_peggiore.remove(peggiore)
    # return calcola_media(voti_senza_peggiore)

    return (sum(voti)-peggiore)/(len(voti)-1)


def media_tranne_2peggiori(voti):
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
    return calcola_media(voti[-4:])


def main():
    # voti = leggi_voti()  # leggi dall'utente
    voti = [21, 23, 30, 28, 28, 18, 30]
    media = calcola_media(voti)
    print(f'Media = {media}')
    calcola_30(voti)
    stampa_voti_ordinati(voti)
    media_senza_peggiore = media_tranne_voto_peggiore(voti)
    print(f'Media senza il peggiore = {media_senza_peggiore}')

# esegui il programma
main()
