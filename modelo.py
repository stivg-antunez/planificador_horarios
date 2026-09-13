class Curso:
    def __init__(
            self,
            codigo,
            nombre,
            profesor,
            carrera,
            ciclo,
            creditos,
            estudiantes,
            grupo,
            horas_semanales,
            prioridad,
            requiere_laboratorio
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = profesor
        self.carrera = carrera
        self.ciclo = ciclo
        self.creditos = creditos
        self.estudiantes = estudiantes
        self.grupo = grupo
        self.horas_semanales = horas_semanales
        self.prioridad = prioridad
        self.requiere_laboratorio = requiere_laboratorio

    def __str__(self):
        laboratorio = "Sí" if self.requiere_laboratorio else "No"

        return (
            f"{self.codigo} - {self.nombre} | "
            f"Profesor: {self.profesor} | "
            f"Grupo: {self.grupo} | "
            f"Estudiantes: {self.estudiantes} | "
            f"Laboratorio: {laboratorio}"
        )


class Aula:
    def __init__(self, codigo, nombre, capacidad, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo

    def __str__(self):
        return (
            f"{self.codigo} - {self.nombre} | "
            f"Capacidad: {self.capacidad} | "
            f"Tipo: {self.tipo}"
        )


class Horario:
    def __init__(self, codigo, dia, hora_inicio, hora_fin):
        self.codigo = codigo
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return (
            f"{self.codigo} - {self.dia} "
            f"{self.hora_inicio}-{self.hora_fin}"
        )


class Asignacion:
    def __init__(self, curso, horario, aula):
        self.curso = curso
        self.horario = horario
        self.aula = aula

    def __str__(self):
        return (
            f"{self.curso.nombre} | "
            f"Profesor: {self.curso.profesor} | "
            f"{self.horario.dia} "
            f"{self.horario.hora_inicio}-{self.horario.hora_fin} | "
            f"{self.aula.nombre}"
        )