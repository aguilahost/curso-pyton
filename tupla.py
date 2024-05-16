#tuplas
mi_tuple = tuple()
mi_otra_tuple = ()
mi_otra_tuple = (33, 22, 24, 25)
mi_tuple = (35, 45, "rodrigo", "Peña", 33)
print(mi_tuple[0])
print(mi_tuple[4])
print(mi_tuple.count("rodrigo"))
print(mi_tuple.index("Peña")) #INDICA LA POSICION DE UN VALOR
print(mi_tuple.index(35))
mi_suma_tuple = mi_otra_tuple + mi_tuple
print(mi_suma_tuple)
