def cancella_numeri_pari(values):
    # for pos in range(len(values)-1, -1, -1):
    #     if values[pos]%2==0:
    #         values.pop(pos)

    values[:] = [val for val in values if val%2!=0]

    # values.append(77)
    # values = values + [77]


numeri = [ 3, 4, 7, 5, 4, 2, 1 ]
cancella_numeri_pari(numeri)
