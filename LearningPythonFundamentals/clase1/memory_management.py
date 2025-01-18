number_x = 10
number_y = 20

address_id_x = 100
address_id_y = 200

print("***Antes de actualizar la variable x***")
print(address_id_x)
print(address_id_y)

number_x = 20
address_id_x = id(number_x)
print("\n***Despues de actualizar la variable x***")

print(address_id_x)
print(address_id_y)