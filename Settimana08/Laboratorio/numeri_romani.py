# Soluzione

def conversione(l):
    if l == 'M':
        v = 1000
    elif l == 'D':
        v = 500
    elif l == 'C':
        v = 100
    elif l == 'L':
        v = 50
    elif l == 'X':
        v = 10
    elif l == 'V':
        v = 5
    elif l == 'I':
        v = 1
    return v


str = input('Inserire il numero romano: ')
str = str.upper()

list = []


for letter in str:
    list.append(conversione(letter))
print(list)    #opzionale

x = 0  # posizione della cifra da convertire
y = 1  # posizione della cifra successiva  -> x+1
while y < len(list):
    if list[x] < list[y]:
        list[x] = -1 * list[x]
    print(list)
    x = x+1
    y = y+1


tot = sum(list)
print(f'totale: {tot}')
