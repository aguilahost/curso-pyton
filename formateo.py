#formateo

name, surname, age, color = "Rodrigo", "Peña", 50, "azul"
print("mi nombre es {} {} mi edad es {} mi color es {}".format(name, surname, age,color))
print("mi nombre es %s %s mi edad es %d mi color es %s" %(name, surname, age,color))

print(f"mi nombre es {name} {surname} mi edad es {age} mi color es {color}") #esta es la mejor manera

#desempaquetado de caracteres
language = "carmelo"
a, b, c, d, e, f, g = language
print(a)
print(c)
print(g)

language_slace = language[1:3]
print(language_slace)

language_slace = language[4:] #imprime desde la letra 4 hasta el final
print(language_slace)
language_slace = language[-3] #desde el final cuenta al principio
print(language_slace)

#reverse
reversed_language = language[:: -2]
print(reversed_language)

#funciones

print(language.capitalize()) #imprime la primera letra en mayuscula
print(language.upper()) #imprime todo en mayuscula
print(language.count(a)) # imprime cuantas a hay en un escrito
print(language.isnumeric())
print("1".isnumeric())
print(language.lower()) #imprime todo en minuscula
print(language.capitalize)
