# Problema 4: Agente de Recomendación de Películas (Basado en Aprendizaje)
def recomendacion_peliculas():
    peliculas = {
        "acción": ["Mad Max", "Gladiador", "John Wick"],
        "comedia": ["Superbad", "Dumb and Dumber", "The Hangover"],
        "drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic"]
    }
    genero = input("Ingrese su género favorito (acción, comedia, drama): ").lower()
    if genero in peliculas:
        print(f"Te recomendamos: {random.choice(peliculas[genero])}")
    else:
        print("Género no disponible.")