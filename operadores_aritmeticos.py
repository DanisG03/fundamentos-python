#operadores_aritmeticos
a = 5
b = 10

# suma
suma = a + b
print(f"La suma de {a} y {b} es {suma}")

# resta
resta = a - b
print(f"La resta de {a} y {b} es {resta}")

# multiplicación
multiplicacion = a * b
print(f"La multiplicacion de {a} y {b} es {multiplicacion}")

# división flotante o decimal 
divicion = a / b
print(f"La división de {a} y {b} es {divicion}")

# división entera
divicion_entera = a // b
print(f"La división entera de {a} y {b} es {divicion_entera}")

# potencia oexponenciación
potencia = a ** b
print(f"La potencia de {a} y {b} es {potencia}")

# módulo o residuo de la división
modulo = a % b
print(f"El módulo de {a} y {b} es {modulo}")


#precedencia de operadores
resultado_1 = a + b * 2
print(f"El resultado de la operacion {a} + {b} * 2 es {resultado_1}")

resultado_2 = (a + b) * 2
print(f"El resultado de la operacion ({a} + {b}) * 2 es {resultado_2}")

resultado_3 = a * b // 3
print(f"El resultado de la operacion {a} * {b} // 3 es {resultado_3}")

resultado_4 = (a * b) // 3
print(f"El resultado de la operacion ({a} * {b}) // 3 es {resultado_4}")

resultado_5 = a *(b //3)
print(f"El resultado de la operacion {a} * ({b} // 3) es {resultado_5}")


# ejercicio operadores aritmeticos

ejerccio= ((a + b) * (a-b) / (a * b)) - ((a**b)% 3)

# ejercicio= ((3+2) * (3-2) / (3*2)) - ((3**2)% 3)
# ejercicio = (5 * 1 / 6) - (9 % 3)
# ejercicio = (5 / 6) - 0
# ejercicio = 0.8333333333333334

print(f"El resultado de la operación ({a} + {b}) * ({a} - {b}) / ({a} * {b}) - {(a ** b) % 3} es {ejerccio}")


# librerias matematicas 

import math

print(math.pi)
print(math.e)
print(math.sqrt(16))


#libreria random

import random
print(random.random()) # números aleatorios entre 0 y 1
numero_aleatorio = random.randint(1, 10) # números aleatorios entre 1 y 10
print(numero_aleatorio)