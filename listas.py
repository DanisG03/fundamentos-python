#listas 

# estructura de una lista 

lista = ["objeto_1", "objeto_2", "objeto_3"]
print(type(lista)) # <class 'list'>

lista_mixta = ["laura", 123, 3.14, True, [1,2,3]]

# crear una lista de aprendices sena ADSO
# indice:       0       1        2        3        4        5        6      7         8          9
aprendices = ["Juan", "Maria", "Pedro", "Luis", "Carlos", "Laura", "Ana", "Sofia", "Andres", "Camila"]
print (aprendices)

# acseder a un elemento de la lista 
print(aprendices[1]) # maria

#modificar un elemento de la lista
aprendices[3] = "Juana"
print(aprendices)

# consulta rangos de elementos de la lista 
print(aprendices[0:2])                  # juan maria no tiene en cunta el 2 norma python : define un rango 
print(aprendices[3:3])         # queda vacio por que el ultimo valor no lo toma 
print(aprendices[3:])         #  juana maria pedro luis carlos laura ana sofia andres camila

# SELECSIONAR SALTEADOS 
print(aprendices[0:3:5]) # juan maria pedro

# si :: si me incluye el ultimo registro 
print (aprendices[1::4]) # juan maria pedro

# concatena y unir dos listas con el signo + se une 

aprendices_ficha_3321349 = ["Juan", "Maria", "Pedro", "Luis", "Carlos", "Laura", "Ana", "Sofia", "Andres", "Camila"]
aprendices_ficha_2993648 = ["Juan", "Maria", "Pedro", "Luis", "Carlos", "Laura", "Ana", "Sofia", "Andres", "Camila"]

# concatena
aprendices_ADSO = aprendices_ficha_3321349 + aprendices_ficha_2993648
print(aprendices_ADSO)













