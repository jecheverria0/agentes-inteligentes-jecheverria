# Agentes Inteligentes en Python

Este repositorio contiene cuatro agentes inteligentes desarrollados en Python para la tarea de Inteligencia Artificial.

## Problema 1: Agente de Semáforo Inteligente (Reactivo)
Este agente simula un semáforo inteligente que ajusta la duración de sus estados (verde, amarillo y rojo) según el tráfico detectado.

### Funcionamiento:
- Detecta el número de vehículos aleatoriamente.
- Ajusta el tiempo del semáforo en verde en función del tráfico.
- Cambia de estado automáticamente.

## Problema 2: Agente Buscador de Objetos (Basado en Objetivos)
El agente se mueve dentro de una cuadrícula 5x5 hasta encontrar un objeto ubicado aleatoriamente.

### Funcionamiento:
- Representa la cuadrícula con una matriz de NumPy.
- Se mueve en dirección al objeto paso a paso.
- Muestra el estado de la cuadrícula en cada movimiento.

## Problema 3: Sistema Experto para Diagnóstico Simple (Basado en Conocimiento)
Un sistema experto que sugiere un diagnóstico basado en los síntomas ingresados por el usuario.

### Funcionamiento:
- Solicita al usuario una lista de síntomas.
- Aplica reglas basadas en condicionales.
- Muestra un diagnóstico probable.

## Problema 4: Agente de Recomendación de Películas (Basado en Aprendizaje)
Un sistema que recomienda películas basadas en el género favorito del usuario.

### Funcionamiento:
- Contiene una lista de películas clasificadas por género.
- Solicita al usuario que ingrese su género favorito.
- Muestra una recomendación aleatoria.