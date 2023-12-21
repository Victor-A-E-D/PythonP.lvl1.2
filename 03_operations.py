#Operaciones de conjuntos

#Conjunto a y b
set_a = {'Col', 'Mex', 'Bol'}
set_b = {'Pe', "Bol"}

#union de conjuntos
set_c = set_a.union(set_b)
print(set_c)
#otro metodo de union
print(set_a | set_b)

#interseccion
set_c = set_a.intesection(set_b)
print(set_c)
#otro metodo de interseccion
print(set_a & set_b)

#resta o diferencia
set_c = set_a.difference(set_b)
print(set_c)
#otro metodo de resta
print(set_a - set_b)

#diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
#otro metodo de diferencia simetrica
print(set_a ^ set_b)




