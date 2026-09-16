import heapq

def quicksort_cursos(cursos, clave="nombre"):
    """
    Ordena una lista de objetos Curso utilizando el algoritmo QuickSort.
    Soporta ordenar por 'nombre' o 'estudiantes'.
    """
    if len(cursos) <= 1:
        return cursos
    
    pivote = cursos[len(cursos) // 2]
    
    if clave == "estudiantes":
        izq = [x for x in cursos if x.estudiantes < pivote.estudiantes]
        centro = [x for x in cursos if x.estudiantes == pivote.estudiantes]
        der = [x for x in cursos if x.estudiantes > pivote.estudiantes]
    else:
        izq = [x for x in cursos if x.nombre < pivote.nombre]
        centro = [x for x in cursos if x.nombre == pivote.nombre]
        der = [x for x in cursos if x.nombre > pivote.nombre]
        
    return quicksort_cursos(izq, clave) + centro + quicksort_cursos(der, clave)

def bubble_sort_cursos(cursos, clave="nombre"):
    """Ordenamiento por Burbuja. Complejidad: O(N^2)"""
    lista = list(cursos)
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = getattr(lista[j], clave)
            val2 = getattr(lista[j + 1], clave)
            if val1 > val2:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort_cursos(cursos, clave="nombre"):
    """Ordenamiento por Selección. Complejidad: O(N^2)"""
    lista = list(cursos)
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if getattr(lista[j], clave) < getattr(lista[min_idx], clave):
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort_cursos(cursos, clave="nombre"):
    """Ordenamiento por Inserción. Complejidad: O(N^2)"""
    lista = list(cursos)
    for i in range(1, len(lista)):
        elem_actual = lista[i]
        j = i - 1
        while j >= 0 and getattr(lista[j], clave) > getattr(elem_actual, clave):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elem_actual
    return lista

def merge_sort_cursos(cursos, clave="nombre"):
    """Ordenamiento por Mezcla (MergeSort). Complejidad: O(N log N)"""
    if len(cursos) <= 1:
        return cursos
    medio = len(cursos) // 2
    izq = merge_sort_cursos(cursos[:medio], clave)
    der = merge_sort_cursos(cursos[medio:], clave)
    
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if getattr(izq[i], clave) <= getattr(der[j], clave):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def heap_sort_cursos(cursos, clave="nombre"):
    """Ordenamiento HeapSort. Complejidad: O(N log N)"""
    heap = [(getattr(c, clave), i, c) for i, c in enumerate(cursos)]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[2] for _ in range(len(heap))]