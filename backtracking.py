from time import perf_counter

from datos import (
    cursos,
    aulas,
    horarios,
    disponibilidad_profesores
)

from modelo import Asignacion

from restricciones import asignacion_valida


def backtracking_recursivo(
        cursos_ordenados,
        posicion,
        asignaciones
):
    """
    Funcion recursiva que construye la planificacion
    curso por curso.

    Si una asignacion genera un conflicto, se descarta
    y se prueba otra alternativa.

    Retorna:
        una tupla con la solucion encontrada
        o una tupla vacia si no existe solucion.
    """

    # Caso base:
    # Todos los cursos fueron asignados.
    if posicion == len(cursos_ordenados):
        return asignaciones

    curso = cursos_ordenados[posicion]

    # Probar todos los horarios disponibles.
    for horario in horarios:

        # Probar todas las aulas disponibles.
        for aula in aulas:

            if asignacion_valida(
                    asignaciones,
                    curso,
                    horario,
                    aula,
                    disponibilidad_profesores
            ):

                asignacion = Asignacion(
                    curso,
                    horario,
                    aula
                )

                nuevas_asignaciones = asignaciones + (
                    asignacion,
                )

                resultado = backtracking_recursivo(
                    cursos_ordenados,
                    posicion + 1,
                    nuevas_asignaciones
                )

                # Si se encontro una solucion completa,
                # se retorna inmediatamente.
                if len(resultado) == len(cursos_ordenados):
                    return resultado

                # Si no se encontro solucion desde esta
                # asignacion, se continua con la siguiente
                # alternativa.

    # No se encontro una solucion desde esta posicion.
    return ()


def backtracking():
    """
    Ejecuta el algoritmo de Backtracking.

    Los cursos se procesan en orden de prioridad para
    intentar primero los cursos mas importantes.

    Retorna:
        resultado
        tiempo_ejecucion
    """

    inicio = perf_counter()

    cursos_ordenados = tuple(
        sorted(
            cursos,
            key=lambda curso: curso.prioridad,
            reverse=True
        )
    )

    resultado = backtracking_recursivo(
        cursos_ordenados,
        0,
        ()
    )

    tiempo = perf_counter() - inicio

    return (
        resultado,
        tiempo
    )


def mostrar_resultado_backtracking():
    print()
    print("=" * 70)
    print("                    BACKTRACKING")
    print("=" * 70)

    resultado, tiempo = backtracking()

    print()
    print(
        f"Tiempo de ejecucion: {tiempo:.6f} segundos"
    )

    print()

    if len(resultado) == 0:
        print("No se encontro una planificacion valida.")
        return

    print("PLANIFICACION ENCONTRADA")
    print("-" * 70)

    for posicion, asignacion in enumerate(
            resultado,
            start=1
    ):

        print(
            f"{posicion}. "
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
            f"  Prioridad: "
            f"{asignacion.curso.prioridad}"
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


if __name__ == "__main__":
    mostrar_resultado_backtracking()