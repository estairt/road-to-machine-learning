def nombre_completo(nombre,apellido,inverso=False):
    if inverso:
        return f'{apellido},{nombre}'
    else:
        return f'{nombre},{apellido}'


print(nombre_completo('Sebastian','Cornejo'))
print(nombre_completo('Sebastian','Cornejo',True))
print(nombre_completo('Sebastian','Cornejo',inverso=True))
print(nombre_completo(apellido='Cornejo',nombre='Seba',inverso=True))