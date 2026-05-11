# ejecricio practico 1
nombre = "Juan"
producto= 20000
promedio_asignaturas = 4.5

print(f"mi nombre es {nombre}, mi producto es {producto}, y mi promedio de asignaturas es {promedio_asignaturas}")
      
    
# ejercicio practico 2
variable_1_entera = int(input("ingrese un numero entero: "))
variable_2_entero = int(input("ingrese un numero entero: "))
variable_float = float(input("ingrese un numero flotante: "))
variable_1_string = input("ingrese un texto: ")
variable_2_string = input("ingrese un texto: ")

# suma de los tres numeros

suma = variable_1_entera + variable_2_entero + variable_float
print(f"la suma de los tres numeros es {suma}")

# mostras el entero mayor 
if variable_1_entera > variable_2_entero:
    print(f"el mayor es {variable_1_entera}")
    
else:
    print(f"el mayor es {variable_2_entero}")

# divicion del float  y enteros 
residuo = variable_float % variable_1_entera

if residuo !=0:
    resultado = variable_float / variable_1_entera
    print(f"el resultado de la division es {resultado}")

# concatena por dos cadenas leidas 
concatenacion = variable_1_string +""+ variable_2_string
print(f"la concatenacion es {concatenacion}")



#ejercicio practico 3

base = 5
exponente = 3

resultado = base**exponente
print(f"la potencia de {base} elevada a {exponente} es {resultado}")

# ejercicio 4 

numeros = input("ingrese un numero: ")

raiz_cuadrada = float(numeros)**0.5

print(f"la raiz cuadrada de {numeros} es {raiz_cuadrada}")


# ejercicio 5

nombre_estudiante = input("ingrese un nombre: ")
nota_1 = float(input("ingrese una nota: "))
nota_2 = float(input("ingrese una nota: "))
nota_3 = float(input("ingrese una nota: "))
nota_4 = float(input("ingrese una nota: "))
nota_5 = float(input("ingrese una nota: "))

media = nota_1 + nota_2 + nota_3 + nota_4 + nota_5
media = media / 5

print(f"la media del estudiante {nombre_estudiante} es {media}")


# ejercicico6

numeroUno =8
numeroDos =2

print(f"aantes de la variable auxiliar: numeroUno = {numeroUno} y numeroDos = {numeroDos}")

# USO DE LA VARIABLE AUXILIAR 
temp = numeroUno
numeroUno = numeroDos
numeroDos = temp
print(f"despues de la asignacion: numeroUno = {numeroUno} y numeroDos = {numeroDos}")


#ejercicio 7

estado = True

if estado == ((5==2) or (2>1)):
    print(f"la condicion es {estado}")
    
    
#ejerciico 8
# Crear variable llamada Resultado

resultado = (9 / 2) + 8 * 2 - 1 + (4 + 2) ** 2 % 5

# Mostrar resultado

print("El resultado de la operación es:", resultado)

#ejercicio 9

# cuadrado
lado_cuadrado = 8 
area_cuadrada = lado_cuadrado * lado_cuadrado
perimetro = 4 * lado_cuadrado
print(f"el perimetro del cuadrado es {perimetro} y su area es {area_cuadrada}")

# base triangulo 
base_triangulo = 9
alto_triangulo = 8

ladoUnoTriangulo = 8
ladoDosTriangulo = 8

area_triangulo = (base_triangulo * alto_triangulo) / 2
perimetro_triangulo = base_triangulo + ladoUnoTriangulo + ladoDosTriangulo

print(f"la area del triangulo es {area_triangulo} y su perimetro es {perimetro_triangulo}")

# rectangulo 
base_rectangulo = 8
alto_rectangulo = 6

area_rectangulo = base_rectangulo * alto_rectangulo
perimetro_rectangulo = (2 *base_rectangulo) + (2 *alto_rectangulo)

print(f"la area del rectangulo es {area_rectangulo} y su perimetro es {perimetro_rectangulo}")

# ejercicio 10 

# Solicitar la edad
edad = int(input("Ingrese su edad: "))

# Condicionales para determinar la categoría
if edad >= 0 and edad <= 5:
    print("Categoría: Infante")

elif edad >= 6 and edad <= 10:
    print("Categoría: Niño")

elif edad >= 11 and edad <= 15:
    print("Categoría: Pre adolescente")

elif edad >= 16 and edad <= 18:
    print("Categoría: Adolescente")

elif edad >= 19 and edad <= 25:
    print("Categoría: Pre adulto")

elif edad >= 26 and edad <= 40:
    print("Categoría: Adulto")

elif edad >= 41 and edad <= 55:
    print("Categoría: Pre anciano")

elif edad >= 56:
    print("Categoría: Anciano")

else:
    print("Edad no válida")


