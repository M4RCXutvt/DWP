#entrada de datos mediante la consola input
name = input("cual es tu nombre")
age = input("¿cual es tu edad?")
salary = float(input("¿cual es tu salario?"))
total_pets = eval(input("¿cuantas mascotas tienes?"))
university = input("¿cual es el nombre de tu universidad?")

print(f"me llamo{name}, mi edad es{age}, el nombre de mi universidad es{university}")
print(type(name))
print(type(age))
print(type(total_pets))
print(type(university))


