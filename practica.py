nombre=str(input('Ingresa tu nombre: '))
print('\nHola',nombre)
edad=int(input('\nIngresa tu edad: '))
print('\n',nombre,edad)
if edad>18:
    print('Eres mayor de edad.')
elif edad<18:
    print('Eres menor de edad, ¿quieres continuar?')