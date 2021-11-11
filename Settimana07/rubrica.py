''

"""
Sviluppare un programma Python che permetta di gestire una rubrica di nomi.
Il "nome" può contenere qualsiasi sequenza di lettere alfabetiche e spazi.

Il programma permette all'utente di inserire una serie di comandi. Ciascun comando è 
costituito da un carattere iniziale, che può essere seguito da un nome (separato con uno spazio):

 i nome     -> inserisce un nuovo nome nella rubrica
 p          -> stampa (print) il contenuto della rubrica
 I nome,nome,nome  -> inserisce un gruppo di nomi (separati da ,) con un unico comando
 d nome     -> cancella il nome specificato (se esiste); in caso di duplicati, cancella il primo
 s          -> ordina la rubrica in ordine alfabetico
 2          -> ricerca se ci sono dei nomi duplicati
 + nome     -> sposta il nome una posizione più avanti nella rubrica
 - nome     -> sposta il nome una posizione più avanti nella rubrica
 0          -> stampa la prima lettera di ciascun nome
 x          -> termina il programma
"""

rubrica = []  # lista di stringhe che rappresenta il contenuto della rubrica

comando = input("Inserisci un comando: ")
comando = comando.strip()  # elimima spazi iniziali e finali
while comando != 'x':
    if len(comando) < 1:
        print("Comando troppo breve")
    # interpreta il comando ed eseguilo
    elif comando[0] == 'i':
        nome = comando[2:].strip()
        rubrica.append(nome)
    elif comando[0] == 'p':
        # print(f'Rubrica: {rubrica}')
        if len(rubrica) >= 1:
            # OK: tratto a parte (fuori dal ciclo) l'ultimo elemento
            # print('Rubrica: ', end='')
            # for nome in rubrica[:-1]:
            #     print(nome, end=', ')
            # print(rubrica[-1], end='.')
            # print() # a capo

            ## NON FUNZIONA SE CI SONO NOMI DUPLICATI!
            # print('Rubrica: ', end='')
            # for nome in rubrica:
            #     if nome==rubrica[-1]:  # sto per stampare l'ultimo nome
            #         print(nome, end='.')
            #     else:
            #         print(nome, end=', ')
            # print() # a capo

            # OK, tratto diversamente l'elemento se mi accorgo che è l'ultimo
            # print('Rubrica: ', end='')
            # for pos in range(len(rubrica)):
            #     if pos==len(rubrica)-1:  # sto per stampare l'ultimo nome
            #         print(rubrica[pos], end='.')
            #     else:
            #         print(rubrica[pos], end=', ')
            # print() # a capo

            stampare = ', '.join(rubrica)
            print(f'{stampare}.')
        else:
            print('Rubrica vuota')
    elif comando[0] == 'I':
        seq_nomi = comando[2:]
        # cerca le virgole e separa le stringhe
        lista_nomi = seq_nomi.split(',')

        # pulizia degli eventuali spazi intorno ai nomi
        for i in range(len(lista_nomi)):
            lista_nomi[i] = lista_nomi[i].strip()

        rubrica.extend(lista_nomi)
        # rubrica = rubrica + lista_nomi

        # ALGORITMO POSSIBILE
        # Aldo,Giovanni,Giacomo
        # pos=4 (seq_nomi.index(','))
        # inserisce nella rubrica seq_nomi[0:4]
        # cancella la parte iniziale -> seq_nomi = seq_nomi[5:]
    elif comando[0] == 'd':
        # delete
        nome = comando[2:].strip()

        if nome in rubrica:
            rubrica.remove(nome)
            # oppure
            # pos = rubrica.index(nome)  # cerca prima occorrenza dall'inizio

            # oppure: cerca la prima occorrenza dal fondo
            # pos = rubrica[::-1].index(nome)
            # pos = len(rubrica)-1 - pos

            # rubrica.pop(pos)
        else:
            print(f'Il nome {nome} non è presente')
    elif comando[0] == 's':
        rubrica.sort()
    elif comando[0] == '2':
        # trova se ci sono nomi duplicati
        pass  # DA FARE
    else:
        print(f'Comando {comando[0]} non supportato')

    comando = input("Inserisci un comando: ")
    comando = comando.strip()
