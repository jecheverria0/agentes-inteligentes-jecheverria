# Agente de Navegación Autónoma (Basado en Metas) con A*
from heapq import heappop, heappush

def astar(laberinto, inicio, meta):
    def heuristica(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    frontera = [(0, inicio)]
    costo = {inicio: 0}
    padres = {inicio: None}
    
    while frontera:
        _, actual = heappop(frontera)
        if actual == meta:
            ruta = []
            while actual:
                ruta.append(actual)
                actual = padres[actual]
            return ruta[::-1]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            vecino = (actual[0] + dx, actual[1] + dy)
            if 0 <= vecino[0] < 5 and 0 <= vecino[1] < 5 and laberinto[vecino[0]][vecino[1]] == 0:
                nuevo_costo = costo[actual] + 1
                if vecino not in costo or nuevo_costo < costo[vecino]:
                    costo[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, meta)
                    heappush(frontera, (prioridad, vecino))
                    padres[vecino] = actual
    return []

laberinto = [[0,0,1,0,0], [0,1,1,0,0], [0,0,0,0,1], [1,0,1,0,0], [0,0,0,1,0]]
inicio = (0,0)
meta = (4,4)
print("Ruta encontrada:", astar(laberinto, inicio, meta))