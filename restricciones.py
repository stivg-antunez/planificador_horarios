def aula_disponible(asignaciones, horario, aula):
    """
    Verifica que el aula no esté ocupada
    en el horario seleccionado.
    """

    for asignacion in asignaciones:
        mismo_horario = (
            asignacion.horario.codigo == horario.codigo
        )

        misma_aula = (
            asignacion.aula.codigo == aula.codigo
        )

        if mismo_horario and misma_aula:
            return False

    return True


def profesor_disponible(asignaciones, curso, horario):
    """
    Verifica que el profesor no tenga
    otro curso en el mismo horario.
    """

    for asignacion in asignaciones:
        mismo_profesor = (
            asignacion.curso.profesor == curso.profesor
        )

        mismo_horario = (
            asignacion.horario.codigo == horario.codigo
        )

        if mismo_profesor and mismo_horario:
            return False

    return True


def grupo_disponible(asignaciones, curso, horario):
    """
    Verifica que un grupo de estudiantes
    no tenga dos cursos al mismo tiempo.
    """

    for asignacion in asignaciones:
        mismo_grupo = (
            asignacion.curso.grupo == curso.grupo
        )

        mismo_horario = (
            asignacion.horario.codigo == horario.codigo
        )

        if mismo_grupo and mismo_horario:
            return False

    return True


def capacidad_suficiente(curso, aula):
    """
    Verifica que la capacidad del aula
    sea suficiente para el curso.
    """

    return curso.estudiantes <= aula.capacidad


def laboratorio_disponible(curso, aula):
    """
    Si el curso requiere laboratorio,
    el aula debe ser de tipo Laboratorio.
    """

    if curso.requiere_laboratorio:
        return aula.tipo == "Laboratorio"

    return True


def profesor_tiene_horario(curso, horario, disponibilidad):
    """
    Verifica si el profesor está disponible
    en el horario seleccionado.
    """

    for profesor, horarios_disponibles in disponibilidad:

        if profesor == curso.profesor:
            return horario.codigo in horarios_disponibles

    return False


def curso_no_repetido(asignaciones, curso):
    """
    Verifica que el curso todavía no
    haya sido asignado.
    """

    for asignacion in asignaciones:

        if asignacion.curso.codigo == curso.codigo:
            return False

    return True


def asignacion_valida(
        asignaciones,
        curso,
        horario,
        aula,
        disponibilidad
):
    """
    Verifica todas las restricciones
    necesarias para realizar una asignación.
    """

    if not curso_no_repetido(asignaciones, curso):
        return False

    if not aula_disponible(asignaciones, horario, aula):
        return False

    if not profesor_disponible(asignaciones, curso, horario):
        return False

    if not grupo_disponible(asignaciones, curso, horario):
        return False

    if not capacidad_suficiente(curso, aula):
        return False

    if not laboratorio_disponible(curso, aula):
        return False

    if not profesor_tiene_horario(
            curso,
            horario,
            disponibilidad
    ):
        return False

    return True