#condicionales

mi_condition = True
#if es un condicionate aqui digo que si mi_condicion es verdadera se imprime

if mi_condition:
    print("esto se imprime y lo ves condicion del if")

print("no esta condicionado")

mi_condition = False
#if es un condicionate aqui digo que si mi_condicion es falsa el if no se imprime

if mi_condition:
    print("esto se imprime y lo ves condicion del if")

print("no esta condicionado")

mi_condition = 3 + 3
#if es un condicionate aqui digo que si mi_condicion es falsa el if no se imprime

if mi_condition == 6:
    print("esto se imprime y lo ves condicion del segundo if")

print("no esta condicionado")

mi_condition = 3 + 3

if mi_condition > 5:
    print("esto se imprime y lo ves condicion ahora")
else:
    print("que es menor te dije de 6")

print("continua la ejecucion")

#condicionales con logica and - or 

mi_condition = 3 * 3

if mi_condition > 5 and mi_condition < 15:
    print("si mi condicion es mayor que 5 y menor que 15")
else:
    print("no cumple la condicion")

print("continua la ejecucion")

mi_condition = 3 * 1

if mi_condition > 5 or mi_condition < 4:
    print("si mi condicion es mayor que 5 y menor que 15")
else:
    print("no cumple la condicion")

print("continua la ejecucion")
