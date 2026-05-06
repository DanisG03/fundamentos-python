# ejercicio creativo 

# eninciado: crea un juego de adivina la pelicula con TIEMPO y alarma 

import random
import time

# =========================
# 🔊 ALARMA
# =========================
def alarma():
    try:
        import winsound
        for _ in range(3):
            winsound.Beep(1000, 400)
            time.sleep(0.2)
    except:
        print("\a\a\a")

# =========================
# 🎬 JUEGO
# =========================
def jugar():
    print("\n🎬 ADIVINA LA PELÍCULA ")
    print("-------------------------------------------------------------------")
    print("ELIGUE LA OPCION QUE QUIERES JUGAR")
    print("1. Fácil\n2. Medio\n3. Difícil")

    try:
        nivel = int(input("Elige opción: "))
    except:
        print("❌ Ingresa un número válido")
        return

    facil = [
        {"pista": "Dinosaurios en un parque", "respuesta": "jurassic park"},
        {"pista": "León rey de la selva", "respuesta": "el rey leon"},
        {"pista": "Juguetes que viven", "respuesta": "toy story"}
    ]

    medio = [
        {"pista": "Viaje en el tiempo en auto", "respuesta": "volver al futuro"},
        {"pista": "Un anillo poderoso", "respuesta": "el señor de los anillos"},
        {"pista": "Mago con cicatriz", "respuesta": "harry potter"}
    ]

    dificil = [
        {"pista": "Sueños dentro de sueños", "respuesta": "inception"},
        {"pista": "Espacio y agujero negro", "respuesta": "interstellar"},
        {"pista": "Club secreto de peleas", "respuesta": "fight club"}
    ]

    # Configuración
    if nivel == 1:
        pelicula = random.choice(facil)
        vidas = 5
        tiempo_limite = 10
    elif nivel == 2:
        pelicula = random.choice(medio)
        vidas = 4
        tiempo_limite = 7
    elif nivel == 3:
        pelicula = random.choice(dificil)
        vidas = 3
        tiempo_limite = 5
    else:
        print("❌ Opción inválida")
        return

    puntos = 100

    print("\n💡 Pista:", pelicula["pista"])
    print(f"⏱ Tienes {tiempo_limite} segundos para responder")

    # =========================
    # 🔁 BUCLE
    # =========================
    while vidas > 0:

        print("\n⏳ ¡Responde rápido!")

        inicio = time.time()  # empieza a contar

        respuesta = input("👉 Tu respuesta: ").lower()

        fin = time.time()
        tiempo = fin - inicio

        print(f"⏱ Tiempo usado: {round(tiempo,2)}s")

        # VALIDACIÓN
        if tiempo > tiempo_limite:
            print("⏰ ¡Te demoraste demasiado!")
            alarma()
            vidas -= 1
            puntos -= 15

        else:
            if respuesta == pelicula["respuesta"]:
                print("🎉 ¡Correcto!")
                print("⭐ Puntos finales:", puntos)
                break
            else:
                print("❌ Incorrecto")
                vidas -= 1
                puntos -= 10

        print(f"❤️ Vidas: {vidas} | ⭐ Puntos: {puntos}")

    if vidas == 0:
        print("💀 Perdiste")
        print("La película era:", pelicula["respuesta"])


# =========================
# 🔁 LOOP PRINCIPAL
# =========================
while True:
    jugar()
    repetir = input("\n¿Jugar otra vez? 🤗(s/n): ")

    if repetir.lower() != "s":
        print("👋 Fin del juego")
        break