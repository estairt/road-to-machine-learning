user_1 = input('Ingrese el nombre del primer usuario : ')
age_1 = int(input('Ingrese la edad del primer usuario : '))
user_2 = input('Ingrese el nombre del segundo usuario : ')
age_2 = int(input('Ingrese la edad del segundo usuario : '))

if age_1 > age_2:
    print(f'{user_1} es mayor que {user_2}')
elif age_1 < age_2:
    print(f'{user_1} es menor que {user_2}')
else:
    print(f'{user_1} tiene la misma edad que {user_2}')