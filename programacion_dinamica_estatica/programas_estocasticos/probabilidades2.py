import random

def graficar():
    pass

def tirar_dado(numero_de_tiradas):
    secuencias_de_tiros = []
    # Un dado
    # for _ in range(numero_de_tiradas):
    #     tiro = random.choice([1, 2, 3, 4, 5, 6])
    #     secuencias_de_tiros.append(tiro)

    # Dos daddos
    for _ in range(numero_de_tiradas):
        dado_1 = random.choice([1, 2, 3, 4, 5, 6])
        dado_2 = random.choice([1, 2, 3, 4, 5, 6])
        secuencias_de_tiros.append(dado_1 + dado_2)
    
    return secuencias_de_tiros


def main(numero_de_tiradas, numero_de_intentos, numero_elegido):
    tiros = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiradas)
        tiros.append(secuencia_de_tiros)

    tiros_con = 0
    # De tener un 1
    # for tiro in tiros:
    #     if 1 in tiro:
    #         tiros_con_1 += 1

    # #  De no tener 1
    # for tiro in tiros:
    #     if 1 not in tiro:
    #         tiros_con_1 += 1

    for tiro in tiros:
        if numero_elegido in tiro:
            tiros_con += 1

    probabilidad_tiros_con_1 = tiros_con / numero_de_intentos

    print(
        f'Probabilidad de obtenr por lo menos un {numero_elegido} en {numero_de_tiradas} tiros = {probabilidad_tiros_con_1}')


if __name__ == "__main__":
    numero_elegido = int(
        input("Ingresa el numero que quieres probar que aparesca : "))
    numero_de_tiradas = int(input("Cuantos tiros del datos: "))
    numero_de_intentos = int(input("Cuantas veces correar la simulacion: "))

    main(numero_de_tiradas, numero_de_intentos, numero_elegido)
