from modelos.horario import Horario
from algoritmo.generador import generar_horario
from datos.datos_prueba import cursos, docentes, salones, franjas

horario = Horario()

exito = generar_horario(cursos, docentes, salones, franjas, horario)

if exito:
    print("Horario generado:\n")
    for a in horario.asignaciones:
        print(a.curso.nombre, "-", a.docente.nombre, "-", a.salon.id, "-", a.franja.id)
else:
    print("No se pudo generar el horario")