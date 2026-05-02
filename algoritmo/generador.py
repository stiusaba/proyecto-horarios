from modelos.asignacion import Asignacion
from validadores.validador_docente import validar_docente
from validadores.validador_salon import validar_salon
from validadores.validador_capacidad import validar_capacidad

def generar_horario(cursos, docentes, salones, franjas, horario, index=0):

    # Ordenar cursos (heurística)
    cursos = sorted(cursos, key=lambda c: c.estudiantes, reverse=True)

    if index == len(cursos):
        return True

    curso = cursos[index]

    # Filtrar salones válidos primero (optimiza mucho)
    salones_validos = [s for s in salones if validar_capacidad(curso, s)]

    for salon in salones_validos:
        for franja in franjas:
            for docente in docentes:

                if not validar_docente(horario, docente, franja):
                    continue

                if not validar_salon(horario, salon, franja):
                    continue

                asignacion = Asignacion(docente, curso, salon, franja)
                horario.agregar(asignacion)

                if generar_horario(cursos, docentes, salones, franjas, horario, index + 1):
                    return True

                horario.eliminar_ultima()

    return False