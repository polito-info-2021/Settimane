def sumsq(values):
    total = 0
    for val in values:
        total = total + val**2
    return total

def eleva2(values):
    for i in range(len(values)):
        values[i] = values[i]**2

def numeripari(values):
    pari = []
    for val in values:
        if val%2==0:
            pari.append(val)
    return pari

values = [ 3, 6, 7, 8, 10 ]

somma = sumsq(values)

eleva2(values)

valori_pari = numeripari(values)
