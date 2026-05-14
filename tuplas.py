# Tuplas
# estructura de una tupla 

# indice:       0         1             2             3    
tupla = ("elemento1", "elemento2", "elemento3")
print(type(tupla)) # <class 'tuple'>

tupla_2 = "a", "b", "c"
print(type(tupla_2)) # <class 'tuple'>

tupla_3 = ("hola",) # sin la como toma un solo valor 
print(type(tupla_3)) # <class 'tuple'>

tupla_4 = tuple("hola")
print(tupla_4) # ('h', 'o', 'l', 'a')

tupla_mixta = ("laura", 123, 3.14, True, [1,2,3])
print(tupla_mixta)


#tupla aprendicces ADSO 

# indice:       0       1        2        3        4        5        6      7         8          9

aprendices = ("Juan", "Maria", "Pedro", "Luis", "Carlos", "Laura", "Ana", "Sofia", "Andres", "Camila")

# acseder a un elemento de tupla 
print (aprendices[1]) # maria


# modificar un elemento de tupla
aprendices[3]  # Juana

# modificar un elemento de la tupla 
# aprendices[3] = "Juana"  "esto genera un error porque no se puede modificar una tupla"

print(aprendices[0:2]) # ('Juan', 'Maria')
print(aprendices[1:4]) # ('Maria', 'Pedro', 'Luis')
print(aprendices[3:]) # ('Luis', 'Carlos', 'Laura')

# sumar dos tuplas 
tupla_1 = (1,2,3)
tupla_2 = (4,5,6)
tupla_suma = tupla_1 + tupla_2
print(tupla_suma) # (1, 2, 3, 4, 5, 6)

# MULTIPLICAR TUPLAS
tupla_multiplicada = tupla_1 * 3
print(tupla_multiplicada) # (1, 2, 3, 1, 2, 3, 1, 2, 3)


#metodos de las tuplas 

# mmedir el largo con len
print(len(aprendices))
# encontrar elemento en una tupla con count
aprendices.count("Juan") # 1

#obtener el indice de un elemento con indixe 

print(aprendices.index("Carlos")) # 4


#modificar  una tupla en lista 

print(type(aprendices)) 

aprendices_lista = list(aprendices) #convertimos la tupla en lista 
aprendices_lista.append("Juana") # agregamos un nuevo elemento ala lista de la tupla 
print(aprendices_lista) 

#convertimos la lista de nuevo en una tupla

aprendices_tupla = tuple(aprendices_lista)
print(aprendices_tupla)

# comprobar  pertenecia (in)

print("simon" in aprendices) # False
print("Juan" in aprendices) # True

# enpaquetae tuplas

programa_1 = "ADSO" 
programa_2 = "sst" 
programa_3 = "topografia"

tupla_prograam = (programa_1, programa_2, programa_3)
print(tupla_prograam) # ('ADSO', 'sst', 'topografia')

# desenpaquetar tuplas

tupla_desenpaquetada = ("ADSO", "SST", "Topografia")
programa_1, programa_2, programa_3 = tupla_desenpaquetada
print(programa_1) # ADSO


#ejercicio 2 tupla 

tupla_ciudades = ("Bogota", "medellin", "cali")
cuiudad_1, ciudad_2, ciudad_3 = tupla_ciudades
print(cuiudad_1) # Bogota

# el astarisco hace que la variable guarde el resto de datos


# interar sobre una tuplacon for 

for ciudad in tupla_ciudades:
    print(ciudad)



















