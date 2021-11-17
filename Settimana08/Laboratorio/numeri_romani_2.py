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


s = input('Inserire il numero romano: ')
s = s.upper()

totale = 0

while s != '':
    if len(s) == 1 or conversione(s[0]) >= conversione(s[1]):  # XX, XI, VI, CL
        totale += conversione(s[0])
        s = s[1:]  # tolgo il primo carattere
    else:  # IX, IV, VC
        totale += conversione(s[1]) - conversione(s[0])
        s = s[2:]  # tolgo i primi 2 caratteri
    print(s)

print(totale)
