si='si'
no='no'
nombre=str(input('Ingresa tu nombre: '))
edad=int(input('\nIngresa tu edad: '))
print('\n',nombre,edad)
print('\nHola',nombre)
if edad>18:
    print('Eres mayor de edad.')
elif edad<18:
    print('Eres menor de edad.')
    ask=input('¿Quieres continuar?: ')
    if ask==si:
        print('Bienvenido',nombre)
    else:
        input('Presiona enter para salir.')