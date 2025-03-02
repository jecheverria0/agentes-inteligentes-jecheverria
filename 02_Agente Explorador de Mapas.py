# Agente Explorador de Mapas (Con Estado Interno)
def explorar_mapa(mapa):
    posicion = (0, 0)
    visitados = set()
    movimientos = [(0,1), (1,0), (0,-1), (-1,0)]
    while len(visitados) < len(mapa) * len(mapa[0]):
        visitados.add(posicion)
        print(f"Explorando: {posicion}")
        for dx, dy in movimientos:
            nueva_pos = (posicion[0] + dx, posicion[1] + dy)
            if nueva_pos in visitados or nueva_pos[0] < 0 or nueva_pos[1] < 0 or nueva_pos[0] >= len(mapa) or nueva_pos[1] >= len(mapa[0]):
                continue
            posicion = nueva_pos
            break

mapa = [[0]*5 for _ in range(5)]
explorar_mapa(mapa)