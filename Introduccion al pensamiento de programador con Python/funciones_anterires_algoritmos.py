def enumeration(objetivo):
    respuesta = 0

    while respuesta **2 < objetivo:
        #print(respuesta)
        respuesta +=1

    if respuesta** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'El {objetivo} no tiene una raiz cuadrada exacta')


def binary_search(objetivo):
    epsilon = 0.00001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        #print(f'bajo ={bajo}, alto={alto}, respuesta ={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def approach(objetivo):
    epsilon = 0.001
    paso = epsilon **2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
       #print(abs(respuesta**2 -objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')  


option = int(input('Ingrese una de las siguientes opciones para encontrar la raiz cuadrada \n 1) enumeracion \n 2) aproximacion \n 3) binaria \n :'))
objetivo = int(input('Ingrese un numero: '))

if option == 1:
    enumeration(objetivo)
elif option == 2:
    approach(objetivo)
elif option == 3:
    binary_search(objetivo)
else:
    print('debe ingresar una opcion valida')