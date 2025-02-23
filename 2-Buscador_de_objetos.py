# Problema 2: Agente Buscador de Objetos (Basado en Objetivos)
def buscador_objetos():
    import numpy as np
    grid = np.zeros((5, 5))
    obj_x, obj_y = random.randint(0, 4), random.randint(0, 4)
    agent_x, agent_y = 0, 0
    grid[obj_x, obj_y] = 2  # 2 representa el objeto
    
    while (agent_x, agent_y) != (obj_x, obj_y):
        grid[agent_x, agent_y] = 1  # 1 representa al agente
        print(grid)
        grid[agent_x, agent_y] = 0
        if agent_x < obj_x:
            agent_x += 1
        elif agent_x > obj_x:
            agent_x -= 1
        elif agent_y < obj_y:
            agent_y += 1
        elif agent_y > obj_y:
            agent_y -= 1
        time.sleep(1)
    print("¡Objeto encontrado!")