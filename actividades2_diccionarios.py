# actividad2_diccionarios.py

# Diccionario de aprendices
grupo = {
    "1001": {
        "nombre": "Laura",
        "edad": 20,
        "ciudad": "Bogotá",
        "notas": [4.0, 3.8, 4.5, 4.2]
    },

    "1002": {
        "nombre": "Carlos",
        "edad": 22,
        "ciudad": "Medellín",
        "notas": [3.0, 3.5, 2.8, 3.2]
    },

    "1003": {
        "nombre": "Ana",
        "edad": 19,
        "ciudad": "Cali",
        "notas": [4.8, 4.5, 4.7, 5.0]
    },

    "1004": {
        "nombre": "Pedro",
        "edad": 21,
        "ciudad": "Barranquilla",
        "notas": [2.5, 3.0, 2.8, 3.1]
    }
}

# Función para calcular promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Reporte de aprendices
print("===== REPORTE DE APRENDICES =====")

for ficha, datos in grupo.items():

    promedio = calcular_promedio(datos["notas"])

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print("\nFicha:", ficha)
    print("Nombre:", datos["nombre"])
    print("Edad:", datos["edad"])
    print("Ciudad:", datos["ciudad"])
    print("Promedio:", round(promedio, 2))
    print("Estado:", estado)

# Agregar nuevo aprendiz
grupo["1005"] = {
    "nombre": "Sofía",
    "edad": 23,
    "ciudad": "Cartagena",
    "notas": [4.2, 4.0, 3.9, 4.5]
}

# Actualizar ciudad
grupo["1002"]["ciudad"] = "Pereira"

print("\n===== NUEVO APRENDIZ AGREGADO =====")
print(grupo["1005"])

# BONUS
print("\n===== APRENDICES ORDENADOS POR PROMEDIO =====")

ordenados = sorted(
    grupo.items(),
    key=lambda item: calcular_promedio(item[1]["notas"]),
    reverse=True
)

for ficha, datos in ordenados:
    promedio = calcular_promedio(datos["notas"])

    print(datos["nombre"], "-", round(promedio, 2))