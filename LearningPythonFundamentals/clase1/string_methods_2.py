#otros metodos
from operator import indexOf

message ="los cuervos de la utvt"

#len
size= len(message)

#replace
new_message = message.replace(' ', '.')

#find
indexOf = message.find('U')

#split
message_sliced = message.split()
print(f"longitud de la cadena:{size}")
print(f"Nueva cadena:{size}")
print(f"posicion del elemento buscado:{indexOf}")
print(f"Cadena particionada:{message_sliced}")






