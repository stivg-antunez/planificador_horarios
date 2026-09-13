import os

from datos import (
    cursos,
    aulas,
    horarios,
    disponibilidad_profesores
)

from restricciones import asignacion_valida

from fuerza_bruta import fuerza_bruta
from voraz import voraz
from backtracking import backtracking


# ============================================================
# COLORES PARA LA CONSOLA
# ============================================================

class Colores:
    RESET = "\033[0m"

    ROJO = "\033[91m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BLANCO = "\033[97m"

    NEGRITA = "\033[1m"


# ============================================================
# FUNCIONES GENERALES
# ============================================================

def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pausar():
    """
    Pausa la ejecucion hasta que el usuario presione ENTER.
    """

    input(
        f"\n{Colores.AMARILLO}"
        "Presione ENTER para volver al menu..."
        f"{Colores.RESET}"
    )


def encabezado(titulo):
    """
    Muestra un encabezado profesional para cada seccion.
    """

    print()
    print(
        f"{Colores.CYAN}"
        "╔══════════════════════════════════════════════════════════════╗"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.NEGRITA}{Colores.BLANCO}"
        f"{titulo:^60}"
        f"{Colores.RESET}"
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}"
        "╚══════════════════════════════════════════════════════════════╝"
        f"{Colores.RESET}"
    )


def separador():
    print(
        f"{Colores.CYAN}"
        "──────────────────────────────────────────────────────────────"
        f"{Colores.RESET}"
    )


def mensaje_exito(mensaje):
    print(
        f"\n{Colores.VERDE}"
        f"✓ {mensaje}"
        f"{Colores.RESET}"
    )


def mensaje_error(mensaje):
    print(
        f"\n{Colores.ROJO}"
        f"✗ {mensaje}"
        f"{Colores.RESET}"
    )


def mensaje_info(mensaje):
    print(
        f"\n{Colores.AZUL}"
        f"ℹ {mensaje}"
        f"{Colores.RESET}"
    )


# ============================================================
# TITULO PRINCIPAL
# ============================================================

def mostrar_titulo():
    print(
        f"{Colores.CYAN}"
        "╔══════════════════════════════════════════════════════════════╗"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.NEGRITA}{Colores.BLANCO}"
        "          SISTEMA DE PLANIFICACIÓN DE HORARIOS           "
        f"{Colores.RESET}"
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "          Análisis de Algoritmos y Estrategias           "
        f"{Colores.RESET}"
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}"
        "╚══════════════════════════════════════════════════════════════╝"
        f"{Colores.RESET}"
    )


# ============================================================
# MOSTRAR CURSOS
# ============================================================

def mostrar_cursos():

    encabezado("LISTADO DE CURSOS")

    for curso in cursos:
        print(
            f"{Colores.VERDE}●{Colores.RESET} "
            f"{curso}"
        )

    print()
    print(
        f"{Colores.AZUL}"
        f"Total de cursos: {len(cursos)}"
        f"{Colores.RESET}"
    )


# ============================================================
# MOSTRAR AULAS
# ============================================================

def mostrar_aulas():

    encabezado("LISTADO DE AULAS")

    for aula in aulas:
        print(
            f"{Colores.VERDE}●{Colores.RESET} "
            f"{aula}"
        )

    print()
    print(
        f"{Colores.AZUL}"
        f"Total de aulas: {len(aulas)}"
        f"{Colores.RESET}"
    )


# ============================================================
# MOSTRAR HORARIOS
# ============================================================

def mostrar_horarios():

    encabezado("HORARIOS DISPONIBLES")

    for horario in horarios:
        print(
            f"{Colores.VERDE}●{Colores.RESET} "
            f"{horario}"
        )

    print()
    print(
        f"{Colores.AZUL}"
        f"Total de horarios: {len(horarios)}"
        f"{Colores.RESET}"
    )


# ============================================================
# DISPONIBILIDAD DE PROFESORES
# ============================================================

def mostrar_disponibilidad_profesores():

    encabezado("DISPONIBILIDAD DE PROFESORES")

    for profesor, horarios_disponibles in disponibilidad_profesores:

        print()
        print(
            f"{Colores.AMARILLO}"
            f"Profesor: {profesor}"
            f"{Colores.RESET}"
        )

        print("Horarios disponibles:")

        for codigo_horario in horarios_disponibles:
            print(
                f"  {Colores.VERDE}✓{Colores.RESET} "
                f"{codigo_horario}"
            )


# ============================================================
# PRUEBA DE RESTRICCIONES
# ============================================================

def probar_asignacion():

    encabezado("PRUEBA DE RESTRICCIONES")

    curso = cursos[0]
    horario = horarios[0]
    aula = aulas[0]

    asignaciones = ()

    resultado = asignacion_valida(
        asignaciones,
        curso,
        horario,
        aula,
        disponibilidad_profesores
    )

    print()
    print(
        f"{Colores.AMARILLO}Curso:{Colores.RESET} "
        f"{curso.nombre}"
    )

    print(
        f"{Colores.AMARILLO}Profesor:{Colores.RESET} "
        f"{curso.profesor}"
    )

    print(
        f"{Colores.AMARILLO}Horario:{Colores.RESET} "
        f"{horario}"
    )

    print(
        f"{Colores.AMARILLO}Aula:{Colores.RESET} "
        f"{aula}"
    )

    separador()

    if resultado:
        mensaje_exito("La asignación es válida.")
    else:
        mensaje_error("La asignación no es válida.")


# ============================================================
# MOSTRAR PLANIFICACION
# ============================================================

def mostrar_planificacion(resultado, nombre_algoritmo):

    encabezado(
        f"PLANIFICACIÓN - {nombre_algoritmo.upper()}"
    )

    if len(resultado) == 0:
        mensaje_error(
            "No se encontró una planificación válida."
        )
        return

    mensaje_exito(
        "Se encontró una planificación válida."
    )

    print()

    for posicion, asignacion in enumerate(
            resultado,
            start=1
    ):

        print(
            f"{Colores.MAGENTA}"
            f"[{posicion}] "
            f"{asignacion.curso.codigo} - "
            f"{asignacion.curso.nombre}"
            f"{Colores.RESET}"
        )

        print(
            f"    Profesor: "
            f"{asignacion.curso.profesor}"
        )

        print(
            f"    Grupo: "
            f"{asignacion.curso.grupo}"
        )

        print(
            f"    Prioridad: "
            f"{asignacion.curso.prioridad}"
        )

        print(
            f"    Horario: "
            f"{asignacion.horario.dia} "
            f"{asignacion.horario.hora_inicio}-"
            f"{asignacion.horario.hora_fin}"
        )

        print(
            f"    Aula: "
            f"{asignacion.aula.nombre}"
        )

        print(
            f"    Capacidad: "
            f"{asignacion.aula.capacidad}"
        )

        separador()


# ============================================================
# EJECUTAR FUERZA BRUTA
# ============================================================

def ejecutar_fuerza_bruta():

    encabezado("EJECUCIÓN - FUERZA BRUTA")

    print()
    print(
        f"{Colores.AZUL}"
        "Algoritmo ejecutado: Fuerza Bruta"
        f"{Colores.RESET}"
    )

    resultado, combinaciones, tiempo = fuerza_bruta()

    print()
    print(
        f"{Colores.AMARILLO}"
        f"Combinaciones evaluadas: {combinaciones}"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.AMARILLO}"
        f"Tiempo de ejecución: {tiempo:.6f} segundos"
        f"{Colores.RESET}"
    )

    mostrar_planificacion(
        resultado,
        "Fuerza Bruta"
    )


# ============================================================
# EJECUTAR VORAZ
# ============================================================

def ejecutar_voraz():

    encabezado("EJECUCIÓN - ALGORITMO VORAZ")

    print()
    print(
        f"{Colores.AZUL}"
        "Algoritmo ejecutado: Voraz"
        f"{Colores.RESET}"
    )

    resultado, decisiones, tiempo = voraz()

    print()
    print(
        f"{Colores.AMARILLO}"
        f"Decisiones realizadas: {decisiones}"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.AMARILLO}"
        f"Tiempo de ejecución: {tiempo:.6f} segundos"
        f"{Colores.RESET}"
    )

    mostrar_planificacion(
        resultado,
        "Algoritmo Voraz"
    )


# ============================================================
# EJECUTAR BACKTRACKING
# ============================================================

def ejecutar_backtracking():

    encabezado("EJECUCIÓN - BACKTRACKING")

    print()
    print(
        f"{Colores.AZUL}"
        "Algoritmo ejecutado: Backtracking"
        f"{Colores.RESET}"
    )

    resultado, tiempo = backtracking()

    print()
    print(
        f"{Colores.AMARILLO}"
        f"Tiempo de ejecución: {tiempo:.6f} segundos"
        f"{Colores.RESET}"
    )

    mostrar_planificacion(
        resultado,
        "Backtracking"
    )


# ============================================================
# COMPARAR ALGORITMOS
# ============================================================

def comparar_algoritmos():

    encabezado("COMPARACIÓN DE ALGORITMOS")

    print()
    print(
        f"{Colores.AZUL}"
        "Ejecutando los tres algoritmos..."
        f"{Colores.RESET}"
    )

    separador()

    # Fuerza Bruta
    resultado_fuerza, combinaciones, tiempo_fuerza = fuerza_bruta()

    # Voraz
    resultado_voraz, decisiones, tiempo_voraz = voraz()

    # Backtracking
    resultado_backtracking, tiempo_backtracking = backtracking()

    print()

    print(
        f"{Colores.NEGRITA}"
        f"{'ALGORITMO':<20}"
        f"{'TIEMPO':<20}"
        f"{'RESULTADO'}"
        f"{Colores.RESET}"
    )

    separador()

    if len(resultado_fuerza) > 0:
        estado_fuerza = (
            f"{Colores.VERDE}Válido{Colores.RESET}"
        )
    else:
        estado_fuerza = (
            f"{Colores.ROJO}No encontrado{Colores.RESET}"
        )

    if len(resultado_voraz) > 0:
        estado_voraz = (
            f"{Colores.VERDE}Válido{Colores.RESET}"
        )
    else:
        estado_voraz = (
            f"{Colores.ROJO}No encontrado{Colores.RESET}"
        )

    if len(resultado_backtracking) > 0:
        estado_backtracking = (
            f"{Colores.VERDE}Válido{Colores.RESET}"
        )
    else:
        estado_backtracking = (
            f"{Colores.ROJO}No encontrado{Colores.RESET}"
        )

    print(
        f"{'Fuerza Bruta':<20}"
        f"{tiempo_fuerza:<20.6f}"
        f"{estado_fuerza}"
    )

    print(
        f"{'Voraz':<20}"
        f"{tiempo_voraz:<20.6f}"
        f"{estado_voraz}"
    )

    print(
        f"{'Backtracking':<20}"
        f"{tiempo_backtracking:<20.6f}"
        f"{estado_backtracking}"
    )

    separador()

    print()
    print(
        f"{Colores.AZUL}"
        f"Fuerza Bruta:"
        f"{Colores.RESET} "
        f"{combinaciones} combinaciones evaluadas"
    )

    print(
        f"{Colores.AZUL}"
        f"Voraz:"
        f"{Colores.RESET} "
        f"{decisiones} decisiones realizadas"
    )

    print(
        f"{Colores.AZUL}"
        f"Backtracking:"
        f"{Colores.RESET} "
        "búsqueda mediante retroceso"
    )

    print()

    tiempos = (
        ("Fuerza Bruta", tiempo_fuerza),
        ("Voraz", tiempo_voraz),
        ("Backtracking", tiempo_backtracking)
    )

    algoritmo_mas_rapido = min(
        tiempos,
        key=lambda elemento: elemento[1]
    )

    print(
        f"{Colores.VERDE}"
        f"✓ Algoritmo más rápido en esta ejecución: "
        f"{algoritmo_mas_rapido[0]}"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.AMARILLO}"
        "Nota: los tiempos pueden variar ligeramente "
        "en cada ejecución."
        f"{Colores.RESET}"
    )


# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():

    print()

    print(
        f"{Colores.CYAN}"
        "╔══════════════════════════════════════════════════════════════╗"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.NEGRITA}{Colores.BLANCO}"
        "                       MENÚ PRINCIPAL                       "
        f"{Colores.RESET}"
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}"
        "╠══════════════════════════════════════════════════════════════╣"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.AMARILLO}"
        "  DATOS DEL SISTEMA"
        f"{Colores.RESET}"
        "                                           "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [1] Mostrar cursos"
        "                                      "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [2] Mostrar aulas"
        "                                       "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [3] Mostrar horarios"
        "                                    "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [4] Mostrar disponibilidad de profesores"
        "             "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        "                                                              "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.AMARILLO}"
        "  RESTRICCIONES"
        f"{Colores.RESET}"
        "                                           "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [5] Probar restricciones"
        "                              "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        "                                                              "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.AMARILLO}"
        "  ALGORITMOS"
        f"{Colores.RESET}"
        "                                              "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [6] Ejecutar Fuerza Bruta"
        "                             "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [7] Ejecutar Algoritmo Voraz"
        "                          "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [8] Ejecutar Backtracking"
        "                             "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        "                                                              "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.AMARILLO}"
        "  COMPARACIÓN"
        f"{Colores.RESET}"
        "                                            "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.BLANCO}"
        "  [9] Comparar los tres algoritmos"
        "                       "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        "                                                              "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}║"
        f"{Colores.ROJO}"
        "  [0] Salir"
        f"{Colores.RESET}"
        "                                                   "
        f"{Colores.CYAN}║"
        f"{Colores.RESET}"
    )

    print(
        f"{Colores.CYAN}"
        "╚══════════════════════════════════════════════════════════════╝"
        f"{Colores.RESET}"
    )


# ============================================================
# FUNCION PRINCIPAL
# ============================================================

def main():

    while True:

        limpiar_pantalla()

        mostrar_titulo()
        mostrar_menu()

        print()

        opcion = input(
            f"{Colores.AMARILLO}"
            "Seleccione una opción: "
            f"{Colores.RESET}"
        )

        if opcion == "1":

            limpiar_pantalla()
            mostrar_titulo()
            mostrar_cursos()
            pausar()

        elif opcion == "2":

            limpiar_pantalla()
            mostrar_titulo()
            mostrar_aulas()
            pausar()

        elif opcion == "3":

            limpiar_pantalla()
            mostrar_titulo()
            mostrar_horarios()
            pausar()

        elif opcion == "4":

            limpiar_pantalla()
            mostrar_titulo()
            mostrar_disponibilidad_profesores()
            pausar()

        elif opcion == "5":

            limpiar_pantalla()
            mostrar_titulo()
            probar_asignacion()
            pausar()

        elif opcion == "6":

            limpiar_pantalla()
            mostrar_titulo()
            ejecutar_fuerza_bruta()
            pausar()

        elif opcion == "7":

            limpiar_pantalla()
            mostrar_titulo()
            ejecutar_voraz()
            pausar()

        elif opcion == "8":

            limpiar_pantalla()
            mostrar_titulo()
            ejecutar_backtracking()
            pausar()

        elif opcion == "9":

            limpiar_pantalla()
            mostrar_titulo()
            comparar_algoritmos()
            pausar()

        elif opcion == "0":

            limpiar_pantalla()
            mostrar_titulo()

            print()
            mensaje_exito(
                "Gracias por utilizar el sistema."
            )

            print(
                f"{Colores.CYAN}"
                "Programa finalizado."
                f"{Colores.RESET}"
            )

            break

        else:

            print()
            mensaje_error(
                "Opción no válida."
            )

            print(
                f"{Colores.AMARILLO}"
                "Seleccione una opción del 0 al 9."
                f"{Colores.RESET}"
            )

            pausar()


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()