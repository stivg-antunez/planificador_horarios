from time import perf_counter

from datos import (
    cursos,
    aulas,
    horarios,
    disponibilidad_profesores
)

from modelo import Asignacion

from restricciones import asignacion_valida


def ordenar_cursos():
    """
    Ordena los cursos de acuerdo con su prioridad,
    desde la prioridad mas alta hasta la mas baja.

    En caso de igualdad de prioridad, se conserva
    el orden original de los cursos.
    """

    cursos_ordenados = sorted(
        cursos,
        key=lambda curso: curso.prioridad,
        reverse=True
    )

    return tuple(cursos_ordenados)


def encontrar_asignacion(asignaciones, curso):
    """
    Busca la primera combinacion valida de horario y aula
    para un curso.

    El algoritmo toma la primera opcion que cumple
    todas las restricciones.
    """

    for horario in horarios:

        for aula in aulas:

            if asignacion_valida(
                    asignaciones,
                    curso,
                    horario,
                    aula,
                    disponibilidad_profesores
            ):

                return Asignacion(
                    curso,
                    horario,
                    aula
                )

    return None


def voraz():
    """
    Algoritmo voraz para la planificacion de horarios.

    Los cursos se procesan desde la mayor prioridad
    hasta la menor prioridad.

    Para cada curso se selecciona la primera asignacion
    valida encontrada.

    Retorna:
        resultado
        decisiones_realizadas
        tiempo_ejecucion
    """

    inicio = perf_counter()

    cursos_ordenados = ordenar_cursos()

    asignaciones = ()
    decisiones_realizadas = 0

    for curso in cursos_ordenados:

        asignacion = encontrar_asignacion(
            asignaciones,
            curso
        )

        if asignacion is None:

            tiempo = perf_counter() - inicio

            return (
                (),
                decisiones_realizadas,
                tiempo
            )

        asignaciones += (
            asignacion,
        )

        decisiones_realizadas += 1

    tiempo = perf_counter() - inicio

    return (
        asignaciones,
        decisiones_realizadas,
        tiempo
    )


def mostrar_resultado_voraz():
    print()
    print("=" * 70)
    print("                    ALGORITMO VORAZ")
    print("=" * 70)

    resultado, decisiones, tiempo = voraz()

    print()
    print(
        f"Decisiones realizadas: {decisiones}"
    )

    print(
        f"Tiempo de ejecucion: {tiempo:.6f} segundos"
    )

    print()

    if len(resultado) == 0:
        print("No se encontro una planificacion completa.")
        return

    print("ORDEN DE ASIGNACION")
    print("-" * 70)

    for posicion, asignacion in enumerate(resultado, start=1):

        print(
            f"{posicion}. "
            f"{asignacion.curso.codigo} - "
            f"{asignacion.curso.nombre} "
            f"(Prioridad: "
            f"{asignacion.curso.prioridad})"
        )

    print()
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
    mostrar_resultado_voraz()