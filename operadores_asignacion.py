# operadores de asignación

x = 5
print(x)
x = x + 2 # forma tradicional suma
x += 2 # simplificada 
print(x)

x= x -3 # forma tradicional resta
x -= 3 # simplificada
print(x)

x = x * 2 # forma tradicional multiplicación
x *= 2 # simplificada
print(x)

x = x / 2 # forma tradicional división
x /= 2 # simplificada
print(x)

x = x % 2 # forma tradicional módulo
x %= 2 # simplificada
print(x)

x = x ** 2 # forma tradicional potencia
x **= 2 # simplificada
print(x)



x = 10 # asigna la variable 
print(x) # imprimir el valor de la variable x 


# walrus operator (operador morsa) introducido en Python 3.8
# permite asignar un valor a una variable dentro de una expresión

print(x := 10) # asigna 10 a x y luego imprime el valor de  