# Agente de Patrullaje (Reflejo Simple)
import random

def patrullar(ruta):
    posicion = 0
    direccion = 1
    while True:
        print(f"Agente en posición: {ruta[posicion]}")
        if random.random() < 0.2:  # Simula un obstáculo con 20% de probabilidad
            direccion = -direccion
            print("Obstáculo detectado! Cambiando dirección.")
        posicion = (posicion + direccion) % len(ruta)

# Ruta de ejemplo
ruta = ["A", "B", "C", "D", "E"]
patrullar(ruta)