def busqueda_lineal_curso(cursos, nombre_buscado):
    """
    Realiza una búsqueda lineal sobre una lista de objetos Curso.
    Devuelve el objeto Curso si lo encuentra, o None si no existe.
    Complejidad: O(N)
    """
    for curso in cursos:
        if curso.nombre.lower() == nombre_buscado.lower():
            return curso
    return None

def busqueda_binaria_curso(cursos_ordenados, nombre_buscado):
    """
    Realiza una búsqueda binaria sobre una lista de cursos previamente ordenada por nombre.
    Devuelve el objeto Curso si lo encuentra, o None si no existe.
    """
    inicio = 0
    fin = len(cursos_ordenados) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        curso_actual = cursos_ordenados[medio]

        if curso_actual.nombre.lower() == nombre_buscado.lower():
            return curso_actual
        elif curso_actual.nombre.lower() < nombre_buscado.lower():
            inicio = medio + 1
        else:
            fin = medio - 1

    return None