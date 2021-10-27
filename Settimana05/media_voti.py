# Esercizio "media voti" (v. slide)

# - leggere il numero di esami/voti
n_esami = int(input("Quanti esami avete? "))

# -  se ci sono studenti da elaborare:

ancora_studenti = True
while ancora_studenti:

    print("Inserisci i voti")
    #     - leggere tutti i voti di uno studente
    somma = 0
    for n in range(n_esami):
        voto = int(input(f"Che voto hai per l'esame {n + 1}? "))
        somma = somma + voto
    print(f"La media è {somma / n_esami}")
    #     - calcolare e stampare la media dei suoi voti
    #
    #     - chiedere se ci sono altri studenti
    risp = input("Ancora studenti (s/n)? ")
    if risp.lower() == 'n':
        ancora_studenti = False
