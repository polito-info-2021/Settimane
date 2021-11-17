s = ['Tom', 'Jerry', 'Qui', 'Quo', 'Jerry', 'Qua']
#                                     ^^i

n = 0  # numero di coppie uguali che ho trovato
# m = 0  # numero di coppie non uguali che ho trovato --- mi serve???
for i in range(0, len(s)):
    for j in range(0, i):
        # 1,0   2,0   2,1    3,0   3,1    3,2 ... --> (len*(len-1))/2
        print(f'- confronto {s[i]} con {s[j]}')
        if s[i] == s[j]:
            n = n + 1
        # else:
        #     m = m + 1
    # for j in range(i+1, len(s)):
    #         print(f'+ confronto {s[i]} con {s[j]}')
    #         if s[i] == s[j]:
    #             n = n + 1
    #         else:
    #             m = m + 1


# versione "pulita" e corretta
n = 0  # numero di coppie uguali che ho trovato
for i in range(0, len(s)):
    for j in range(0, i):
        if s[i] == s[j]:
            n = n + 1



# ALTERNATIVA per prendere tutte le coppie (nei due versi) senza fare due loop per la parte sinistra e destra
# for i in range(0, len(s)):
#     for j in range(0, len(s)):
#         if i != j:
#             if s[i] == s[j]:
#                 n = n + 1

if n != 0:
    print("C'è almeno un duplicato!")
else:
    print("Non ci sono duplicati!")
