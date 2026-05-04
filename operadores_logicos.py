# operadores lógicos

#AND
print(True and True) # si ambos son verdaderos = true
print(True and False) # si uno es falso = false 
print(False and True) # si uno es falso = false
print(False and False) # si ambos son falsos = false

# OR 
print(True or True) # si ambos son verdadeeros = true 
print(True or False) # si uno es verdadero = true
print(False or True) # si uno es falso = true
print(False or False) # si ambos son falsos = false

#NOT 
print(not True) # si es falso = true
print(not False) # si es verdadero = false      

# ejercicio and 
print(5>3 and 2<4) # true
print(5>3 and 5<4) # false
print(2>3 and 2>4)  # false 
print(2>3 and 5<4)  # false

# ejercicio OR 
print(5>3 or 2<4) # true
print(5>3 or 5<4) # true 
print(2>3 or 2>4)  # true
print(2>3 or 5<4)  # false


# ejercicio NOT 
print(not 5>3) #false 
print(not 2>3) # true
