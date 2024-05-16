# Loops
#whike

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else:
    print("mi condicion es mayor a 10")
print("la funcion continua")

while mi_condicion < 20:
    print(mi_condicion)
    mi_condicion += 1
    if mi_condicion == 15:
        print("hemos llegado a 15")
        break # al colocar un breack detiene el loop

else:
    print("mi condicion es mayor a 20")
print("la funcion continua")

#for nos sirve para listar un elemento

mi_list = [12, 23, 44, 50, 51, 33, 24]
for element in mi_list:
print(element)