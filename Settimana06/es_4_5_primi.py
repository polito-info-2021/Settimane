# Soluzione esercizio 4.5+

n = int(input("Valore max: "))

for i in range(2, n + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False

    if primo:
        print(i)
