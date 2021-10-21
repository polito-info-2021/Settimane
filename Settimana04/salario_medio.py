# Acquisisci una serie di dati che rappresentano i salari
# in diversi anni, e calcola la media di tali valori
# L'inserimento dei dati termina quando si inserisce il
# valore 'sentinella' -1

# INIZIALIZZAZIONI NECESSARIE IN TUTTE LE VARIANTI SEGUENTI
somma = 0.0
conta = 0

# VARIANTE 1: INIZIALIZZAZIONE DELLA VARIABILE DI CONTROLLO CON UN DATO FASULLO
dato = 0.0  # valore iniziale fasullo, solo per entrare nel ciclo alla prima iterazione
while dato != -1:
    # Acquisisci un nuovo dato
    dato = float(input("Salario: "))
    if dato != -1:
        # Aggiorna somma e conteggio
        somma = somma + dato
        conta = conta + 1

# VARIANTE 2: LETTURA ANTICIPATA DEL PRIMO DATO
dato = float(input("Salario: "))  # Leggi il primo dato
while dato != -1:
    somma = somma + dato
    conta = conta + 1

    dato = float(input("Salario: "))  # Leggi il prossimo dato, per la prossima iterazione

# VARIANTE 3A: UTILIZZO DI UNA VARIABILE LOGICA (FLAG) PER CONTROLLARE IL CICLO
fine = False  # "Flag"
while not fine:  # fine==False
    dato = float(input("Salario: "))
    if dato == -1:
        fine = True
    else:
        somma = somma + dato
        conta = conta + 1

# VARIANTE 3B: UTILIZZO DI UNA VARIABILE LOGICA (FLAG) PER CONTROLLARE IL CICLO
continua = True  # "Flag"
while continua:  # continua==True
    dato = float(input("Salario: "))
    if dato == -1:
        continua = False
    else:
        somma = somma + dato
        conta = conta + 1

# VARIANTE 4: UTILIZZO DEL COSTRUTTO BREAK
while True:  # ciclo infinito
    dato = float(input("Salario: "))
    if dato == -1:
        break
    somma = somma + dato
    conta = conta + 1

# UTILIZZO DI UNA SENTINELLA DI TIPO STRINGA (ES: UNA RIGA VUOTA)
riga = input("Salario: ")
while riga != "":
    dato = float(riga)
    somma = somma + dato
    conta = conta + 1
    riga = input("Salario: ")

# print(f'{somma=} {conta=}')
# print(f'La somma vale {somma}')

# Calcola la media: somma/conteggio
if conta == 0:
    print("Nessuno stipendio inserito, impossibile calcolare la media")
else:
    media = somma / conta
    print(f"Lo stipendio medio vale {media}")
