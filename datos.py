from modelo import Curso, Aula, Horario


# ============================================================
# CURSOS
# ============================================================

cursos = (
    Curso(
        "C001",
        "Programacion",
        "Carlos",
        "Ingenieria de Sistemas",
        2,
        4,
        30,
        "A",
        4,
        3,
        False
    ),

    Curso(
        "C002",
        "Base de Datos",
        "Maria",
        "Ingenieria de Sistemas",
        3,
        4,
        25,
        "A",
        4,
        3,
        False
    ),

    Curso(
        "C003",
        "Matematica",
        "Pedro",
        "Ingenieria de Sistemas",
        1,
        5,
        35,
        "A",
        5,
        5,
        False
    ),

    Curso(
        "C004",
        "Algoritmos",
        "Luis",
        "Ingenieria de Sistemas",
        4,
        4,
        20,
        "A",
        4,
        5,
        False
    ),

    Curso(
        "C005",
        "Redes",
        "Ana",
        "Ingenieria de Sistemas",
        5,
        3,
        28,
        "A",
        3,
        4,
        True
    ),

    Curso(
        "C006",
        "Sistemas Operativos",
        "Carlos",
        "Ingenieria de Sistemas",
        5,
        4,
        30,
        "B",
        4,
        4,
        True
    )
)


# ============================================================
# AULAS
# ============================================================

aulas = (
    Aula(
        "A01",
        "Aula 101",
        40,
        "Aula"
    ),

    Aula(
        "A02",
        "Aula 102",
        30,
        "Aula"
    ),

    Aula(
        "A03",
        "Laboratorio 201",
        30,
        "Laboratorio"
    ),

    Aula(
        "A04",
        "Laboratorio 202",
        25,
        "Laboratorio"
    )
)


# ============================================================
# HORARIOS
# ============================================================

horarios = (
    Horario(
        "H01",
        "Lunes",
        "08:00",
        "10:00"
    ),

    Horario(
        "H02",
        "Lunes",
        "10:00",
        "12:00"
    ),

    Horario(
        "H03",
        "Martes",
        "08:00",
        "10:00"
    ),

    Horario(
        "H04",
        "Martes",
        "10:00",
        "12:00"
    ),

    Horario(
        "H05",
        "Miercoles",
        "08:00",
        "10:00"
    ),

    Horario(
        "H06",
        "Miercoles",
        "10:00",
        "12:00"
    )
)


# ============================================================
# DISPONIBILIDAD DE PROFESORES
# ============================================================

disponibilidad_profesores = (
    ("Carlos", ("H01", "H02", "H03", "H04")),
    ("Maria", ("H01", "H03", "H05", "H06")),
    ("Pedro", ("H02", "H04", "H05")),
    ("Luis", ("H01", "H04", "H06")),
    ("Ana", ("H02", "H03", "H05", "H06"))
)