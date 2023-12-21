#Un set o conjunto, elementos agrupados con propiedades en comun. 
#Se modifican pero no tiene orden. Y no se repiten.
set_countries = {'col ', 'mex ', 'bol '}
print(set_countries)
print(type(set_countries))


set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)
print(type(set_numbers))

set_types = {1, 'hola', False, 12.31}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
#utilizar list para tenerlo dentro de una lista.
unique_numbers = list(set_numbers)
print(unique_numbers)

