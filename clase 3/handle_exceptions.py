result = None
numero_x = 10
numero_y = 0


try:

    numero_x = int(input('ingresa un numero para X'))
    numero_y = int(input('ingresa un numero para Y'))
    result= numero_x / numero_y
    print(f'el resultado de la division es: {result}')
except ZeroDivisionError as e:
    print(f'la excepcion es la siguiente: {e}')
except ValueError as e:
    print(f'la excepcion de Valuerror  es la siguiente: {e}')
except Exception as e:
    print(f'la excepcion  Exception de Valuerror  es la siguiente: {e}')
finally:
    print('nuestro programa ha finalizado')