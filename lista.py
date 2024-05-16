#listas
mi_list = list()
mi_other_list = ()
print(len(mi_list))
mi_list = ["cafe, pan, azucar, huevo, cafe"]
print(mi_list)
mi_list = [12, 23, 44, 50, 51, 33, 24]
print(mi_list)
print(len(mi_list)) # len cuenta el numero de elemtos en mi lista son 7
mi_other_list = [50, 1.80, "Rodrigo", "Peña", 45] #se pueden mesclar elementos
print(mi_other_list [0])
print(mi_other_list [4])
print(mi_other_list [-1])
print(mi_other_list [-3])
print(mi_list + mi_list) # se pueden nsumar las listas
mi_other_list.append("aguilahost") #sagregar un nelemnto a la lista siempre en la ultima posicion
print(mi_other_list)
mi_other_list.insert( 1,"aguilahost") # insertar un nelemnto a la lista siempre en la posicion que le indique en este caso es 1
print(mi_other_list)
mi_other_list.remove(45) # elimina un nelemnto a la lista en este caso es 45
print(mi_other_list)

my_pop_element = mi_list.pop(2) #elimina de una lista un elemento 
print(my_pop_element)
print(mi_list)

del mi_list[2] #es una manera de eliminar un elemento de la lista
print(mi_list)
mi_nueva_lista = mi_list.copy()
mi_list.clear() #elimina toda la lista 
print(mi_nueva_lista)
mi_nueva_lista.reverse() #da vuelta a la lista
print(mi_nueva_lista)
mi_nueva_lista.sort() #ordena de mayor a menor
print(mi_nueva_lista)
