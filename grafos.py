def construir_grafo_conflictos(cursos, horarios):
    """
    Construye un grafo (lista de adyacencia) donde dos cursos están conectados
    si comparten el mismo profesor o el mismo ciclo académico (conflicto de grupo/profesor).
    """
    grafo = {curso.nombre: [] for curso in cursos}
    
    for i in range(len(cursos)):
        for j in range(i + 1, len(cursos)):
            c1 = cursos[i]
            c2 = cursos[j]
            
            # Conflicto si tienen el mismo profesor o pertenecen al mismo ciclo
            mismo_profesor = c1.profesor == c2.profesor
            mismo_ciclo = c1.ciclo == c2.ciclo
            
            if mismo_profesor or mismo_ciclo:
                if c2.nombre not in grafo[c1.nombre]:
                    grafo[c1.nombre].append(c2.nombre)
                if c1.nombre not in grafo[c2.nombre]:
                    grafo[c2.nombre].append(c1.nombre)
                
    return grafo

def mostrar_conflictos_grafo(grafo):
    """Muestra en consola las conexiones del grafo de conflicto."""
    print("\n--- Grafo de Conflictos Potenciales ---")
    for curso, vecinos in grafo.items():
        conflictos = ", ".join(vecinos) if vecinos else "Sin conflictos"
        print(f"Curso [{curso}] -> Relación con: {conflictos}")

def coloreado_horarios_grafo(grafo):
    """
    Asigna un bloque horario (color) a cada curso mediante algoritmo Voraz (Welsh-Powell)
    para garantizar que cursos en conflicto reciban bloques diferentes.
    """
    colores = {}
    nodos_ordenados = sorted(grafo.keys(), key=lambda x: len(grafo[x]), reverse=True)
    
    for nodo in nodos_ordenados:
        colores_usados = {colores[vecino] for vecino in grafo[nodo] if vecino in colores}
        color_disponible = 1
        while color_disponible in colores_usados:
            color_disponible += 1
        colores[nodo] = color_disponible
        
    return colores