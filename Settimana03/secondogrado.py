"""
Risoluzone equazioni di secondo grado.

Il programma riceve in input i coefficienti a, b, c (numeri reali) e calcola e stampa le soluzioni reali della
equazione ax²+bx+c=0, considerando tutti i possibili casi particolari.
"""

# 1. Acquisizione dei dati
import math

print("Risoluzione equazione ax²+bx+c=0")

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# 2. Verifica se l'equazione è effettivamente di secondo grado

if a != 0.0:
    # 2.1. Secondo grado
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Non esistono soluzioni perché il discriminante è negativo")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Esiste una soluzione doppia poiché il discriminante è nullo: x = {x}")
    else:
        # caso normale: Δ=0
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"L'equazione ha due soluzioni: x₁ = {x1} e x₂ = {x2}")

else:
    # 2.2. Primo grado, nella forma bx+c=0
    if b == 0.0:
        # Forma degenere: c=0
        if c == 0.0:
            print(f"L'equazione è degenere {c} = 0, non ammette soluzioni (impossibile)")
        else:
            print(f"L'equazione è degenere {c} = 0, ammette infinite soluzioni (indeterminata)")
    else:
        x = -c / b
        print(f"L'equazione è di primo grado {b}x+{c}=0, la soluzione è x = {x}")
