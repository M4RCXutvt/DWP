from itertools import count

print("manejo de listas en python")

#declaracion de una lista
my_list= [1,2,3,4,5,6,7,8,9,10]
print(f'valores actuales de la lista{my_list}')
#AGregar elementos a la lista append, 8 y 11
my_list.append(0)
my_list.append(11)
print(f'valores modificados de mi lista{my_list}')
#Ordenar los elementos de mi lista medíante SORT
my_list.sort()
print(f'los elementos de la lista han sido ordenados {my_list}')
#Modificar y eliminar un elemento de mi lista
my_list[0] = 'esta es una cadena'
my_list.pop()
print(f'valores actuales de mi lista, ejemplom pop {my_list}')

#Creacion de una sublista [0:5]
my_sublist = my_list[0:5]
print(f'valores acrtuales de mi sublista {my_sublist}')
#Imprimir los valores de mi lista
print(f'estos son los elementos de mi lista, los cuales seran impresos mediante un ciclo for')
for item in my_list:
    print(f'elemento de mi lista {count} - {item} ')
    count =+1