from itertools import product
from time import perf_counter

from datos import (
    cursos,
    aulas,
    horarios,
    disponibilidad_profesores
)

from modelo import Asignacion

from restricciones import (
    asignacion_valida,
    capacidad_suficiente,
    laboratorio_disponible,
    profesor_tiene_horario
)


# ============================================================
# OBTENER OPCIONES POSIBLES PARA CADA CURSO
# ============================================================

def obtener_opciones_curso(curso):
    """
    Obtiene las combinaciones de horario y aula
    que pueden utilizarse para un curso.

    Estas opciones cumplen únicamente las restricciones
    individuales del curso:
        - Disponibilidad del profesor
        - Capacidad del aula
        - Tipo de aula
    """

    opciones = ()

    for horario in horarios:

        if not profesor_tiene_horario(
                curso,
                horario,
                disponibilidad_profesores
        ):
            continue

        for aula in aulas:

            if not capacidad_suficiente(curso, aula):
                continue

            if not laboratorio_disponible(curso, aula):
                continue

            opciones += (
                (horario, aula),
            )

    return opciones


# ============================================================
# GENERAR OPCIONES DE TODOS LOS CURSOS
# ============================================================

def generar_opciones():
    """
    Genera las opciones de horario y aula disponibles
    para cada curso.
    """

    opciones_cursos = ()

    for curso in cursos:

        opciones = obtener_opciones_curso(curso)

        opciones_cursos += (
            opciones,
        )

    return opciones_cursos


# ============================================================
# COMPROBAR UNA SOLUCIÓN COMPLETA
# ============================================================

def solucion_valida(combinacion):
    """
    Comprueba si una combinación completa de cursos,
    horarios y aulas cumple todas las restricciones.

    No se modifica la combinación durante la comprobación.
    Esto permite mantener el enfoque de fuerza bruta.
    """

    asignaciones = ()

    for posicion in range(len(cursos)):

        curso = cursos[posicion]

        horario = combinacion[posicion][0]

        aula = combinacion[posicion][1]

        if not asignacion_valida(
                asignaciones,
                curso,
                horario,
                aula,
                disponibilidad_profesores
        ):
            return False

        asignacion = Asignacion(
            curso,
            horario,
            aula
        )

        asignaciones += (
            asignacion,
        )

    return True


# ============================================================
# CONVERTIR COMBINACIÓN EN ASIGNACIONES
# ============================================================

def crear_asignaciones(combinacion):
    """
    Convierte una combinación encontrada en objetos
    de tipo Asignacion.
    """

    asignaciones = ()

    for posicion in range(len(cursos)):

        curso = cursos[posicion]

        horario = combinacion[posicion][0]

        aula = combinacion[posicion][1]

        asignacion = Asignacion(
            curso,
            horario,
            aula
        )

        asignaciones += (
            asignacion,
        )

    return asignaciones


# ============================================================
# ALGORITMO DE FUERZA BRUTA
# ============================================================

def fuerza_bruta():
    """
    Explora sistemáticamente las combinaciones posibles
    de horarios y aulas para todos los cursos.

    Retorna:
        resultado
        combinaciones_evaluadas
        tiempo_ejecucion
    """

    inicio = perf_counter()

    opciones_cursos = generar_opciones()

    combinaciones_evaluadas = 0

    # Verificar que todos los cursos tengan al menos
    # una opción individual disponible.
    for opciones in opciones_cursos:

        if len(opciones) == 0:

            tiempo = perf_counter() - inicio

            return (
                (),
                combinaciones_evaluadas,
                tiempo
            )

    # --------------------------------------------------------
    # PRODUCTO CARTESIANO
    # --------------------------------------------------------
    #
    # Se generan todas las combinaciones posibles:
    #
    # Curso 1 -> opción 1
    # Curso 2 -> opción 1
    # Curso 3 -> opción 1
    #
    # Curso 1 -> opción 1
    # Curso 2 -> opción 1
    # Curso 3 -> opción 2
    #
    # etc.
    #
    # --------------------------------------------------------

    for combinacion in product(*opciones_cursos):

        combinaciones_evaluadas += 1

        if solucion_valida(combinacion):

            resultado = crear_asignaciones(
                combinacion
            )

            tiempo = perf_counter() - inicio

            return (
                resultado,
                combinaciones_evaluadas,
                tiempo
            )

    tiempo = perf_counter() - inicio

    return (
        (),
        combinaciones_evaluadas,
        tiempo
    )


# ============================================================
# MOSTRAR RESULTADO
# ============================================================

def mostrar_resultado_fuerza_bruta():

    print()
    print("=" * 70)
    print("                 FUERZA BRUTA")
    print("=" * 70)

    resultado, combinaciones, tiempo = fuerza_bruta()

    print()
    print(
        f"Combinaciones evaluadas: {combinaciones}"
    )

    print(
        f"Tiempo de ejecucion: {tiempo:.6f} segundos"
    )

    print()

    if len(resultado) == 0:

        print("No se encontro una planificacion valida.")

        return

    print("PLANIFICACION ENCONTRADA")
    print("-" * 70)

    for asignacion in resultado:

        print(
            f"{asignacion.curso.codigo} - "
            f"{asignacion.curso.nombre}"
        )

        print(
            f"  Profesor: "
            f"{asignacion.curso.profesor}"
        )

        print(
            f"  Grupo: "
            f"{asignacion.curso.grupo}"
        )

        print(
            f"  Horario: "
            f"{asignacion.horario.dia} "
            f"{asignacion.horario.hora_inicio}-"
            f"{asignacion.horario.hora_fin}"
        )

        print(
            f"  Aula: "
            f"{asignacion.aula.nombre}"
        )

        print(
            f"  Capacidad: "
            f"{asignacion.aula.capacidad}"
        )

        print("-" * 70)


# ============================================================
# PROGRAMA DE PRUEBA
# ============================================================

if __name__ == "__main__":

    mostrar_resultado_fuerza_bruta()