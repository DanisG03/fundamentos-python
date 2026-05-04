print("Hola mundo")


snake_case = "hola" 
aprendiz_sena = "laura gomez" # este es el metodo de escritura 

# tipos de escritura de variables 

nombre = "laura"
apellido = "gomez"  # datos quemados 
edad = 21
altura = 1.45
activo = True
correo = "laura@gmail.com"
telefono = "3107857488"
telefono_int = int(telefono)
cedula = 12345678


# imprimir el tipo de dato y el valor de cada variable
print(type(nombre), nombre )
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(telefono_int), telefono_int)

# casteo convertir de un tipo a otro tipos

edad_float = float(edad)
altura_int = int(altura)
cedula_str = str(cedula)
telefono_int = int(telefono)

print(type(edad_float), edad_float)
print(type(altura_int), altura_int)
print(type(cedula_str), cedula_str)


"""COMENTARIOS 
 EN BLOQUE DE CÓDIGO
    """

# identacion en python tener en cuenta la estructura del codigo 

if 5 > 2: 
    print("5 es mayor que 2")
    
else:
    print("5 es menor que 2")
    
    
    #input
nombre_completo = input("Ingrese su nombre completo: ")
print(nombre_completo)
    
    
edad = int (input("Ingrese su edad: "))
print(edad)


# imprimir con f_string simplificar y concatener texto con numeros 

print(f" {nombre_completo} tiene {edad} años")
