name  = 'John Wayne John John'

# Cerca la SECONDA occorrenza di 'n' nel nome
cerca = 'n'

if name.count(cerca)>=2:
    # ci sono almeno 2 occorrenze -> cercala
    prima_pos = name.find(cerca)
    seconda_pos = name[prima_pos+1:].find(cerca) + prima_pos+1
    print(f'Ho trovato {cerca} alle posizioni {prima_pos} e {seconda_pos}')
    print(f'INFATTI: {name[prima_pos]} / {name[seconda_pos]}')
else:
    print(f'La stringa {cerca} non compare 2 volte')
