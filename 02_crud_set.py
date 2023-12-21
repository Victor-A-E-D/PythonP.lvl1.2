set_countries = {'Col', 'Mex', 'Bol'}

# CRUD - Create
size = len(set_countries)
print(size)

#Para saber si esta dentro del conjunto
print('Col' in set_countries)
print('pe' in set_countries)

#Add - agregar
set_countries.add('Pe')
print(set_countries)
set_countries.add('Pe'  )
print(set_countries)

#update - actualizar
set_countries.update({'arg', 'ecua', 'pe'})

print(set_countries)

#remove - eliminar
set_countries.remove('Col')
print(set_countries)

set_countries.remove('arg')
print(set_countries)