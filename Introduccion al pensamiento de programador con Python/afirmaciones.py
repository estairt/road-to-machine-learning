def primera_letra(lista_de_palabras):
    primera_letras = []

    for palabra in lista_de_palabras:
        
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primera_letras.append(palabra[0])

    return primera_letras


print(primera_letra(['hola','2']))