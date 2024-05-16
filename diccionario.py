#diccionarios

mi_dict = dict()
mi_otro_dict = {}

mi_otro_dict = {"Nombre": "Rodrigo", "Apellido": "Peña", "Alias": "aguilahost", "Edad": 50, 1:"python"}
print(mi_otro_dict)

mi_dict = {"Nombre": "Rodrigo", "Apellido": "Peña", "Alias": "aguilahost", "Edad": 50, "lenguajes": {"python. html. ccs5, javascripts"}}
print(mi_dict)

print(mi_dict["lenguajes"])
mi_otro_dict["Nombre"] = ["Rodrigo Jose"]#agregar o modificar un elemento del diccionario
print(mi_otro_dict)
del mi_otro_dict["Nombre"] #elimina un elemento del diccinario

#del mi_otro_dict **eliminaaria el diccionario completo de esta manera

print(mi_otro_dict.keys())
print(mi_otro_dict.items())
print(mi_otro_dict.values())

e_dict = {}

e_dict = dict.fromkeys(("titulo": "alana", 1))
print(mi_nuevo_dict)

print(e_dict)
