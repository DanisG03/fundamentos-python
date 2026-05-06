# actividad 3 

# actividad3.py

# PASO 1. Solicitar datos
print("==" * 45)

peso = float(input("Ingrese su peso en kg: "))
print("==" * 45)

estatura = float(input("Ingrese su estatura en metros: "))

# PASO 2. Validación (bonus)
if peso <= 0 or estatura <= 0:
    print("Error: El peso y la estatura deben ser valores positivos.")
else:
    
    # PASO 3. Calcular Índice de Masa Corporal (IMC)
    imc = peso / (estatura ** 2)

    # PASO 4. Clasificación
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    # PASO 5. Mostrar resultados
    
    print("\n--- Resultados ---")
    
    print(f"IMC: {round(imc, 2)}")
    print(f"Clasificación: {clasificacion}")
    