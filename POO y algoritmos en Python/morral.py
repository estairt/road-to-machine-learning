

def morral(tamano_morral, pesos, valores, n,llamada='entrada'):
    print(f'llamada  {llamada}')
    print('-'*50)

    if n == 0 or tamano_morral == 0:
        return 0
       
    print(f'Tamaño del morral {tamano_morral}')
    print(f'Pesos actual {pesos[n - 1]}')
    print(f'Valor actual {valores[n-1]}')
    print('*'*50)
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n - 1,llamada='izquierda'),
               morral(tamano_morral, pesos, valores, n - 1,llamada='derecha'))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 60
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
