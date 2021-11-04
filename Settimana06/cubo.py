# definiamo una funzione che calcoli il volume di un cubo
# nome: volume_cubo
# argomenti: un argomento (float), lunghezza del lato
# valore di ritorno: il valore (float) del volume
import math


def volume_cubo(a):
    '''
    Calcola il volume di un cubo, dato il lato

    :param a: lunghezza del lato
    :return: volume del cubo
    '''
    v = a ** 3
    return v


def misura_ipercubo(lato, dimensioni=3):
    return lato ** dimensioni


def superficie_cubo(a):
    return 6 * a ** 2


def pitagora(c1, c2):
    return math.sqrt(c1 ** 2 + c2 ** 2)


# lato = float(input("Lato: "))
# volume = volume_cubo(lato)
# print(f'Il volume vale {volume}')

# ipotenusa = pitagora(3.0, 4.0)
# print(ipotenusa)
#
# ipotenusa = pitagora(2.5, 7)
# print(ipotenusa)

print('Area di un quadrato di lato 7: ', misura_ipercubo(7, 2))
print('Volume di un cubo di lato 7: ', misura_ipercubo(7, 3))
print('Volume di un cubo di lato 7: ', misura_ipercubo(7))
print('Misura di un ipercubo di lato 7: ', misura_ipercubo(7, 4))


def area_triangolo_rettangolo(cateto1=0, cateto2=0, ipotenusa=0):
    if ipotenusa == 0:
        return cateto1 * cateto2 / 2
    elif cateto1 == 0:
        cat1 = math.sqrt(ipotenusa**2-cateto2**2)
        return cat1 * cateto2 / 2
    elif cateto2==0:
        pass
    else:
        pass

area = area_triangolo_rettangolo(cateto1=3,  ipotenusa=5)

volume = volume_cubo(a=8)
