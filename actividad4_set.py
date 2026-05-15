# actividad3_sets.py

# Conjuntos
python_curso = {"Ana", "Luis", "Marta", "Carlos", "Sofía", "Pedro"}
java_curso = {"Luis", "Carlos", "Pedro", "Laura", "Diego"}
bd_curso = {"Marta", "Sofía", "Ana", "Miguel"}

# 1. Total de aprendices únicos
todos = python_curso | java_curso | bd_curso

print("Total de aprendices únicos:", todos)

# 2. Aprendices que están en Python y Java
python_java = python_curso & java_curso

print("\nAprendices en Python y Java:", python_java)

# 3. Solo en Python
solo_python = python_curso - java_curso - bd_curso

print("\nAprendices solo en Python:", solo_python)

# 4. Exactamente en dos programas
dos_programas = (
    (python_curso & java_curso) |
    (python_curso & bd_curso) |
    (java_curso & bd_curso)
) - (python_curso & java_curso & bd_curso)

print("\nAprendices en exactamente dos programas:", dos_programas)

# 5. Lista con duplicados
inscripciones = [
    "Ana", "Luis", "Ana", "Marta",
    "Carlos", "Luis", "Sofía",
    "Pedro", "Ana"
]

# Conjunto para eliminar repetidos
unicos = set(inscripciones)

print("\nAprendices únicos:", unicos)
print("Cantidad de aprendices únicos:", len(unicos))

# 6. Diccionario de conteo
conteo = {
    aprendiz: (
        (aprendiz in python_curso) +
        (aprendiz in java_curso) +
        (aprendiz in bd_curso)
    )
    for aprendiz in todos
}

print("\nCantidad de programas por aprendiz:")

for aprendiz, cantidad in conteo.items():
    print(aprendiz, ":", cantidad)

# BONUS
tres_programas = python_curso & java_curso & bd_curso

print("\nAprendices matriculados en los tres programas:")
print(tres_programas)