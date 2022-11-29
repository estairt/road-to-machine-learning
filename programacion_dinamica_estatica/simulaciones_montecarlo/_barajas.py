from copyreg import constructor
from pickle import TRUE
import random
import collections


PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7',
           '8', '9', '10', 'jota', 'reina', 'rey']


def crear_baraja():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano


def escaleras(manos, intentos):
    escalera = 0
    escalera_color = 0
    escalera_real = 0

    for mano in manos:
        numeros_mano = []
        palo = ""
        es_mismo_palo = True
        es_escalera = True
        es_real = False

        for carta in mano:
            if palo == "":
                palo = carta[0]
            elif palo != carta[0]:
                es_mismo_palo = False

            match carta[1]:
                case 'as':
                    numeros_mano.append(1)
                case 'jota':
                    numeros_mano.append(11)
                case 'reina':
                    numeros_mano.append(12)
                case 'rey':
                    numeros_mano.append(13)
                case _:
                    numeros_mano.append(int(carta[1]))

        numeros_mano.sort()

        numero_anterior = 0
        for n in numeros_mano:
            if numero_anterior == 0:
                numero_anterior = n
                continue

            if numero_anterior == 1 and n == 10:
                es_real = True

            if numero_anterior == 1 and n != 10 and numero_anterior + 1 != n or numero_anterior != 1 and numero_anterior + 1 != n:
                es_escalera = False
                break

            numero_anterior = n

        if es_escalera:
            escalera += 1
        if es_mismo_palo and es_escalera and es_real:
            escalera_real += 1
        elif es_mismo_palo and es_escalera:
            escalera_color += 1
        elif es_mismo_palo:
            

    print(f'contador escalera {escalera}')
    print(f'contador escalera color  {escalera_color}')
    print(f'contador escalera_real  {escalera_real}')
    probabilidad_escalera = escalera / intentos
    probabilidad_escalera_color = '{:.7f}'.format(escalera_color / intentos)
    probabilidad_escalera_real = '{:.8f}'.format(escalera_real / intentos)

    return probabilidad_escalera, probabilidad_escalera_color, probabilidad_escalera_real


def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    probabilidad_escalera, probabilidad_escalera_color, probabilidad_escalera_real = escaleras(
        manos, intentos)

    print(
        f'La probabilidad de obtner una escalera en una mano de {tamano_mano} barajas es {probabilidad_escalera} ')
    print(
        f'La probabilidad de obtner una escalera color en una mano de {tamano_mano} barajas es {probabilidad_escalera_color} ')
    print(
        f'La probabilidad de obtner una escalera real en una mano de {tamano_mano} barajas es {probabilidad_escalera_real} ')
    # pares = 0
    # for mano in manos:
    #     valores = []
    #     for carta in mano:
    #         valores.append(carta[1])

    #     counter = dict(collections.Counter(valores))
    #     for val in counter.values():
    #         if val == 2:
    #             pares += 1
    #             break

    # probabilidad_par = pares / intentos
    # print(
    #     f'La probabilidad de obtern un par en una mano de {tamano_mano} barajas es {probabilidad_par} ')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)
