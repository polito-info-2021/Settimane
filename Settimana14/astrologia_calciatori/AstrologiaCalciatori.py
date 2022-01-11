from operator import itemgetter


def leggi_calciatori():
    fileCalciatori = open("sportivi.csv", "r", encoding="UTF-8")
    calciatori = []

    for line in fileCalciatori:
        dati = line.rstrip().split(',')
        riga = []
        for i in range(len(dati)):
            riga.append(dati[i])
        calciatori.append(riga)

    fileCalciatori.close()
    return calciatori


def leggi_zodiaco():
    fileZodiaco = open("zodiaco.csv", "r", encoding="UTF-8")
    zodiaco = []

    for line in fileZodiaco:
        dati = line.rstrip().split(',')
        riga = []
        for i in range(len(dati)):
            riga.append(dati[i])
        zodiaco.append(riga)

    fileZodiaco.close()

    return zodiaco


# calciatore sappere il suo segno zodiaco
# summare i goal

def trova_segno(nascita, segni):
    segno_trovato = " "

    for segno in segni:
        gg_inizio = segno[1].split('/')[1] + segno[1].split('/')[0]
        gg_fine = segno[2].split('/')[1] + segno[2].split('/')[0]

        if (nascita >= gg_inizio) and (nascita <= gg_fine):
            segno_trovato = segno[0]
            return segno_trovato

    return "Capricorno"


def calcola_punti(segni, calcitori):
    punti = {}

    for j in range(len(segni)):
        punti[segni[j][0]] = 0

    for i in range(len(calcitori)):
        nato = calcitori[i][3].split('/')[1] + calcitori[i][3].split('/')[0]
        segno = trova_segno(nato, segni)
        punti[segno] = punti[segno] + int(calcitori[i][1])

    return punti


def main():
    calciatori = leggi_calciatori()
    zodiaco = leggi_zodiaco()
    punti = calcola_punti(zodiaco, calciatori)
    sorted_punti = sorted(punti.items(), key=itemgetter(1), reverse=True)

    # print(calciatori)
    # print(zodiaco)
    # print(sorted_punti)

    for i in range(len(sorted_punti)):
        asterischi = (sorted_punti[i][1] * 50)//sorted_punti[0][1]
        print(f'{sorted_punti[i][0]:10s} ({sorted_punti[i][1]:4d})', "*"*asterischi)


main()
