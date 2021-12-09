# Leggere dei valori INTERI ed inserirli una lista

valori = []

dato = input('Dato: ')
while dato != '':
    try:
        d = int(dato)
        valori.append(d)
    except ValueError as errore:
        # arrivo qui se una delle istruzioni del blocco precedente
        # ha generato un'eccezione di tipo ValueError
        print(f'Il valore {dato} non è un numero correttamente formattato. Riprova.')
        # dato = input('Re-inserisci il dato: ')
        print('Messaggio di errore: ', str(errore))

    dato = input('Dato: ')


print(valori)
