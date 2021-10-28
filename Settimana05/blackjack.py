# Soluzione esercizio "BlackJack" proposto sulle slide
import random

# punteggio = numero di mani vinte da ciascuno
punti_giocatore = 0
punti_banco = 0

ancora = True  # decide quando terminare il gioco

# RIPETI PER MOLTE 'MANI' DI GIOCO, FINCHÉ L'UTENTE NON TERMINA
while ancora:
    # GIOCA UNA SINGOLA MANO

    # il banco estrae la prima carta
    carta = random.randint(1, 10)
    print(f'BANCO: Ho pescato {carta}')
    carte_banco = carta

    # GIOCA IL GIOCATORE -> determina carte_giocatore
    print("TOCCA A TE")
    carte_giocatore = 0

    # dare prima carta
    carta = random.randint(1, 10)
    # carta = random.randrange(1, 11)
    # carta = int(random.random() * 10 + 1)
    print(f'Hai pescato {carta}')
    carte_giocatore = carta

    risp = 'hit'  # obbliga ad entrare nel ciclo, la prima volta
    while risp == 'hit':
        # dare seconda carta
        carta = random.randint(1, 10)
        print(f'Hai pescato {carta}')
        carte_giocatore = carte_giocatore + carta

        # hai sballato?
        if carte_giocatore > 21:
            print("Hai sballato!")
            risp = 'stay'  # forzo uscita dal ciclo
        else:
            # chiedi se vuole altre carte
            risp = input("Vuoi continuare (hit) o fermarti (stay)?").lower()
            while risp != 'hit' and risp != 'stay':
                print(f'Valore {risp} non ammesso, ripeti')
                risp = input("Vuoi continuare (hit) o fermarti (stay)?").lower()
            # se sì, dare le carte successive

    if carte_giocatore <= 21:
        # GIOCA IL BANCO -> determina carte_banco
        print(f"TOCCA AL BANCO (avevo già {carte_banco})")

        while carte_banco < 17 and carte_banco < carte_giocatore:
            carta = random.randint(1, 10)
            print(f'Ho pescato {carta}')
            carte_banco = carte_banco + carta

    # DETERMINA IL VINCITORE ED AGGIORNA I PUNTEGGI
    print(f'Giocatore: {carte_giocatore} / Banco: {carte_banco}')

    if carte_giocatore > 21:
        print('Vince il banco')
        punti_banco = punti_banco + 1
    elif carte_banco > 21:
        print('Hai vinto')
        punti_giocatore = punti_giocatore + 1
    elif carte_giocatore > carte_banco:  # nessuno ha sballato, giocatore ha più punti
        print('Hai vinto')
        punti_giocatore = punti_giocatore + 1
    else:  # nessuno ha sballato, banco ha più punti oppure gli stessi punti
        print('Vince il banco')
        punti_banco = punti_banco + 1

    print(f"PUNTEGGIO ATTUALE: Giocatore: {punti_giocatore} / Banco: {punti_banco}")

    risp = input("Vuoi continuare (s/n)? ").lower()
    while risp != 's' and risp != 'n':
        risp = input("RIPETI - Vuoi continuare (s/n)? ").lower()

    if risp == 'n':
        ancora = False
        if punti_giocatore > punti_banco:
            print("Sei il campione")
        elif punti_giocatore == punti_banco:
            print("Avete pareggiato")
        else:
            print("Ti ho battuto anche questa volta")
