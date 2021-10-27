# stampare i numeri da 1 a 10

print("VERSIONE A")
for i in range(10):  # crea la sequenza 0, 1, 2, 3,...9
    print(i + 1)

print("VERSIONE B")
for i in range(1, 11):  # crea 1, 2, 3,...., 10
    print(i)

print("NUMERI QUADRATI")

# stampare i quadrati dei primi 5 numeri naturali partendo da 1
for n in range(1, 6):  # sequenza: 1, 2, 3, 4, 5
    n2 = n * n
    print(n2)  # print(n*n)

print(f'alla fine, n vale {n}')

for n in range(5):  # sequenza: 0, 1, 2, 3, 4
    n2 = (n + 1) * (n + 1)
    print(n2)  # print(n*n)

#
s = "Ciao"

for ch in s:
    print(ch)

print(f'ultimo carattere era {ch}')
#
# i = 0
# while i<10:
#     print(i+1)
#     i = i+1

for i in range(0):
    print("Il mio prof è cattivo")
for ch in "":
    print("nessun carattere")
