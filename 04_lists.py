
'''
nunbers = []
for element in range(1, 11):
    nunbers.append(element * 2)
print(nunbers)

#DIFERENCIA ES QUE ES MAS CORTO Y MAS FACIL DE LEER
                        #[Ciclo dond se extrae element]
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)
'''

nunbers = []
for i in range(1, 11):
  if i % 2 == 0:
    nunbers.append(i * 2)
print(nunbers)

numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)