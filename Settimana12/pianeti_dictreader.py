import csv
from pprint import pprint


def converti_float(pianeta):
    pianeta['massa'] = float(pianeta['massa'])
    pianeta['diametro'] = float(pianeta['diametro'])
    pianeta['densita'] = float(pianeta['densita'])
    pianeta['gravita'] = float(pianeta['gravita'])
    pianeta['velocita_fuga'] = float(pianeta['velocita_fuga'])
    pianeta['rotazione'] = float(pianeta['rotazione'])

    pianeta['giorno'] = float(pianeta['giorno'])
    pianeta['distanza'] = float(pianeta['distanza'].rstrip('*'))
    pianeta['perielio'] = float(pianeta['perielio'].rstrip('*'))
    pianeta['afelio'] = float(pianeta['afelio'].rstrip('*'))
    pianeta['periodo'] = float(pianeta['periodo'])

    pianeta['velocita'] = float(pianeta['velocita'])
    pianeta['inclinazione'] = float(pianeta['inclinazione'])
    pianeta['eccentricita'] = float(pianeta['eccentricita'])
    pianeta['tilt'] = float(pianeta['tilt'])
    pianeta['temperatura'] = float(pianeta['temperatura'])

    try:
        pianeta['pressione'] = float(pianeta['pressione'])
    except ValueError:
        pianeta['pressione'] = None
    pianeta['lune'] = float(pianeta['lune'])


pianeti = []
pianeti_diz = {}

# Planet,Mass (10**24kg),Diameter (km),Density (kg/m**3),Gravity (m/s**2),Escape Velocity (km/s),Rotation Period (hours),
# Length of Day (hours),Distance from Sun (10**6 km),Perihelion (10**6 km),Aphelion (10**6 km),Orbital Period (days),
# Orbital Velocity (km/s),Orbital Inclination (degrees),Orbital Eccentricity,Axial Tilt (degrees),Mean Temperature (C),
# Surface Pressure (bars),Number of Moons,Ring System?,Global Magnetic Field?
nomi_colonne = ['nome', 'massa', 'diametro', 'densita', 'gravita', 'velocita_fuga', 'rotazione',
                'giorno', 'distanza', 'perielio', 'afelio', 'periodo',
                'velocita', 'inclinazione', 'eccentricita', 'tilt', 'temperatura',
                'pressione', 'lune', 'anelli', 'campo_magnetico']

with open('planets.csv', 'r', encoding='utf-8') as infile:

    infile.readline() # ignora la prima riga

    reader = csv.DictReader(infile, fieldnames=nomi_colonne)

    for pianeta in reader:
        converti_float(pianeta)



        pianeti.append(pianeta)
        pianeti_diz[pianeta['nome']] = pianeta

pprint(pianeti)
pprint(pianeti_diz)


# Determina il pianeta che ha la massima gravità

maxg = 0.0
nome_max = ''
for pianeta in pianeti:
    if pianeta['gravita'] > maxg:
        nome_max = pianeta['nome']
        maxg = pianeta['gravita']
print(f'La massima gravità si trova su {nome_max} e vale {maxg}')


