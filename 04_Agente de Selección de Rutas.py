# Agente de Selección de Rutas (Basado en Utilidad) con Dijkstra
def dijkstra(recompensas, inicio):
    frontera = [(0, inicio)]
    utilidad = {inicio: 0}
    padres = {inicio: None}
    
    while frontera:
        utilidad_actual, actual = heappop(frontera)
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            vecino = (actual[0] + dx, actual[1] + dy)
            if 0 <= vecino[0] < 5 and 0 <= vecino[1] < 5:
                nueva_utilidad = utilidad_actual + recompensas[vecino[0]][vecino[1]]
                if vecino not in utilidad or nueva_utilidad > utilidad[vecino]:
                    utilidad[vecino] = nueva_utilidad
                    heappush(frontera, (-nueva_utilidad, vecino))
                    padres[vecino] = actual
    return utilidad

recompensas = [[0,1,2,3,4], [2,3,4,5,6], [3,4,5,6,7], [1,2,1,2,1], [5,4,3,2,1]]
inicio = (0,0)
print("Mejor ruta con utilidad:", dijkstra(recompensas, inicio))
