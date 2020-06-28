import random

def ordenamiento_de_burbuja(list):
    n = len(lista)

    for i in range(n):
        for j in range(0,n-i-1):

            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]

    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    list_ordenada = ordenamiento_de_burbuja(lista)
    print(list_ordenada)