Descripcion de los Agentes

1️ Agente de Patrullaje (Reflejo Simple)

Este agente sigue una ruta fija, pero si encuentra un obstáculo, cambia de dirección de manera aleatoria. Su comportamiento es simple, ya que no almacena información del entorno, solo reacciona a lo que tiene enfrente.

2️ Agente Explorador de Mapas (Con Estado Interno)

A diferencia del agente anterior, este sí tiene memoria. Mientras se mueve en una cuadrícula, recuerda las posiciones que ya ha visitado para no volver a pasar por ellas, lo que le permite explorar nuevas zonas de manera eficiente.

3️ Agente de Navegación Autónoma (Basado en Metas) 🏁

Este agente tiene un objetivo claro: encontrar la salida en un laberinto de 5x5. Utiliza el algoritmo A* para calcular la ruta más corta, evitando obstáculos y optimizando su movimiento hasta llegar a la meta.

4️ Agente de Selección de Rutas (Basado en Utilidad) 🔝

Aquí el objetivo no es solo moverse, sino encontrar la mejor ruta considerando recompensas. Cada celda tiene un valor y el agente evalúa las opciones para elegir el camino con mayor beneficio. Usa el algoritmo de Dijkstra para tomar decisiones inteligentes.