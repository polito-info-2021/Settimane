# Calcola entro quanti anni un capitale raddoppia

cap_iniziale = float(input("Capitale iniziale: "))
tasso = float(input("Tasso di interesse (%): "))

cap_finale = 2 * cap_iniziale
#
# capitale anno 2 = capitale anno 1 + capitale anno 1 * tasso interesse
#
# capitale anno 3 = capitale anno 2 + capitale anno 2 * tasso interesse

# variabile di controllo: 'capitale'
capitale = cap_iniziale
anni = 0
while capitale < cap_finale:
    nuovo_capitale = capitale + capitale*tasso/100.00
    # calcolo il capitale a fine anno partendo da quello a inizio anno
    anni = anni + 1

    capitale = nuovo_capitale
    # il capitale di INIZIO del PROSSIMO anno è uguale a quello di FINE dell'anno corrente

print(f'Dopo {anni} anni il capitale finale è {capitale}')
