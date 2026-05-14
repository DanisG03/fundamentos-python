
# actividad 2 

temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# Indexación
print("Primer día:", temperaturas[0])
print("Último día:", temperaturas[-1])
print("Día 7 :", temperaturas[6])
print("Penúltimo día:", temperaturas[-2])

# Slicing
print("Primera semana:", temperaturas[0:7])
print("Segunda semana:", temperaturas[7:14])
print("Días pares:", temperaturas[1::2])
print("Lista invertida:", temperaturas[::-1])

# Promedio de cada semana
semana1 = temperaturas[0:7]
semana2 = temperaturas[7:14]

promedio1 = sum(semana1) / len(semana1)
promedio2 = sum(semana2) / len(semana2)

print("Promedio semana 1:", promedio1)
print("Promedio semana 2:", promedio2)

# Bonus
if promedio1 > promedio2:
    print("La semana 1 tuvo mayor temperatura promedio.")
elif promedio2 > promedio1:
    print("La semana 2 tuvo mayor temperatura promedio.")
else:
    print("Ambas semanas tuvieron el mismo promedio.")