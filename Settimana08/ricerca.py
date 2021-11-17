values = [10, 200, 17, 34, 130, 199, 150, 8]
limit = 100

posizioni = []
for pos in range(len(values)):
    if values[pos] > limit:
        posizioni.append(pos)

result = []
for element in values:
    if element > limit:
        result.append(element)

print('Dove sono?', posizioni)
print('Quanti sono?', len(posizioni))
print('Quali sono?', result)

print('Quali sono?')
# values[ posizioni[1] ]
for i in range(len(posizioni)):
    print(values[posizioni[i]])
for pos in posizioni:
    print(values[pos])

# ELIMINA TUTTI I VALORI >100

print("PROVO A CANCELLARE")

# ERRORI FREQUENTI: ***** mai modificare una lista *****
# sulla quale si sta iterando con un for
# print(values)
# for element in values:
#     if element>limit:
#         values.remove(element)  # cancella elemento con valore 'element'

# for pos in range(len(values)):
#     if values[pos]>limit:
#         values.pop(pos)  # cancella elemento in posizione 'pos'
# print(values)

print(values)
pos = 0
while pos<len(values):
    if values[pos]>limit:
        values.pop(pos)
    else:
        pos = pos+1
print(values)

# IDEA: elimino da values tutti i valori che sono in result (quelli da cancellare)
for elemento_da_cancellare in result:
    values.remove(elemento_da_cancellare)

for pos in posizioni[::-1]:  # [1, 4, 5, 6]
    values.pop(pos)
    # [10, 200, 17, 34, 130, 8]

# IDEA: costruisco una nuova lista che contiene solo i valori
# che devono sopravvivere

new_values = []
for element in values:
    if not element>limit:
        new_values.append(element)

new_values = [element for element in values if not element>limit]
