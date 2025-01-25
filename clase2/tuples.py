print('ejemplo con tuplas')

#definicion de una tupla

tupla_informacion = ('ana picapiedra', 22, 95.5)
print(f'infromacion de la tupla: {tupla_informacion}')

#destructuraciono unpacking
full_name, age, salary = tupla_informacion
print(f' numbre {full_name} , age {age}, salaryc {salary}')

print('impresion de la tupla con un cilo for')
#impresion de los elementos de una tupla
for item in tupla_informacion:
    print(item)
