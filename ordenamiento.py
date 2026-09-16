def quicksort_cursos(cursos, clave="nombre"):
    """
    Ordena una lista de objetos Curso utilizando el algoritmo QuickSort.
    Soporta ordenar por 'nombre' o 'alumnos'.
    """
    if len(cursos) <= 1:
        return cursos
    
    pivote = cursos[len(cursos) // 2]
    
    if clave == "alumnos":
        izq = [x for x in cursos if x.alumnos < pivote.alumnos]
        centro = [x for x in cursos if x.alumnos == pivote.alumnos]
        der = [x for x in cursos if x.alumnos > pivote.alumnos]
    else:
        izq = [x for x in cursos if x.nombre < pivote.nombre]
        centro = [x for x in cursos if x.nombre == pivote.nombre]
        der = [x for x in cursos if x.nombre > pivote.nombre]
        
    return quicksort_cursos(izq, clave) + centro + quicksort_cursos(der, clave)