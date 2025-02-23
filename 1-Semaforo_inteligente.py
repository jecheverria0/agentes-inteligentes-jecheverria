# Problema 1: Agente de Semáforo Inteligente (Reactivo)
import time
import random

def semaforo_inteligente():
    estados = ['Verde', 'Amarillo', 'Rojo']
    while True:
        vehiculos = random.randint(0, 10)  # Simulación de tráfico
        if vehiculos > 7:
            tiempo_verde = 10
        elif 4 <= vehiculos <= 7:
            tiempo_verde = 7
        else:
            tiempo_verde = 5
        
        print(f"Estado: Verde ({tiempo_verde} segundos) - Vehículos detectados: {vehiculos}")
        time.sleep(tiempo_verde)
        print("Estado: Amarillo (3 segundos)")
        time.sleep(3)
        print("Estado: Rojo (5 segundos)")
        time.sleep(5)