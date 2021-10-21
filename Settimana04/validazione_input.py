# Leggi un dato da tastiera, garantendo che sia compreso tra 1 e 100

# Se il dato è errato, interrompi il programma
value = float(input("Valore: "))

if value < 1 or value > 100:
    print("errore")
else:
    print(value)

# Se il dato è errato, chiedi di re-inserirlo
valid = False
while not valid:
    riga = input("Valore: ")
    value = float(riga)

    if 1 <= value <= 100:
        valid = True
    else:
        print("Valore errato, riprova")

# qui sono SICURO che 'value' sia tra 1 e 100
