# CONJUNTOS (SET) EN PYTHON

# estructura de un conjunto 

conjunto ={}  # asi no es un conjunto
conjunto = set()  # esto si es un  conjunto 
print(type(conjunto))


# --- creacion de un conjunto ---
lenguaje = {"python", "java", "c++", "javascript"} # sin duplicados 

#---metodo de modificacion---
frutas = {"manzana", "pera", "limon", "maracuya"}
frutas.add("naranja")                            # agregar un elemento
frutas.add("pera")                               # no agrega pera ya que ya existe
frutas.remove("limon")                           # eliminar un elemento   eliminar: lanza keyerror si no exixte 
frutas.discard("naranja")                        # eliminar un elemento si existe
elem = frutas.pop()                              # eliminar y retornar un  elemento aleatorio
print(elem)


#----verificar pertenencia : 0(1)
print("python" in lenguaje)         # True - instantanea sin importar el tamaño
print("cobol" in lenguaje)          # false




python_devs = {"ana", "luis", "marta", "carlos", "sofia"}
java_devs = {"luis", "carlos", "pedro", "laura"}


#_______________________________________________
# UNION: todos los elementos de ambos conjuntos
#_________________________________________________

todos = python_devs  | java_devs

# o tambien : python_devs.union(java_devs)

print("Union:", todos)
# {'ana', 'luis', 'marta', 'carlos', 'sofia', 'pedro', 'laura'}


#_______________________________________________
# INTERSECTION  &: solo los que estan en ambos 
#_________________________________________________
ambos = python_devs & java_devs
print("Intersection:", ambos) # {'luis', 'carlos'}

#_______________________________________________
# DIFERENCIA: - : los de A que NO estan en B 
#_________________________________________________
solo_python = python_devs - java_devs

# o tambien : python_devs.difference(java_devs)

print("Solo_python:", solo_python) # {'ana', 'marta', 'sofia'}

solo_java = java_devs - python_devs
print("Solo_java:", solo_java) # {'pedro', 'laura'}


#_______________________________________________
# DIFERENCIA SIMETRICA ^: los que estan en uno PERO NO en ambos
#_________________________________________________
exclusivos = python_devs ^ java_devs

# o tambien : python_devs.symmetric_difference(java_devs)

print("Exclusivos:", exclusivos) 
# {'ana', ''marta', 'sofia', 'pedro', 'laura'}


















