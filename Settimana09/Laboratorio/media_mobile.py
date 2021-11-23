# Laboratorio 7, Esercizio 7, Media Mobile

misure = [1, 2, 3, 2, 1, 1, 4, 6, 8, 7, 6, 5, 6, 5, 4, 3, 2, 9]

"""
IDEA
misure_corrette[0] = (misure[i]                 + misure[i + 1]) / 2
misure_corrette[i] = (misure[i] + misure[i - 1] + misure[i + 1]) / 3
misure_corrette[-1] = (misure[-1] + misure[-2]                 ) / 2
"""

misure_corrette = []
for i in range(len(misure)):
    if i == 0:
        misure_corrette.append((misure[0] + misure[1]) / 2)
    elif i == len(misure) - 1:
        misure_corrette.append((misure[-1] + misure[-2]) / 2)
    else:
        misure_corrette.append((misure[i] + misure[i - 1] + misure[i + 1]) / 3)

# misure_corrette = [0] * len(misure)  # [0,0,0,0,0,0,0...]
# # misure_corrette = [None] * len(misure)
#
# for i in range(len(misure)):
#     if i == 0:
#         misure_corrette[0] = (misure[0] + misure[1]) / 2
#     elif i == len(misure) - 1:
#         misure_corrette[-1] = (misure[-1] + misure[-2]) / 2
#     else:
#         misure_corrette[i] = (misure[i] + misure[i - 1] + misure[i + 1]) / 3

print(misure_corrette)


## PROVO A MODIFICARE LA STESSA LISTA DI PARTENZA

# [1, 2, 3, 2, 1, 1, 4, 6, 8, 7, 6, 5, 6, 5, 4, 3, 2, 9]
# [1.5, 2, 3, 2, 1, 1, 4, 6, 8, 7, 6, 5, 6, 5, 4, 3, 2, 9]
# [1.5, 2.166, 3, 2, 1, 1, 4, 6, 8, 7, 6, 5, 6, 5, 4, 3, 2, 9]


for i in range(len(misure)):
    if i == 0:
        precedente = misure[0]
        misure[0] = (misure[0] + misure[1]) / 2
    elif i == len(misure) - 1:
        misure[-1] = (misure[-1] + precedente) / 2
    else:
        temp = misure[i]
        misure[i] = (misure[i] + precedente + misure[i + 1]) / 3
        precedente = temp

print(misure)
