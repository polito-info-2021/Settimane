# - Dati di partenza:
#     - lunghezza del muro, in cm (LUNGHEZZA_MURO)
#     - lato della piastrella (supponiamo quadrata), in cm (DIM_PIASTRELLA)
# - Requisiti di progetto:
#     - riempire al meglio lo spazio disponibile
#     - iniziare e terminare con una piastrella nera
#     - lasciare lo stesso spazio a sinistra e destra
# - Dati da calcolare:
#     - numero di piastrelle bianche, nere e totali (num_piastrelle)
#     - spazio da lasciare in ciascun lato, in cm  (spazio_vuoto)
#
# ESEMPIO
# LUNGHEZZA_MURO = 310 cm
# DIM_PIASTRELLA = 25 cm
#
# |...[N] [B][N] [B][N] [B][N]...|
#
# spazio occupato dalle piastrelle : ( 1 + 2 bianche ) * DIM_PIASTRELLA
# piastrelle totali = numero nere + numero bianche = (numero bianche + 1)  + numero bianche
# spazio occupato =?= LUNGHEZZA_MURO
# piastrelle totali = LUNGHEZZA_MURO / DIM_PIASTRELLA ==> frazionario, pari o dispari
# 310 cm / 25 cm = 12.4 'piastrelle'
# ==> 11 piastrelle totali, di cui 5 bianche e 6 nere
# ==> il più grande numero dispari minore o uguale a 12.4
# piastrelle_totali = int(LUNGHEZZA_MURO / DIM_PIASTRELLA)  ==> 12
# se piastrelle_totali è pari, allora piastrelle_totali = piastrelle_totali - 1  ==> 11
# bianche = (piastrelle_totali-1)/2  ==> 5
#
#
# ALTERNATIVA
# coppie di piastrelle = (LUNGHEZZA_MURO-DIM_PIASTRELLA) / (2*DIM_PIASTRELLA)
#
# ALTERNATIVA
# per ciascun numero dispari 'n'
#     verifica se DIM_PIASTRELLA*n < LUNGHEZZA_MURO
#         sì -> continua a incrementare n
#         no -> il valore precedente di n è la risposta


# DEFINISCO I DATI DI INGRESSO
LUNGHEZZA_MURO = 100
DIM_PIASTRELLA = 33

# CALCOLO NUMERO DI PIASTRELLE BIANCHE, NERE, TOTALI
coppie_piastrelle = (LUNGHEZZA_MURO - DIM_PIASTRELLA) // (2 * DIM_PIASTRELLA)
# print(coppie_piastrelle)
bianche = coppie_piastrelle
nere = bianche + 1
num_piastrelle = bianche + nere

# CALCOLO SPAZIO DA LASCIARE AI LATI
spazio_vuoto = (LUNGHEZZA_MURO - num_piastrelle * DIM_PIASTRELLA) / 2

# STAMPO I RISULTATI OTTENUTI
print("Dato un muro di", LUNGHEZZA_MURO, "cm e una piastrella di", DIM_PIASTRELLA, "cm")
print("Dovrai posizionare", num_piastrelle, "piastrelle, di cui", bianche, "bianche e", nere, "nere")
print("Devi lasciare", spazio_vuoto, "cm da ciascun lato")
