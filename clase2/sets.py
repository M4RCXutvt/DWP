print('ejemplo de uso de selecciones tipo SET')

#deifinir ejemplos con colecciones
first_collection = {1,2,3,4,5}
second_collection = {3,4,5,6,7,8}

print(f'mi coleccion tipo set {type(first_collection)}')

#remover un elemento de la coleccion REMOVE
first_collection.remove(4)
print(f'mi coleccion actualizada {first_collection}')

#agregar un elemento a la coleccion ADD
first_collection.add('hola mundo')
print(f'mi coleccion actualizada ADD {first_collection}')

#iteracion sobre una coleccion con un ciclo FOR
print('impresion del contenido de la coleccion')
for item  in first_collection:
    print(item)

#operaciones con colecciones
union_set =    first_collection.union(second_collection)
interseccion_set = first_collection.intersection(second_collection)
diferent_set = first_collection.difference(second_collection)

print(f'union de la coleccion {union_set}')
print(f'interseccion de la coleccion {interseccion_set}')
print(f'diferencia en colecciones {diferent_set}')
