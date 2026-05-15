# diccionario (caracteristicas a un elemento)

# creacion de un diccionario

# estructura de un diccionario

diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"}

# diccionario vacio
diccionario_vacio = {}


diccionario_aprendiz = {
    "nombre": "laura",
    "apellido": "gomez",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": 25
}

print(type(diccionario_aprendiz))  


# obtener un valor del diccionario
print(diccionario_aprendiz["programa"])
print(diccionario_aprendiz.get("programa"))


# obtener solo las claves del diccionario
print(diccionario_aprendiz.keys())


# obtener solo los valores del diccionario
print(diccionario_aprendiz.values())


# obtener la clave y el valor
print(diccionario_aprendiz.items())


# agregar un nuevo elemento al diccionario
diccionario_aprendiz["correo"] = "laura.gomez@example.com"


# modificar el valor del diccionario
diccionario_aprendiz["programa"] = "sst"
print(diccionario_aprendiz)


# metodo update
diccionario_aprendiz.update({"nombre": "laura"})
diccionario_aprendiz.update({"ciudad": "sogamoso"})
print(diccionario_aprendiz)


#comprobar pertenencia (in)
if "programa" in diccionario_aprendiz:
    print("ficha es una de las propiedades de este diccionario")
    
    
# recorrer un diccionario con un ciclo for 
 
# recorrer solo las claves de diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)
    
        
#recorrer solo los valores de diccionario

for valor in diccionario_aprendiz.values():
    print(valor)
    

# recorrer ambos claves y valores de diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}: {valor}")
    
    
# eliminar elementos en un diccionario pop ()
diccionario_aprendiz.popitem()  # eliminar el ultimo elemento agregado
print(diccionario_aprendiz)

diccionario_aprendiz.pop("edad")  # eliminar el elemento especifico 
print(diccionario_aprendiz)


#eliminar todos los elementos del diccionario
diccionario_aprendiz.clear()
print(diccionario_aprendiz)


# dicicionarios anidados 
aprendices ={
    "aprendiz_1": {
        "nombre": "laura",
        "apellido": "gomez",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 25
    },
    "aprendiz_2": {
       "nombre": "marta",
       "apellido": "daza",
       "programa": "sst",
       "ficha": "3321349",
       "edad": 19
    },
    "aprendiz_3": {
        "nombre": "juan",
        "apellido": "perez",
        "programa": "quimica",
        "ficha": "3321349",
        "edad": 30
    }
}


# acceder a un valor de un diccionario anidado
print(aprendices["aprendiz_2"]["programa"])


# recorerer un diccionario anidado con un siclo for
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave, valor in datos.items():
        print(f" {clave}: {valor}")























