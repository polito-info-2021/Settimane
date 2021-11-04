# Soluzione esercizio 4.7
import random


def mossa_intelligente(biglie):
    if biglie == 63 or biglie == 31 or biglie == 15 or biglie == 7 or biglie == 3:
        return random.randint(1, max(biglie // 2, 1))
    if biglie > 63:
        return biglie - 63
    elif biglie > 31:
        return biglie - 31
    elif biglie > 15:
        return biglie - 15
    elif biglie > 7:
        return biglie - 7
    elif biglie > 3:
        return biglie - 3
    else:
        return 1

# Suggerimento alternativo:
#     if not log2(b+1).is_integer():    #ossia se b NON è una potenza di 2 -1
#         power = int(log2(b)) #potenza
#         pcprende = b + 1 - 2**power
#         print("Il computer prende", pcprende, "biglie")
#         b = b - pcprende #b = biglie totali


biglie = random.randint(10, 100)  # dimensione iniale del mucchio
print(f'Partita a NIM con {biglie} biglie')

if random.randint(0, 1) == 0:
    turno_giocatore = True
else:
    turno_giocatore = False

# modalità di gioco del computer
if random.randint(0, 1) == 0:
    intelligente = False
else:
    intelligente = True

while biglie > 0:  # partita in corso
    if turno_giocatore:
        # fai fare la mossa al giocatore
        print(f"Giocatore: ci sono {biglie} biglie")
        prendi = int(input("Quante biglie prendi? "))
        while prendi < 1 or prendi > max(biglie // 2, 1):
            prendi = int(input("Errore: Quante biglie prendi? "))
        biglie = biglie - prendi
    else:
        # mossa del computer
        print(f"Computer: ci sono {biglie} biglie")
        if intelligente:
            prendi = mossa_intelligente(biglie)
        else:
            # stupido: numero a caso tra 1 e biglie//2
            if biglie == 1:
                prendi = 1
            else:
                prendi = random.randint(1, biglie // 2)
        print(f'Ho preso {prendi} biglie')
        biglie = biglie - prendi
    turno_giocatore = not turno_giocatore

if turno_giocatore == True:
    print("Ha vinto il giocatore")
else:
    print("Ha vinto il computer")
