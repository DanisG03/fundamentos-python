# actividad de calculadora de notas

print("=" * 45)
# PASO1:Solicitar datos de notas al usuario
nota_1 = float(input("ingresa tu primera nota:"))
print("=" * 45)

nota_2 = float(input("ingresa tu segunda nota:"))
print("=" * 45)

nota_3 = float(input("ingresa tu tercer nnota:")) 
print("=" * 45)

# PASO 2:calcular promedio

promedio = (nota_1 + nota_2 + nota_3) / 3
promedio_redondeado = round(promedio, 2)

# PASO 3: calcular cuantos puntos faltan para 5.0

NOTA_MAXIMA = 5.0
faltante = round(max(0,NOTA_MAXIMA - promedio),2)

# PASO 4: determinar si aprueva o no 
NOTA_MINIMA_APROBACION = 3.0
aprueva = promedio >= NOTA_MINIMA_APROBACION


print ("\n========RESULTADO============")

print (f"promedio: {promedio_redondeado}")
print (f"faltante: {faltante}")

if aprueva:
    print ("Estado: Aprueba✅")
else:
    print ("Estado: No Aprueba❌")


