#operadores_aritmeticos
a = 10
b = 5

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
division_entera = a // b
potencia = a ** b

print(f"Suma: {suma}")

#RETO 

valor_1 = float(input("Ingrese un valor: "))
valor_2 = float(input("Ingrese otro valor: "))
tipo_operacion = input("Ingrese el tipo de operación (1. suma, 2. resta, 3. multiplicacion, 4. division): ")

suma = valor_1 + valor_2
resta = valor_1 - valor_2
multiplicacion = valor_1 * valor_2
division = valor_1 / valor_2

if tipo_operacion == "1":
    print(f"La suma es {suma}")
elif tipo_operacion == "2":
    print(f"La resta es {resta}")
elif tipo_operacion == "3":
    print(f"La multiplicacion es {multiplicacion}")
elif tipo_operacion == "4":
    print(f"La division es {division}")
