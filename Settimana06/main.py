# Programma principale per l'esempio dei cubi
from cubo import volume_cubo

lato = float(input("Lato: "))
volume = volume_cubo(lato)
print(f'Il volume vale {volume}')
