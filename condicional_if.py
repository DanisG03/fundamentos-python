# condicionaal IF / ELIF / ELSE/

# estructura vasica de los  condicional 

if False:
    print ("la condicion es verdadera")
elif False:
    print ("la condicion es falsa") 
elif True:
    print ("la condicion es falsa")
else : 
    print ("la condicion es falsa")


# ejercicio : clasificacion de edad 

edad = 21

if edad < 18:
    print ("eres un menor de edad")
    
elif edad >= 18 and edad < 30:
    print("eres un adulto")
    
else: 
    print("eres un menor de edad")
    
    
    
    # ejrcicio : clasificacion de edad if anidado
    
Edad = int(input("ingrese su edad: "))
    
if Edad < 18:
    if Edad > 12 and Edad < 18:
        print("adolecente")
    else: 
        print("niño")
else: 
    if Edad >= 18 and Edad < 60:
        print("eres un adulto")
    else:
     print("eres un adulto mayor")
     
# operador ternario simplifica el codigo en uno solo linea

numero = 4 
if numero % 2 == 0: 
    print ("el numero es par ")
else: 
    print ("el numero es impar")
    
# imprimir en una sola linea 
print ("el numero es par"if numero % 2 == 0 else "el numero es impar")
     
     