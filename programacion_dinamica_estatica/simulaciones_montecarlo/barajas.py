import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7',
           '8', '9', '10', 'jota', 'reina', 'rey']

VALORES_ALFABETICOS = {'as': 1, 'jota': 11, 'reina': 12, 'rey': 13}


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def escaleras(manos):
    escalara_real = 0
    escalera_color = 0
    escalera = 0

    for mano in manos:
        palo = mano[0][0]
        mismo_palo = True
        escalera = True
        mano_num = []
        valores = []

        for carta in mano:
            if carta[0] != palo:
                mismo_palo = False

            for value, key in VALORES_ALFABETICOS.items():
                if carta[1] == key:
                    carta[1] == value
                    break
            valores.append(carta[1])

        valores.sort()

        for val, key in valores:
            if (val+1) != valores[key+1]:
                escalera = False


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))

        print(counter)
        for val in counter.values():
            if val == 4:
                pares += 1
                break

    probabilidad_par = pares / intentos

    #print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


if __name__ == "__main__":
    tamano_mano = int(input('De cuantas barajas sera la mano : '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad : '))

    main(tamano_mano, intentos)
