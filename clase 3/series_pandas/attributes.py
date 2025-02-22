import pandas as pd

good_student_qualities = ['Self-Discipline', 'Self-Discipline', 'Goal-Oriented', 'Punctuality', 'Diligence and Hard Work', 'Respectfull', 'password']
serie = pd.Series(good_student_qualities)
print(serie)

#El tamaño de la serie
print(f'El tamaño de la serie es el siguiente: {serie.size}')

#La serie tiene valores duplicados
print(f'La serie tiene valores duplicados: {serie.is_unique}')

#Información de los indices
print(f'Este atributo muestra información de los indices: {serie.index}')

#Informacion del almancenamiento de los valores de la serie
print(f'Información de los valores de la serie: {serie.values}')

#Información del tipo de datos que se utilizan para almancenar los valores de la serie
print('Tipo de datos: [type(serie.values)}')