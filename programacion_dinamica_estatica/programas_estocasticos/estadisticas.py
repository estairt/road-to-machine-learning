import random
import math

def media(x):
    return sum(x)/len(x)


def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador +=(x-mu)**2

    return acumulador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))


if __name__ == "__main__":
    x = [random.randint(1,21) for i in range(20)]

    mu = media(x)

    Var = varianza(x)
    sigma = desviacion_estandar(x)


    print(f'Arreglo de x :{x}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion estandar = {sigma}')
