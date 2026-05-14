# actividad 3 

# Lista inicial
canciones = [
    "Shape of You",
    "Despacito",
    "Blinding Lights",
    "Perfect",
    "Hawái"
]

print("Lista inicial:", canciones)

# append()
canciones.append("Levitating")
print("Después de append:", canciones)

# insert()
canciones.insert(1, "Monotonía")
print("Después de insert:", canciones)

# extend()
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Después de extend:", canciones)

# remove()
canciones.remove("Perfect")
print("Después de remove:", canciones)

# pop()
eliminada = canciones.pop()
print("Canción eliminada:", eliminada)
print("Después de pop:", canciones)

# sort()
canciones.sort()
print("Lista ordenada:", canciones)

# Preguntas

#Responde estas preguntas usando métodos: 

# ¿Cuántas canciones tiene la playlist?
# R: 7 cansiones

#¿En qué posición está la primera canción que agregaste? 

# R: 4 posición

# ¿Cuántas veces aparece el string 'Bonus Track 1'?

# R: 2 veses 
