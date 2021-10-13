from math import sqrt

cateto1 = float(input("Cateto 1: "))
cateto2 = float(input("Cateto 2: "))

if cateto1 <= 0:
    print("Il cateto 1 deve essere un numero positivo")
else:
    if cateto2 <= 0:
        print("Il cateto 2 deve essere un numero positivo")
    else:
        ipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
        print(f'Triangolo di lati {cateto1}, {cateto2} e {ipotenusa}')

###########################################################

if cateto1 <= 0:
    print("Il cateto 1 deve essere un numero positivo")
elif cateto2 <= 0:
    print("Il cateto 2 deve essere un numero positivo")
else:
    ipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
    print(f'Triangolo di lati {cateto1}, {cateto2} e {ipotenusa}')




###########################################################

if cateto1 <= 0 or cateto2 <= 0:
    print("Almeno uno dei cateti non era positivo")
else:
    ipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
    print(f'Triangolo di lati {cateto1}, {cateto2} e {ipotenusa}')

###########################################################


if cateto1 > 0:
    if cateto2 > 0:
        ipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
        print(f'Triangolo di lati {cateto1}, {cateto2} e {ipotenusa}')
    else:
        print("Il cateto 2 deve essere un numero positivo")
else:
    print("Il cateto 1 deve essere un numero positivo")

###########################################################

if cateto1 > 0 and cateto2 > 0:
    ipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
    print(f'Triangolo di lati {cateto1}, {cateto2} e {ipotenusa}')
else:
    print("Almeno uno dei cateti non era positivo")


# if cateto1 <= 0:
#     # ramo VERO della scelta
#     a
#     b
#     c
# else:
#     # ramo FALSO della scelta (cioè cateto1 > 0)
#     x
#     y
#     z
#
# # sono FUORI dalla scelta, verranno eseguite SEMPRE
# d
# e
# f
