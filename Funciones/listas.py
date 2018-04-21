# ####Listas

mi_lista = ['Juan','Cabral',29, 1.78, True]

mi_list = list()
###insertar al final
mi_list.append('Juan')
mi_list.append('Cabral')
mi_list.append(1.78)

# print(mi_list)

# print(mi_lista)
# ###insertar con indice
# mi_list.insert(2,29)
# print(mi_list)

#agrego valores de mi_lista al final de mi_list
#mi_list.extend(mi_lista)

# ##modificar un item de lista
# mi_list[2]= 39
# print(mi_list)

# ##modificar varios items
# mi_list[3:]=[1.87,False]
# print(mi_list)

# ##Eliminar un item de la lista por indice
# mi_list.pop(1)
# print(mi_list)

# ##Eliminar un item por valor
# mi_lista.remove('Cabral')
# print(mi_lista)

# #reversa la lista
# print(mi_list)
# mi_list.reverse()

# ##ordena la lista siempre que sean del mismo tipo
# #mi_list.sort()
# ordena lista por string
#mi_list.sort(key=str)

# print(mi_list.count(1.78))
#index() devuelve la posicion de la primera
if juan in mi_list:
	print(mi_list.index('Juan'))
else:
	print(No esta en la lista)
print(mi_list)
print(max(mi_list))
print(min(mi_list))
print(len(mi_list))

input()
